/*  Arduino DC Motor Control - PWM | H-Bridge | L298N  -  Example 01

    by Dejan Nedelkovski, www.HowToMechatronics.com
*/

#define enA 5

#define in1 8
#define in2 9

int start = 0;
void setup() {
  pinMode(enA, OUTPUT);
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);

  // Set initial rotation direction
  digitalWrite(in1, LOW);
  digitalWrite(in2, HIGH);

  Serial.begin(9600);
}

void loop() {
  if (start == 0) {
    analogWrite(enA, 140);
    start = 1;
    delay(1000);
  }
   else if (start == 1) {
    analogWrite(enA, 100);
    start = 3;
    delay(1000);
  }
  else {
   analogWrite(enA,50); // Send PWM signal to L298N Enable pin
  }
}
