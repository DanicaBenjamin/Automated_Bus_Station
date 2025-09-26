// program controlling the IR sensors and RFID sensor
#include <Arduino.h>
#include <SPI.h>
#include <MFRC522.h>


#define PIN_RST 42
#define PIN_SS 41
#define PIN_SCK 40
#define PIN_MOSI 39
#define PIN_MISO 38

#define PIN_ENTRY 6
#define PIN_EXIT 7 

MFRC522 rfid(PIN_SS, PIN_RST);
int cardCount = 0;

void setup() {
  Serial.begin(115200);

  pinMode(PIN_ENTRY, INPUT);
  pinMode(PIN_EXIT, INPUT);
  xTaskCreatePinnedToCore(entryIR, "entryIR", 2000, NULL, 1, NULL, 1);
  xTaskCreatePinnedToCore(exitIR, "exitIR", 2000, NULL, 1, NULL, 1);

  SPI.begin(PIN_SCK, PIN_MISO, PIN_MOSI, PIN_SS);
  rfid.PCD_Init();
  byte v = rfid.PCD_ReadRegister(rfid.VersionReg);
  Serial.println(v, HEX);
}

bool wait1 = false;
bool wait2 = false;  
int people = 0; 

void entryIR(void *pvParameters) {
  for(;;) { 
    while(digitalRead(PIN_ENTRY) == LOW) {
      wait1 = true; 
    } 
    if(wait1) {
      Serial.println(++people); 
    }
  wait1 = false; 
  }
}

void exitIR(void *pvParameters) {
  for(;;) { 
    while(digitalRead(PIN_EXIT) == LOW) {
      wait2 = true; 
    } 
    if((wait2) && (people > 0)) {
      Serial.println(--people); 
    }
  wait2 = false; 
  }
}

void loop() {
  if(!rfid.PICC_IsNewCardPresent()) {
    return;
  }
  if(!rfid.PICC_ReadCardSerial()) {
    return; 
  }

  Serial.printf("\nNew Card Detected %d", ++cardCount);
  Serial.printf("\nCard UID: %s", uidToString(&rfid.uid));

  MFRC522::PICC_Type type = rfid.PICC_GetType(rfid.uid.sak);
  Serial.printf("\nCard type: %s", rfid.PICC_GetTypeName(type));
  Serial.println(); 
  rfid.PICC_HaltA();
  rfid.PCD_StopCrypto1(); 
}

String uidToString(MFRC522::Uid *uid) {
  String content = "";
  for (byte i = 0; i < uid->size; i++) {
    if (uid->uidByte[i] < 0x10) content += "0";
    content += String(uid->uidByte[i], HEX);
  }
  content.toUpperCase();
  return content;
}
