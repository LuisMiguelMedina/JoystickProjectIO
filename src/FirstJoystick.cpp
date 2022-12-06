#include <Arduino.h>
int d8 =8;
int d7 =7;

void setup() {
  
  pinMode(d7,INPUT_PULLUP);
Serial.begin(9600);

 pinMode(d8,INPUT_PULLUP);
Serial.begin(9600);
}
void loop() {
  int X = analogRead(A1);
  int Y = analogRead(A0);
  int x = map(X, 1, 1023, 1023, 1);
  int y = map(Y, 1, 1023, 1, 1023);
  int X2 = analogRead(A3);
  int Y2 = analogRead(A2);
  int x2 = map(X2, 1, 1023, 1023, 1);
  int y2 = map(Y2, 1, 1023, 1, 1023);

if(digitalRead(d7)==LOW){
Serial.print("5");
}
if(digitalRead(d8)==LOW){
Serial.print("c");
}else{
  Serial.print("z");
}
Serial.print(" ");
Serial.print(x);
Serial.print(" ");
Serial.print(y);
Serial.print(" ");
Serial.println("m");

if(y2 > 800) {
  Serial.print("1");
}
if(y2 < 200) {
  Serial.print("2");
}
// for some reason neutral x = 900!!!
if(x2 < 600) {
  Serial.print("3");
}
if(x2 > 1200) {
  Serial.print("4");
}
delay(180);
}