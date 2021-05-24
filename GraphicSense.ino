/*
             AUTOR: Santiago Escoto Rojas
        Este es el programa que tiene que leer
  tu Arduino Uno para que el programa de GraphicSense
     pueda funcionar, habrá una imagen adjunta para
    que se guíe en ese diagrama al conectar su sensor
*/
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
