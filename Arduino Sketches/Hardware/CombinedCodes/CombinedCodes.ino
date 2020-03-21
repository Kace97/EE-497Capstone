#include <Wire.h>
#include <FastLED.h>
#include <Adafruit_Sensor.h> // if error, add Adafruit Unified Sensor and adafruit tsl2591
#include "Adafruit_TSL2591.h"

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
#define NUM_LEDS 1

CRGB bottomLED[NUM_LEDS];
CRGB frontLED[NUM_LEDS];

int gateStep = 0;
int numSteps = 0;
long currentLux = 0;
bool gotFirstPack = false;
int PERF_THRESHOLD = 23;
int lengthPack = 2000;

Adafruit_TSL2591 tsl = Adafruit_TSL2591(2591); 


void configureSensor(void) {
   tsl.setGain(TSL2591_GAIN_MED);      // 25x gain

   tsl.setTiming(TSL2591_INTEGRATIONTIME_100MS);  // shortest integration time (bright light)

  /* Display the gain and integration time for reference sake */  
  Serial.println(F("------------------------------------"));
  Serial.print  (F("Gain:         "));
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


void setup() {
  Serial.begin(115200);
  pinMode(STEPPER_FRONT_IN1, OUTPUT);
  pinMode(STEPPER_FRONT_IN2, OUTPUT);
  pinMode(STEPPER_FRONT_IN3, OUTPUT);
  pinMode(STEPPER_FRONT_IN4, OUTPUT);
  pinMode(STEPPER_BACK_IN1, OUTPUT);
  pinMode(STEPPER_BACK_IN2, OUTPUT);
  pinMode(STEPPER_BACK_IN3, OUTPUT);
  pinMode(STEPPER_BACK_IN4, OUTPUT);
  
  configureSensor();

  FastLED.addLeds<APA104, BACK_LED_PIN, GRB>(bottomLED, NUM_LEDS);
  FastLED.addLeds<APA104, FRONT_LED_PIN, GRB>(frontLED, NUM_LEDS);
  bottomLED[0] = CRGB ( 0, 0, 0);
  bottomLED[1] = CRGB ( 0, 0, 0);
  frontLED[0] = CRGB ( 0, 0, 0);
  frontLED[1] = CRGB ( 0, 0, 0);
  FastLED.show();
}

void loop() {
  if (!gotFirstPack) {
    nextPack(3250); // moves first pill pack edge to the beginning of LED
    while (currentLux < PERF_THRESHOLD) {
      currentLux = advancedRead();
      OneStep(true);
    }
    gotFirstPack = true;
    nextPack(lengthPack);
  } else {
    currentLux = advancedRead();
    Serial.println(currentLux);
    if (currentLux < PERF_THRESHOLD){
      OneStep(true);
    } else {
      Serial.println("found a line");
      delay(10000);
      nextPack(lengthPack);
    }
  }
}

void nextPack(int stepLength) {
  for(int i = 0; i < stepLength;i++){
    OneStep(true);
  }
}

long advancedRead(void) {
  uint32_t lum = tsl.getFullLuminosity();
  uint16_t ir, full;
  ir = lum >> 16;
  full = lum & 0xFFFF;
  return tsl.calculateLux(full, ir);
}

void OneStep(bool dir){
  delay(2);
  if(dir){
    switch(gateStep){
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
      switch(gateStep){
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
  gateStep++;
  if(gateStep > 3) {
    gateStep = 0;
  }
}
