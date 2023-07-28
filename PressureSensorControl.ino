#include <Servo.h>
Servo myservo;
#define sensorPin A1
#define WINDOW_SIZE 20
#define ServoPin A0
int INDEX=0;
int emgreading=0;
int servoAngleint;
int SUM=0;
int READINGS[WINDOW_SIZE];
int AVERAGED;

void setup() {
  Serial.begin(9600);
   pinMode(sensorPin,INPUT);
   myservo.attach(ServoPin);
}

void loop() {
 SUM=SUM-READINGS[INDEX];
 int x=analogRead(sensorPin);
 READINGS[INDEX]=x;
 SUM = SUM + x;     
 INDEX=(INDEX+1) % WINDOW_SIZE;
 AVERAGED=SUM/WINDOW_SIZE;

 servoAngleint=map(AVERAGED,1,600,1,180);
 myservo.write(servoAngleint);
 
 Serial.println(servoAngleint);
 
}
