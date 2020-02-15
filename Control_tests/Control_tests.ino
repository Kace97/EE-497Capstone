/*********************************************************************************************
 * Summary:
 * This sketch is only being used to regain familiarity with motor control using arduino
 * Sketch is also useful for ensuring a control method for a specific motor
 * 
 ********************************************************************************************/

 /*
  * Include the needed files for this sketch
  */
#include <Servo.h>

/*
 * motor control pins
 */
int in1 = 8;
int in2 = 9;
int in3= 10;
int in4 = 11;
Servo EnA;
Servo EnB;

/*
 * digital inputs
 */
int on_off = 3;
int direc = 2;

/*
 * globals
 */
 unsigned long lastTime = millis();
boolean on = true;
void setup() {
  //set up signals for motor A
  EnA.attach(5);
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  digitalWrite(in1, HIGH);
  digitalWrite(in2, LOW);
  //set up signals for motor B
  EnB.attach(6);
  pinMode(in3, OUTPUT);
  pinMode(in4, OUTPUT);
  digitalWrite(in3, HIGH);
  digitalWrite(in4, LOW);
  //set up serial communication
  Serial.begin(115200);

  
  //attach interrupt
  attachInterrupt(direc, toggle_direction, CHANGE);
  attachInterrupt(on_off, toggle_on, CHANGE);
  Serial.println("Setup Complete!");
}

void loop() {
 int potValue = analogRead(A0);
 int PWM_speed = map(potValue, 0, 1023, 0, 255);
 if(on){
  EnA.write(PWM_speed);
  EnB.write(PWM_speed);
  if(((millis() - lastTime) / 1000) < 1){
    Serial.println(PWM_speed);
  }
 }
 else{
  EnA.write(0);
  EnB.write(0);
 }
}

void toggle_on(){
  on ^= on;
  Serial.println("on = ");
  Serial.print(on);
}

void toggle_direction(){
  //change direction of motA
  digitalWrite(in1, LOW);
  digitalWrite(in2, HIGH);
  //change direction of motB
  digitalWrite(in3, LOW);
  digitalWrite(in4, HIGH);
}
