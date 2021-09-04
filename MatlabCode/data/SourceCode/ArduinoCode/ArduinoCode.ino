// Include the Servo library 
#include <Servo.h> 
// Declare the Servo pin 
int servoPin = 3; 
// Create a servo object 
Servo Servo1; 
// serial variable
int incomingByte = 0; // for incoming serial data
bool band = false;

// void setup
void setup() { 
   // We need to attach the servo to the used pin number 
   Servo1.attach(servoPin);
   // setup serial comunication
   Serial.begin(9600); // opens serial port, sets data rate to 9600 bps
}

//void loop
void loop() {
  // send data only when you receive data:
  if (Serial.available() > 0) {
    // read the incoming byte:
    incomingByte = Serial.read();
    if (incomingByte=='S'){
       band=!band;
      // say what you got:
      //Serial.print("I received: ");
      //Serial.println(incomingByte, DEC);
      Servo1.write(10); 
      delay(1000);
    }
    if (incomingByte=='V'){
       band=!band;
      // say what you got:
      //Serial.print("I received: ");
      //Serial.println(incomingByte, DEC);
      Servo1.write(160); 
      delay(1000);
    }
    //if(band){
    //  Servo1.write(10); 
    //  delay(1000);
    //}
    //else{
    //  Servo1.write(160); 
    //  delay(1000);
    //}
  }
}
