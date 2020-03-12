/*
 * Runs 2 LED strips, 2 stepper motors, and 1 light sensor together.
 * The motors will slowly move until a bright light (perforation) is 
 * detected. When the perforation is detected, the backlight LEDs will 
 * first flash on for 4 seconds. Then, the front LEDs will flash for 
 * another 4 seconds. Afterwards, the motors will move the pill pack
 * slightly so that it is no longer on the perforation
*/



#include <Wire.h>
#include <FastLED.h>
#include <Adafruit_Sensor.h>
#include "Adafruit_TSL2591.h"

Adafruit_TSL2591 tsl = Adafruit_TSL2591(2591); 
// if error, add Adafruit Unified Sensor and adafruit tsl2591


#define STEPPER_FRONT_IN1 9
#define STEPPER_FRONT_IN2 10
#define STEPPER_FRONT_IN3 11
#define STEPPER_FRONT_IN4 12

#define STEPPER_BACK_IN1 4
#define STEPPER_BACK_IN2 5
#define STEPPER_BACK_IN3 6
#define STEPPER_BACK_IN4 7

#define BACK_LED_PIN 3
#define FRONT_LED_PIN 2
#define NUM_LEDS    2

CRGB bottomLED[NUM_LEDS];
CRGB frontLED[NUM_LEDS];

int stepNum = 0;
int curLux = 0;

void setup() {
  pinMode(STEPPER_FRONT_IN1, OUTPUT);
  pinMode(STEPPER_FRONT_IN2, OUTPUT);
  pinMode(STEPPER_FRONT_IN3, OUTPUT);
  pinMode(STEPPER_FRONT_IN4, OUTPUT);
  pinMode(STEPPER_BACK_IN1, OUTPUT);
  pinMode(STEPPER_BACK_IN2, OUTPUT);
  pinMode(STEPPER_BACK_IN3, OUTPUT);
  pinMode(STEPPER_BACK_IN4, OUTPUT);
  
  configureSensor();
  Serial.begin(112500);
  
  FastLED.addLeds<APA104, BACK_LED_PIN, GRB>(bottomLED, NUM_LEDS);
  FastLED.addLeds<APA104, FRONT_LED_PIN, GRB>(frontLED, NUM_LEDS);
  bottomLED[0] = CRGB ( 0, 0, 0);
  bottomLED[1] = CRGB ( 0, 0, 0);
  frontLED[0] = CRGB ( 0, 0, 0);
  frontLED[1] = CRGB ( 0, 0, 0);
  FastLED.show();
}

void loop() {
  curLux = getLuxValues();
  if (curLux < 190) { // 190 = lux value when there is a perforation
      OneStep(false); // take one step if there is no perforation
      delay(2);
  } else {
    Serial.println("Found a line");
    bottomLED[0] = CRGB ( 255, 255, 255);
    bottomLED[1] = CRGB ( 255, 255, 255);
    FastLED.show();
    delay(4000); // take back picture here
    bottomLED[0] = CRGB ( 0, 0, 0);
    bottomLED[1] = CRGB ( 0, 0, 0);
    frontLED[0] = CRGB ( 255, 255, 255);
    frontLED[1] = CRGB ( 255, 255, 255);
    FastLED.show();
    delay(4000); // take front picture here
    frontLED[0] = CRGB ( 0, 0, 0);
    frontLED[1] = CRGB ( 0, 0, 0);
    for (int i = 0; i <= 60; i++) { // take 60 steps to get off perforation
      OneStep(false); 
      delay(2);
    }
  }
  Serial.println(curLux);
}

void configureSensor(void) {
  
  tsl.setGain(TSL2591_GAIN_MED);      // 25x gain
  tsl.setTiming(TSL2591_INTEGRATIONTIME_100MS);  // shortest integration time (bright light)
  tsl2591Gain_t gain = tsl.getGain();
  switch(gain) {
    case TSL2591_GAIN_LOW:
      Serial.println(F("1x (Low)"));
      break;
    case TSL2591_GAIN_MED:
      Serial.println(F("25x (Medium)"));
      break;
    case TSL2591_GAIN_HIGH:
      Serial.println(F("428x (High)"));
      break;
    case TSL2591_GAIN_MAX:
      Serial.println(F("9876x (Max)"));
      break;
  }
}


// Reads and returns current lux value from TSL2591 light sensor
long getLuxValues(void)
{
  uint32_t lum = tsl.getFullLuminosity();
  uint16_t ir, full;
  ir = lum >> 16;
  full = lum & 0xFFFF;
  int lux = tsl.calculateLux(full, ir);
  return lux;
}

