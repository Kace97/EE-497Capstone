#define readRaspiPin 0
#define sendRaspiPin 3

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
  
  readVoltage = readVal_Raspi * (5.0 / 1023.0);
  Serial.println(readVoltage);
  if (readVoltage > 2) {
    movePills = true;
    analogWrite(sendRaspiPin, sendVal_Raspi * (1023.0 / 5.0));// send signal to Raspi that we are starting
    digitalWrite(ledPin, HIGH);
  }

  if (movePills) {
    movePills = false; 
    delay(1000);
    analogWrite(sendRaspiPin,0.0);
    
    digitalWrite(ledPin, LOW);
    
  }
  delay(50);
}
