#include <Arduino.h>
int d8 =8;

void setup() {
  pinMode(d8,INPUT_PULLUP);

  Serial.begin(9600);
}
void loop() {
  int X2 = analogRead(A1);
  int Y2 = analogRead(A0);
  int X = analogRead(A3);
  int Y = analogRead(A2);
  int x = map(X, 1, 1023, 1917, 2);
  int y = map(Y, 1, 1023, 2, 1077);
  int x2 = map(X2, 1, 1023, 1077, 2);
  int y2 = map(Y2, 1, 1023, 2, 1077);
  int h,i,j,k;

if(digitalRead(d8)==LOW){
Serial.print("c");

}else{
  Serial.print("z");
}
 //split arrangement
if(y2 > 800) {
  h = 1;
} else {
  h = 0;
}
if(y2 < 200) {
  i = 2;
} else {
  i = 0;
}
if(x2 > 800) {
  j = 3;
} else {
  j = 0;
}
if(x2 < 200) {
  k = 4;
}else {
  k = 0;
}
//FirstJoystick
Serial.print(" ");
Serial.print(x);
Serial.print(" ");
Serial.print(y);
Serial.print(" ");
//SecondJoystick
Serial.print(" ");
Serial.print(x2);
Serial.print(" ");
Serial.print(y2);
Serial.print(" ");
Serial.print(" ");
Serial.print(h);
Serial.print(" ");
Serial.print(i);
Serial.print(" ");
Serial.print(j);
Serial.print(" ");
Serial.print(k);
Serial.print(" ");
Serial.println("m");
delay(180);
}