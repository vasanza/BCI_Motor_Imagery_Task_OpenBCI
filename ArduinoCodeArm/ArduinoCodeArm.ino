//Pulgar: close 0 - open 60
//Dedo Pulgar: close 20 - open 150
//Medio: close 150 - open 0
//Indice: colse 0 - open 120
// Anular & Menique: close 150 - open 10

// Include the Servo library 
#include <Servo.h> 
// Declare the Servo pin 
int AnularMenique = 3;
int Medio = 5;
int Indice =6;
int DedoPulgar =9;
int Pulgar =11;
// Create a servo object 
Servo Servo1;//AnularMenique
Servo Servo2;//Medio
Servo Servo3;//Indice
Servo Servo4;//DedoPulgar
Servo Servo5;//Pulgar
//int angulo=90;
// serial variable
int incomingByte = 0; // for incoming serial data
//bool band = false;

// void setup
void setup() { 
   // We need to attach the servo to the used pin number 
   Servo1.attach(AnularMenique);
   Servo2.attach(Medio);
   Servo3.attach(Indice);
   Servo5.attach(Pulgar);
   Servo4.attach(DedoPulgar);  
   // setup serial comunication
   Serial.begin(9600); // opens serial port, sets data rate to 9600 bps
}

//void loop
void loop() {
  //open all
  Servo1.write(10); 
  delay(300);
  Servo2.write(0); 
  delay(300);
  Servo3.write(120); 
  delay(300);
  Servo4.write(150); 
  delay(300);
  Servo5.write(60); 
  delay(300);
  while(true){
  // send data only when you receive data:
  if (Serial.available() > 0) {
    // read the incoming byte:
    incomingByte = Serial.read();
    //if (incomingByte=='U'){
    //  angulo=angulo+10;
    //}
    //if (incomingByte=='D'){
    //  angulo=angulo-10;
    //}
    //Serial.println(angulo);
    //Servo1.write(angulo);
    //delay(500);
    if (incomingByte=='V'){//open
    //   band=!band;
      //// say what you got:
      ////Serial.print("I received: ");
      ////Serial.println(incomingByte, DEC);
      Servo1.write(10); 
      delay(300);
      Servo2.write(0); 
      delay(300);
      Servo3.write(120); 
      delay(300);
      Servo4.write(150); 
      delay(300);
      Servo5.write(60); 
      delay(300);
    }
    if (incomingByte=='S'){//close
     //  band=!band;
      //// say what you got:
      ////Serial.print("I received: ");
      ////Serial.println(incomingByte, DEC);
        Servo1.write(150); 
        delay(350);
        Servo2.write(150); 
        delay(350);
        Servo3.write(0); 
        delay(350);
        Servo5.write(0); 
        delay(350);
        Servo4.write(20); 
        delay(350);
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
}
