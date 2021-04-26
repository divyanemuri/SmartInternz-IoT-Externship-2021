void setup() {
  // put your setup code here, to run once:
pinMode(2,OUTPUT);
pinMode(4,INPUT);
Serial.begin(9600);
}

void loop() {
int buttonval=digitalRead(4);
if(buttonval==1){
digitalWrite(2,HIGH);
Serial.println("Led is on");
delay(1000);
}
else{
digitalWrite(2,LOW);
Serial.println("Led is off");
delay(1000);
}
}
