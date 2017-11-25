float pHX;
float pHS = 7;
//float offset;
float Es = 0;
float F = 9.6485309e4;
float R = 8.314510;
float T = 23.6 + 273.15;
//int acidPump = 9;
//int basePump = 10;

void setup() {
  Serial.begin(9600);
//  pinMode(acidPump, OUTPUT);
//  pinMode(basePump, OUTPUT);
}

void loop() {
  float sensorValue = analogRead(A4);
  float ExMax = -((3-7)*(R*T*log(10)))/F + Es;
//  float Ex = map(sensorValue, 0.0, 1023, 0.0, ExMax);
  float Ex = sensorValue*(ExMax/1023);;
//  map(sensorValue, 0, maxSensorReading, 0, maxVpH); maxSensorReading at maxVpH, maxVpH depends on temp
  pHX = pHS + (((Es-Ex)*F)/(R*T*log(10)));
  Serial.println(pHX);
  Serial.println(Ex);
  Serial.println(sensorValue);

//  if(pHX > 5.5) {
//    digitalWrite(acidPump, HIGH);
//  }
//  else if(pHX < 4.5){
//    digitalWrite(basePump, HIGH);
//  }

//  delay(2000);
//  analogWrite(acidPump, LOW);
//  analogWrite(basePump, LOW);
}