void OneStep(bool dir){
  if(dir){
    switch(stepNum){
        case 0:
          digitalWrite(STEPPER_FRONT_IN1, HIGH);
          digitalWrite(STEPPER_FRONT_IN2, LOW);
          digitalWrite(STEPPER_FRONT_IN3, LOW);
          digitalWrite(STEPPER_FRONT_IN4, LOW);
          digitalWrite(STEPPER_BACK_IN1, HIGH);
          digitalWrite(STEPPER_BACK_IN2, LOW);
          digitalWrite(STEPPER_BACK_IN3, LOW);
          digitalWrite(STEPPER_BACK_IN4, LOW);
          break;
        case 1:
          digitalWrite(STEPPER_FRONT_IN1, LOW);
          digitalWrite(STEPPER_FRONT_IN2, HIGH);
          digitalWrite(STEPPER_FRONT_IN3, LOW);
          digitalWrite(STEPPER_FRONT_IN4, LOW);
          digitalWrite(STEPPER_BACK_IN1, LOW);
          digitalWrite(STEPPER_BACK_IN2, HIGH);
          digitalWrite(STEPPER_BACK_IN3, LOW);
          digitalWrite(STEPPER_BACK_IN4, LOW);
          break;
        case 2:
          digitalWrite(STEPPER_FRONT_IN1, LOW);
          digitalWrite(STEPPER_FRONT_IN2, LOW);
          digitalWrite(STEPPER_FRONT_IN3, HIGH);
          digitalWrite(STEPPER_FRONT_IN4, LOW);
          digitalWrite(STEPPER_BACK_IN1, LOW);
          digitalWrite(STEPPER_BACK_IN2, LOW);
          digitalWrite(STEPPER_BACK_IN3, HIGH);
          digitalWrite(STEPPER_BACK_IN4, LOW);
          break;
        case 3:
          digitalWrite(STEPPER_FRONT_IN1, LOW);
          digitalWrite(STEPPER_FRONT_IN2, LOW);
          digitalWrite(STEPPER_FRONT_IN3, LOW);
          digitalWrite(STEPPER_FRONT_IN4, HIGH);
          digitalWrite(STEPPER_BACK_IN1, LOW);
          digitalWrite(STEPPER_BACK_IN2, LOW);
          digitalWrite(STEPPER_BACK_IN3, LOW);
          digitalWrite(STEPPER_BACK_IN4, HIGH);
          break;
      } 
  } else {
      switch(stepNum){
        case 0:
          digitalWrite(STEPPER_FRONT_IN1, LOW);
          digitalWrite(STEPPER_FRONT_IN2, LOW);
          digitalWrite(STEPPER_FRONT_IN3, LOW);
          digitalWrite(STEPPER_FRONT_IN4, HIGH);
          digitalWrite(STEPPER_BACK_IN1, LOW);
          digitalWrite(STEPPER_BACK_IN2, LOW);
          digitalWrite(STEPPER_BACK_IN3, LOW);
          digitalWrite(STEPPER_BACK_IN4, HIGH);
          break;
        case 1:
          digitalWrite(STEPPER_FRONT_IN1, LOW);
          digitalWrite(STEPPER_FRONT_IN2, LOW);
          digitalWrite(STEPPER_FRONT_IN3, HIGH);
          digitalWrite(STEPPER_FRONT_IN4, LOW);
          digitalWrite(STEPPER_BACK_IN1, LOW);
          digitalWrite(STEPPER_BACK_IN2, LOW);
          digitalWrite(STEPPER_BACK_IN3, HIGH);
          digitalWrite(STEPPER_BACK_IN4, LOW);
          break;
        case 2:
          digitalWrite(STEPPER_FRONT_IN1, LOW);
          digitalWrite(STEPPER_FRONT_IN2, HIGH);
          digitalWrite(STEPPER_FRONT_IN3, LOW);
          digitalWrite(STEPPER_FRONT_IN4, LOW);
          digitalWrite(STEPPER_BACK_IN1, LOW);
          digitalWrite(STEPPER_BACK_IN2, HIGH);
          digitalWrite(STEPPER_BACK_IN3, LOW);
          digitalWrite(STEPPER_BACK_IN4, LOW);
          break;
        case 3:
          digitalWrite(STEPPER_FRONT_IN1, HIGH);
          digitalWrite(STEPPER_FRONT_IN2, LOW);
          digitalWrite(STEPPER_FRONT_IN3, LOW);
          digitalWrite(STEPPER_FRONT_IN4, LOW);
          digitalWrite(STEPPER_BACK_IN1, HIGH);
          digitalWrite(STEPPER_BACK_IN2, LOW);
          digitalWrite(STEPPER_BACK_IN3, LOW);
          digitalWrite(STEPPER_BACK_IN4, LOW);
          break;
      } 
  }
  stepNum++;
  if(stepNum > 3) {
    stepNum = 0;
  }
}
