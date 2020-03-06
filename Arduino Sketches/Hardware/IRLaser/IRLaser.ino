
int IRPin = 3;

void setup() {
  Serial.begin(9600);
}

void loop() {
  Serial.println(digitalRead(IRPin));
  delay(100);
}
