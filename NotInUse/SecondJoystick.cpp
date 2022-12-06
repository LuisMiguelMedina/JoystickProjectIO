#include <Arduino.h>
int d7 =7;

void setup() {
 pinMode(d7,INPUT_PULLUP);
Serial.begin(9600);
}

void loop() {
  int X = analogRead(A3);
  int Y = analogRead(A2);
  int x = map(X, 1, 1023, 1077, 2);
  int y = map(Y, 1, 1023, 2, 1077);
  
  if(digitalRead(d7)==LOW){
  Serial.print("5");
  }

  if(y > 800) {
    Serial.print("1");
  }
  if(y < 200) {
    Serial.print("2");
  }
  // for some reason neutral x = 900!!!

  if(x < 600) {
    Serial.print("3");
  }
  if(x > 1200) {
    Serial.print("4");
  }
}