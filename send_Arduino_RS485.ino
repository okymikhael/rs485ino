#include <SoftwareSerial.h>

int ldr;
int EN = 2;
int intensitas;

SoftwareSerial mySerial(6,7);  //rx, tx

void setup() 
{
 pinMode(EN, OUTPUT);
 Serial.begin (9600);
 mySerial.begin(9600);
 digitalWrite(EN,LOW);

}//--(end setup )---

void loop()    
{
 digitalWrite(EN, HIGH); // enable send
 delay(5);
 // Send Data
 ldr = analogRead(A0);
 //kalibrasi sesuai luxmeter
 intensitas = ((pow(ldr,-1.71))*(pow(10,8.14)));
 Serial.print("$01#");
 Serial.print(intensitas);
 Serial.print("\n");
 mySerial.print("$01#");
 mySerial.print(intensitas);
 mySerial.print("\n");
 delay(1000);
}
