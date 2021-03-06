#define STEPPER_FRONT_IN1 9
#define STEPPER_FRONT_IN2 10
#define STEPPER_FRONT_IN3 11
#define STEPPER_FRONT_IN4 12


#include <FastLED.h>
#include <Wire.h>
#include <Adafruit_Sensor.h>
#include "Adafruit_TSL2591.h"

//#define I2C_7BITADDR 0x68 // DS1307
//#define MEMLOC 0x0A 

int gateNum = 0;
long currLux = 0;
int PERF_THRESHOLD = 4000;
int lenPack = 1800;
bool foundPerf = false;
bool newPack = false;


Adafruit_TSL2591 tsl = Adafruit_TSL2591(2591);



void setup() {
    configureSensor();
    Serial.begin(115200);
    pinMode(STEPPER_FRONT_IN1, OUTPUT);
    pinMode(STEPPER_FRONT_IN2, OUTPUT);
    pinMode(STEPPER_FRONT_IN3, OUTPUT);
    pinMode(STEPPER_FRONT_IN4, OUTPUT);
  
    //FastLED.addLeds<APA104, BACK_LED_PIN, GRB>(backLED, NUM_LEDS);
  
    //turnOffBackLight();
    //nextPack(5000);
    //FastLED.setBrightness(255);
    //Serial.begin(9600);
}

void loop() {
    currLux = lightSensorRead();
    Serial.println(currLux);
    oneStep(true);
    
    if (newPack) {
      for (int i = 0;i <1300; i++) {
        oneStep(true);
      }
      newPack = false;
    }
    if (currLux > 160) {
      newPack = true;
    }
    /*
    if (currLux > 100) {
      oneStep(true);
      currLux = lightSensorRead();
      Serial.println(currLux);
    } else {
      oneStep(true);
      oneStep(true);
      oneStep(true);
      oneStep(true);
      oneStep(true);
      oneStep(true);
      oneStep(true);
    }
    */
//      currLux = 0;
//      foundPerf = findPerf();
// 
//      if (foundPerf) {
//
//        Serial.println("Found line");
//
//        delay(1000);
//
//        //turnOffBackLight();
//        //delay(500);
//        foundPerf = false;
//        //nextPack(lenPack);
//      }
 }



void configureSensor(void) {
   tsl.setGain(TSL2591_GAIN_LOW);      // 25x gain

   tsl.setTiming(TSL2591_INTEGRATIONTIME_100MS);  // shortest integration time (bright light)
}


long lightSensorRead(void) {
  uint32_t lum = tsl.getFullLuminosity();
  uint16_t ir, full;
  ir = lum >> 16;
  full = lum & 0xFFFF;
  return tsl.calculateLux(full, ir);
}

/*
 * void getFirstPack(void) {
  nextPack(3250); // moves first pill pack edge to the beginning of LED
  findPerf();
  nextPack(lenPack);
}

bool findPerf(void) {
  int numRotations = 0;
  
  while (currLux < PERF_THRESHOLD) {
    currLux = lightSensorRead();
    Serial.println(currLux);
    if (currLux < 140) {
      oneStep(true);
 
    }
    else {
      oneStep(true);
    }
    numRotations++;
  }
  
  return true;
}

void nextPack(int stepLen) {
  for(int i = 0; i < stepLen;i++){
    oneStep(true);
  }
}
void turnOnBackLight(void) {
  backLED[0] = CRGB (255, 255, 255);
  backLED[1] = CRGB (255, 255, 255);
  FastLED.show();
}

void turnOffBackLight(void) {
  backLED[0] = CRGB (0, 0, 0);
  backLED[1] = CRGB (0, 0, 0);
  FastLED.show();
}
*/

void oneStep(bool dir){
  delay(5);
  if(dir){
    switch(gateNum){
        case 0:
          digitalWrite(STEPPER_FRONT_IN1, HIGH);
          digitalWrite(STEPPER_FRONT_IN2, LOW);
          digitalWrite(STEPPER_FRONT_IN3, LOW);
          digitalWrite(STEPPER_FRONT_IN4, LOW);

          break;
        case 1:
          digitalWrite(STEPPER_FRONT_IN1, LOW);
          digitalWrite(STEPPER_FRONT_IN2, HIGH);
          digitalWrite(STEPPER_FRONT_IN3, LOW);
          digitalWrite(STEPPER_FRONT_IN4, LOW);

          break;
        case 2:
          digitalWrite(STEPPER_FRONT_IN1, LOW);
          digitalWrite(STEPPER_FRONT_IN2, LOW);
          digitalWrite(STEPPER_FRONT_IN3, HIGH);
          digitalWrite(STEPPER_FRONT_IN4, LOW);

          break;
        case 3:
          digitalWrite(STEPPER_FRONT_IN1, LOW);
          digitalWrite(STEPPER_FRONT_IN2, LOW);
          digitalWrite(STEPPER_FRONT_IN3, LOW);
          digitalWrite(STEPPER_FRONT_IN4, HIGH);

          break;
      } 
  } else {
      switch(gateNum){
        case 0:
          digitalWrite(STEPPER_FRONT_IN1, LOW);
          digitalWrite(STEPPER_FRONT_IN2, LOW);
          digitalWrite(STEPPER_FRONT_IN3, LOW);
          digitalWrite(STEPPER_FRONT_IN4, HIGH);

          break;
        case 1:
          digitalWrite(STEPPER_FRONT_IN1, LOW);
          digitalWrite(STEPPER_FRONT_IN2, LOW);
          digitalWrite(STEPPER_FRONT_IN3, HIGH);
          digitalWrite(STEPPER_FRONT_IN4, LOW);

          break;
        case 2:
          digitalWrite(STEPPER_FRONT_IN1, LOW);
          digitalWrite(STEPPER_FRONT_IN2, HIGH);
          digitalWrite(STEPPER_FRONT_IN3, LOW);
          digitalWrite(STEPPER_FRONT_IN4, LOW);

          break;
        case 3:
          digitalWrite(STEPPER_FRONT_IN1, HIGH);
          digitalWrite(STEPPER_FRONT_IN2, LOW);
          digitalWrite(STEPPER_FRONT_IN3, LOW);
          digitalWrite(STEPPER_FRONT_IN4, LOW);

          break;
      } 
  }
  gateNum++;
  if(gateNum > 3) {
    gateNum = 0;
  }
}
