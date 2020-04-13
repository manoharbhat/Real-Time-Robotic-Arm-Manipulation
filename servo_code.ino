#include <Servo.h>
Servo thumb;
Servo index;
Servo middle;
Servo ring;
Servo pinky;
void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
thumb.attach(13);
index.attach(12);
middle.attach(11);
ring.attach(10);
pinky.attach(9);
thumb.write(180);
index.write(180);
middle.write(180);
ring.write(180);
pinky.write(180);
}
//180-finger up
//0-finger down
void loop() {
  // put your main code here, to run repeatedly:
if(Serial.available()>=0){
  if((char)Serial.read()=='0')//for showing zero
  {
    thumb.write(0);
    delay(100);
    index.write(0);
    delay(100);
    middle.write(0);
    delay(100);
    ring.write(0);
    delay(100);
    pinky.write(0);
    delay(100);
  }}
if(Serial.available()>=0){
 if((char)Serial.read()=='1')//for showing one
  {
    thumb.write(0);
    index.write(180);
    middle.write(0);
    ring.write(0);
    pinky.write(0);
    delay(900);
  }}
if(Serial.available()>=0){
 if((char)Serial.read()=='2')//for showing two
  {
    thumb.write(0);
    index.write(180);
    middle.write(180);
    ring.write(0);
    pinky.write(0);
    delay(900);
  }}
if(Serial.available()>=0){
 if((char)Serial.read()=='3')//for showing three
  {
    thumb.write(0);
    index.write(180);
    middle.write(180);
    ring.write(180);
    pinky.write(0);
    delay(900);
  }}
if(Serial.available()>=0){
  if((char)Serial.read()=='4')//for showing four
  {
    thumb.write(0);
    index.write(180);
    middle.write(180);
    ring.write(180);
    pinky.write(180);
  }}
if(Serial.available()>=0){
  if((char)Serial.read()=='5')//for showing five
  {
    thumb.write(180);
    index.write(180);
    middle.write(180);
    ring.write(180);
    pinky.write(180);
    delay(900);
  }}
if(Serial.available()>=0){
  if((char)Serial.read()=='6')//for showing thumbs up

  {
    thumb.write(180);
    index.write(0);
    middle.write(0);
    ring.write(0);
    pinky.write(0);
    delay(900);
  }}
if(Serial.available()>=0){
  if((char)Serial.read()=='7')//for showing OK sign
  {
    thumb.write(0);
    index.write(0);
    middle.write(180);
    ring.write(180);
    pinky.write(180);
    delay(900);
  }
  }
}
