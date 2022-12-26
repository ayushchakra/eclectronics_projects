int LED_PIN_ONE = 8;
int LED_PIN_TWO = 9;
int LED_PIN_THREE = 10;
int LED_PIN_FOUR = 11;

void setup() {
  // put your setup code here, to run once:
  pinMode(14, OUTPUT);
  digitalWrite(14, HIGH);
  pinMode(15, OUTPUT);
  digitalWrite(15, HIGH);
  pinMode(18, OUTPUT);
  digitalWrite(18, HIGH);
  pinMode(23, OUTPUT);
  digitalWrite(23, HIGH);
  pinMode(LED_PIN_ONE, OUTPUT);
  digitalWrite(LED_PIN_ONE, HIGH);
  pinMode(LED_PIN_TWO, OUTPUT);
  digitalWrite(LED_PIN_TWO, LOW);
  pinMode(LED_PIN_THREE, OUTPUT);
  digitalWrite(LED_PIN_THREE, HIGH);
  pinMode(LED_PIN_FOUR, OUTPUT);
  digitalWrite(LED_PIN_FOUR, LOW);
  Serial.begin();
  Serial1.setRX(1);
  Serial1.setTX(0);
  Serial1.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(LED_PIN_ONE, !digitalRead(LED_PIN_ONE));
  digitalWrite(LED_PIN_TWO, !digitalRead(LED_PIN_TWO));
  digitalWrite(LED_PIN_THREE, !digitalRead(LED_PIN_THREE));
  digitalWrite(LED_PIN_FOUR, !digitalRead(LED_PIN_FOUR));
  delay(500);
  Serial.println(analogRead(A0) + 10000);
  Serial.println(analogRead(A1) + 20000);
  Serial.println(analogRead(A2) + 30000);
  Serial.println(analogRead(A3) + 40000);
  // Serial1.println('4');
}
