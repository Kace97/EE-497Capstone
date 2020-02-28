#include <Stepper.h>
#include <Wire.h>
#include <Adafruit_Sensor.h>
#include "Adafruit_TSL2591.h"

#define STEPS_PER_MIN 2038 

Adafruit_TSL2591 tsl = Adafruit_TSL2591(2591);
Stepper stepper(STEPS_PER_MIN, 8, 10, 9, 11);

boolean onLine = false; 
float currentLux = 0;
 
void setup() {
  Serial.begin(115200);
  stepper.setSpeed(2);
  configureSensor();
}

void loop() {
  currentLux = getLux();
  if (currentLux < 200) {
    stepper.step(STEPS_PER_MIN/4); // do 2038 steps -- corresponds to one revolution in one minute
  }
  else {
    Serial.println("Found a line");
    delay(10000);
    stepper.step(STEPS_PER_MIN/4);
  }

void configureSensor(void) {
  tsl.setGain(TSL2591_GAIN_MED);   

   tsl.setTiming(TSL2591_INTEGRATIONTIME_300MS);

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

float getLux(void)
{

  uint32_t lum = tsl.getFullLuminosity();
  uint16_t ir, full;
  ir = lum >> 16;
  full = lum & 0xFFFF;
  newLux = tsl.calculateLux(full, ir);
  return newLux;
}
