#include <FastLED.h>


#define BACK_LED_PIN 3
#define FRONT_LED_PIN 2
#define NUM_LEDS 2

CRGB backLED[NUM_LEDS];
CRGB frontLED[NUM_LEDS];

void setup() {


  FastLED.addLeds<APA104, BACK_LED_PIN, GRB>(backLED, NUM_LEDS);
  FastLED.addLeds<APA104, FRONT_LED_PIN, GRB>(frontLED, NUM_LEDS);
  
  turnOffBackLight();
  turnOffFrontLight();
  
  Serial.begin(9600);

}

void loop() {
  /*
   * Testing Arduino sending message
  Serial.println("on"); // prints to Raspi
  delay(10000); 
  */

  if (Serial.available() > 0) {
    String line = Serial.readStringUntil('\n');
    if (line == "on") {
      //nextPack(lenPack);
      turnOnBackLight();
      delay(500);
      turnOffBackLight();
      delay(500);
      //Serial.println("back");
      
      
      /*
      while (line != "took contour") {
        line = Serial.readStringUntil('\n');
      }
      turnOffBackLight();
      turnOnFrontLight();
      Serial.println("front light on");
      while (line != "took front photo") {
        line = Serial.readStringUntil('\n');
      }
      turnOffFrontLight();
      */
    }
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

void turnOnFrontLight(void) {
  frontLED[0] = CRGB (255, 255, 255);
  frontLED[1] = CRGB (255, 255, 255);
  FastLED.show();
}

void turnOffFrontLight(void) {
  frontLED[0] = CRGB (0, 0, 0);
  frontLED[1] = CRGB (0, 0, 0);
  FastLED.show();
}
