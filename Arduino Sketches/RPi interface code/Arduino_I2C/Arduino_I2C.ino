/*
include needed files
*/
#include <Wire.h>

/* 
 Define the led pins
 */
#define green_LED 6
#define yellow_LED 5
#define white_LED 4
#define red_LED 3
#define blue_LED 2

byte function = 0;
byte color = 0;

byte const message_to_Pi [2] = {88, 1};

void setup() {
  // put your setup code here, to run once:
  Wire.begin(5);
  Wire.onReceive(receiveEvent);
  pinMode(green_LED, OUTPUT);
  pinMode(yellow_LED, OUTPUT);
  pinMode(white_LED, OUTPUT);
  pinMode(red_LED, OUTPUT);
  pinMode(blue_LED, OUTPUT);
  digitalWrite(green_LED, HIGH);
  delay(500);
  digitalWrite(green_LED, LOW);
}

void loop() {
  delay(100);
}

void receiveEvent(int howMany){
  if(Wire.available()){
    function = Wire.read();
  }
  if(Wire.available()){
    color = Wire.read();
  }
  if(function == 0){
    turn_off_LED(color);
  }

  else if(function == 15){
    turn_on_LED(color);
  }
  if(Wire.available())
    Wire.write(message_to_Pi, 2);
}

void turn_off_LED(byte color){
  if(color == 0)
    digitalWrite(green_LED, LOW);
  else if(color == 1)
    digitalWrite(yellow_LED, LOW);
  else if(color == 2)
    digitalWrite(white_LED, LOW);
  else if(color == 3)
    digitalWrite(red_LED, LOW);
  else if(color == 4)
    digitalWrite(blue_LED, LOW);
  else if(color == 7){
    digitalWrite(green_LED, LOW);
    digitalWrite(yellow_LED, LOW);
    digitalWrite(white_LED, LOW);
    digitalWrite(red_LED, LOW);
    digitalWrite(blue_LED, LOW);
  }
}

void turn_on_LED(byte color){
  if(color == 0)
    digitalWrite(green_LED, HIGH);
  else if(color == 1)
    digitalWrite(yellow_LED, HIGH);
  else if(color == 2)
    digitalWrite(white_LED, HIGH);
  else if(color == 3)
    digitalWrite(red_LED, HIGH);
  else if(color == 4)
    digitalWrite(blue_LED, HIGH);
  else if(color == 7){
    digitalWrite(green_LED, HIGH);
    digitalWrite(yellow_LED, HIGH);
    digitalWrite(white_LED, HIGH);
    digitalWrite(red_LED, HIGH);
    digitalWrite(blue_LED, HIGH);
  }
}
