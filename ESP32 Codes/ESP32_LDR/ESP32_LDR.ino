void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
int ldrval=analogRead(15);
Serial.print("the LDR value is:");
Serial.println(ldrval);
delay(1000);
}
