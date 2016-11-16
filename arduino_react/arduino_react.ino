int inputPin1 = A0;
int inputPin2 = A1;
int inputPin3 = A2;
int inputPin4 = A3;
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
    
    int input1 = analogRead(inputPin1);
    int input2 = analogRead(inputPin2);
    int input3 = analogRead(inputPin3);
    int input4 = analogRead(inputPin4);
    
    Serial.print(input1);
    Serial.print(",");
    Serial.print(input2);
    Serial.print(",");
    Serial.print(input3);
    Serial.print(",");
    Serial.println(input4);
  }
}
