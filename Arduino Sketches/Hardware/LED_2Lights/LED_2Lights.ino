#include <FastLED.h>

#define LED_PIN     3
#define NUM_LEDS    2

CRGB leds[NUM_LEDS];

void setup() {

  FastLED.addLeds<APA104, LED_PIN, GRB>(leds, NUM_LEDS);
  leds[0] = CRGB (255, 255, 255);
  leds[1] = CRGB (255, 255, 255);

  FastLED.setBrightness(60);
  FastLED.show();
}

void loop() {

}
