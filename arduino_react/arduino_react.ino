long input1;
long input2;
long input3;
long input4;
int inputPin1 = A0;
int inputPin2 = A1;
int inputPin3 = A2;
int inputPin4 = A3;
float val1;
float val2;
float val3;
float val4;
int inByte = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(inputPin1, INPUT);
  pinMode(inputPin2, INPUT);
  pinMode(inputPin3, INPUT);
  pinMode(inputPin4, INPUT);
}

void loop() {
  
  if (Serial.available() > 0)
  {
    inByte = Serial.read();
      
    input1 = 0;
    input2 = 0;
    input3 = 0;
    input4 = 0;
    
    for (int i=0; i < 1000; i++) {
      input1 = input1 + analogRead(inputPin1);
      input2 = input2 + analogRead(inputPin2);
      input3 = input3 + analogRead(inputPin3);
      input4 = input4 + analogRead(inputPin4);
    }
  
    val1 = (float) input1 / 1000.0;
    val2 = (float) input2 / 1000.0;
    val3 = (float) input3 / 1000.0;
    val4 = (float) input4 / 1000.0;
    
    Serial.print(val1);
    Serial.print(",");
    Serial.print(val2);
    Serial.print(",");
    Serial.print(val3);
    Serial.print(",");
    Serial.println(val4);
  }

  delay(1);
}
