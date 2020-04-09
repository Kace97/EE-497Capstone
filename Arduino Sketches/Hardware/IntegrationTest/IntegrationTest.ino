#define readRaspiPin 1
#define sendRaspiPin 2

int readVal_Raspi = 0;
int sendVal_Raspi = 3.3;
float readVoltage = 0;
bool movePills = false;
int counter = 0;
int ledPin = 3;

void setup() {
  Serial.begin(115200);

}

void loop() {
  readVal_Raspi = analogRead(readRaspiPin);
  Serial.println(readVal_Raspi);
  readVoltage = readVal_Raspi * (5.0 / 1023.0);
  if (readVoltage > 2) {
    movePills = true;
    analogWrite(sendRaspiPin, sendVal_Raspi * (1023.0 / 5.0));// send signal to Raspi that we are starting
    digitalWrite(ledPin, HIGH);
  }
  while (movePills) {
    counter++;
    
    if (counter > 3) {
      movePills = false; 
      digitalWrite(ledPin, LOW);
      analogWrite(sendRaspiPin,0);
      counter = 0;
    }
    delay(500);
  }
  
}
