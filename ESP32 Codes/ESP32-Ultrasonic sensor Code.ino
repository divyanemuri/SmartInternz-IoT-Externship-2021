int echopin=4;
int trigpin=5;

void setup() {
  // put your setup code here, to run once:
pinMode(echopin,INPUT);
pinMode(trigpin,OUTPUT);
Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
digitalWrite(trigpin,HIGH);
delay(1000);
digitalWrite(trigpin,LOW);
int duration=pulseIn(echopin,HIGH);
int distance=duration*0.0343/2;
Serial.print("the distance is");
Serial.println(distance);
delay(2000);
}
