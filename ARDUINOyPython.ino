int s = 0;
void setup() {
  Serial.begin(9600);
  pinMode(A2, INPUT);

}

void loop() {
  if (Serial.read() == '1') {
    delay(1000);
    for (int i = 0; i < 500; i++) {
      s = analogRead(A2);
      delay(500);
      Serial.println(s);

    }
  }
}
