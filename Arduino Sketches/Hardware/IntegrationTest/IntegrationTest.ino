#define readRaspiPin 1
#define sendRaspiPin 2

int readVal_Raspi = 0;
int sendVal_Raspi = 3.3;
float readVoltage = 0;
bool movePills = false;
int counter = 0;

void setup() {
  Serial.begin(115200);

}

void loop() {
  readVal_Raspi = analogRead(readRaspiPin);
  readVoltage = readVal_Raspi * (5.0 / 1023.0);
  if (readVoltage > 2) {
    movePills = true;
    analogWrite(sendRaspiPin, sendVal_Raspi * (1023.0 / 5.0));// send signal to Raspi that we are starting
  }
  while (movePills) {
    counter++;
    Serial.println("I'm doing stuffffff");
    if (counter > 5) {
      movePills = false; 
    }
    analogWrite(sendRaspiPin,0);
    counter = 0;
    delay(300);
  }
}
