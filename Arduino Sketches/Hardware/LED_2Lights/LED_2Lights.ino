#include <FastLED.h>

#define LED_PIN     2
#define LED_PIN2    3
#define NUM_LEDS    2

CRGB leds[NUM_LEDS];
CRGB leds2[NUM_LEDS];

void setup() {

  FastLED.addLeds<APA104, LED_PIN, GRB>(leds, NUM_LEDS);
  leds[0] = CRGB (255, 255, 255);
  leds[1] = CRGB (255, 255, 255);

  FastLED.setBrightness(255);
  FastLED.show();

  FastLED.addLeds<APA104, LED_PIN2, GRB>(leds2, NUM_LEDS);
  leds2[0] = CRGB (255, 255, 255);
  leds2[1] = CRGB (255, 255, 255);

  FastLED.setBrightness(255);
  FastLED.show();
}

void loop() {

}
