#define STEPPER_FRONT_IN1 9
#define STEPPER_FRONT_IN2 10
#define STEPPER_FRONT_IN3 11
#define STEPPER_FRONT_IN4 12

#define STEPPER_BACK_IN1 4
#define STEPPER_BACK_IN2 5
#define STEPPER_BACK_IN3 6
#define STEPPER_BACK_IN4 7

int stepNum = 0;
void setup() {
  pinMode(STEPPER_FRONT_IN1, OUTPUT);
  pinMode(STEPPER_FRONT_IN2, OUTPUT);
  pinMode(STEPPER_FRONT_IN3, OUTPUT);
  pinMode(STEPPER_FRONT_IN4, OUTPUT);
  pinMode(STEPPER_BACK_IN1, OUTPUT);
  pinMode(STEPPER_BACK_IN2, OUTPUT);
  pinMode(STEPPER_BACK_IN3, OUTPUT);
  pinMode(STEPPER_BACK_IN4, OUTPUT);

}

void loop() {
  for(int i = 0; i < 4000;i++){
    OneStep(true);
  }
  delay(500);
  for(int i = 0; i < 6000;i++){
    OneStep(true);
  }
  delay(1000);
}


void OneStep(bool dir){
  delay(5);
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
