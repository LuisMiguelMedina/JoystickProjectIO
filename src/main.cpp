#include <Arduino.h>
#include <AlignedJoy.h>

// joystick 1
#define PIN_JOY1_X   0  //(up  down)
#define PIN_JOY1_Y   1  //(left  right)
// joystick 2
#define PIN_JOY2_X   2  //(up  down)
#define PIN_JOY2_Y   3  //(left  right)

AlignedJoy joystick_1(PIN_JOY1_X, PIN_JOY1_Y);
AlignedJoy joystick_2(PIN_JOY2_X, PIN_JOY2_Y);

// 0 to 1023
void setup() {
 // DEBUG
 Serial.begin(9600);
 while(!Serial){} 
}

void loop() {

 // print joystick 1 axes value
 Serial.print("joystick_1 X -> ");
 Serial.print(joystick_1.read(X));
 Serial.print(" | Y -> ");
 Serial.print(joystick_1.read(Y));
 
 // print joystick 1 axes value
 Serial.print(" -|- joystick_2 X -> ");
 Serial.print(joystick_2.read(X));
 Serial.print(" | Y -> ");
 Serial.println(joystick_2.read(Y));
 delay(500);
}