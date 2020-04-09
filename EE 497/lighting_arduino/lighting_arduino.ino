 #include <FastLED.h>

#define LED_PIN     7
#define NUM_LEDS    20
#define BUTTON_PIN    3

// variables will change:
int buttonState = 0;         // variable for reading the pushbutton status

CRGB leds[NUM_LEDS];

void setup() {

  FastLED.addLeds<WS2812, LED_PIN, GRB>(leds, NUM_LEDS);
  pinMode(BUTTON_PIN, INPUT);
  pinMode(LED_PIN, OUTPUT);

}

void loop() {

    // read the state of the pushbutton value:
  buttonState = digitalRead(BUTTON_PIN);

  // check if the pushbutton is pressed. If it is, the buttonState is HIGH:
  if (buttonState == HIGH) {
    // turn LED on:
    leds[0] = CRGB(255, 255, 255);
    FastLED.show();

  } else {
    // turn LED off:
    leds[0] = CRGB(0, 0, 0);
    FastLED.show();
  }
  


}
