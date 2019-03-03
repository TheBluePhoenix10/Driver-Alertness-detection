/* Connections:
 *  Orange wire of servo: PA9 (indicates the car has started or not)
 *  green LED: PA5 (indicates the car can start)
 *  Red LED: PC13 (indicates the driver is drunk)
 *  Alcohol Sensor input: PA0 
 */


#include <Servo.h>
int value;
int thresh=100;
Servo myservo;
void setup() {
Serial.begin(115200);
pinMode(PC13, OUTPUT);
pinMode(PA10, OUTPUT);
pinMode(PA7, OUTPUT);
pinMode(PA5, OUTPUT);
pinMode(PB10, INPUT);
digitalWrite(PA5, HIGH);
digitalWrite(PC13, LOW); 
digitalWrite(PB1,HIGH);
myservo.attach(9);
myservo.write(0);
}

void loop(){
  value= analogRead(PA0);
  Serial.print("Alcohol value: ");
  Serial.println(value);
  delay(100);
  if(value > thresh) {
    Serial.print("Alcohol detected: ");
    digitalWrite(PC13, HIGH);
    digitalWrite(PA5, LOW);
    myservo.write(0);
    delay(15);
  }
  
  else if(digitalRead(PA15) == LOW) {
    Serial.print("Car started... ");
    if(!digitalRead(PC13)) {
      digitalWrite(PA5, HIGH);
      myservo.write(45);
      delay(15);  
    }
  }
}
