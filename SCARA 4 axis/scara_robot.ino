// Define stepper motor connections and steps per revolution:
#define dirPin1 2  // Motor 1
#define stepPin1 3 // Motor 1

#define dirPin2 4  // Motor 2
#define stepPin2 5 // Motor 2

#define dirPin3 6  // Motor 3
#define stepPin3 7 // Motor 3

#define dirPin4 8  // Motor 4
#define stepPin4 9 // Motor 4

#define stepsPerRevolution 1600

void setup() {
  // Declare pins as output:
  pinMode(stepPin1, OUTPUT); // Motor 1
  pinMode(dirPin1, OUTPUT);  // Motor 1
  pinMode(stepPin2, OUTPUT); // Motor 2
  pinMode(dirPin2, OUTPUT);  // Motor 2
  pinMode(stepPin3, OUTPUT); // Motor 3
  pinMode(dirPin3, OUTPUT);  // Motor 3
  pinMode(stepPin4, OUTPUT); // Motor 4
  pinMode(dirPin4, OUTPUT);  // Motor 4
}

void loop() {
  forward(dirPin1, stepPin1);
  backward(dirPin1, stepPin1);
  
  forward(dirPin2, stepPin2);
  backward(dirPin2, stepPin2);
  
  forward(dirPin3, stepPin3);
  backward(dirPin3, stepPin3);
  
  forward(dirPin4, stepPin4);
  backward(dirPin4, stepPin4);
}

void forward(int dirPin, int stepPin) {
  // Set the spinning direction clockwise:
  digitalWrite(dirPin, HIGH);

  // Spin the stepper motor 1 revolution slowly:
  for (int i = 0; i < 4500; i++) {
    // These four lines result in 1 step:
    digitalWrite(stepPin, HIGH);
    delayMicroseconds(500);
    digitalWrite(stepPin, LOW);
    delayMicroseconds(500);
  }
  
  delay(1000);
}

void backward(int dirPin, int stepPin) {
  // Set the spinning direction clockwise:
  digitalWrite(dirPin, LOW);

  // Spin the stepper motor 1 revolution slowly:
  for (int i = 0; i < 4500; i++) {
    // These four lines result in 1 step:
    digitalWrite(stepPin, HIGH);
    delayMicroseconds(500);
    digitalWrite(stepPin, LOW);
    delayMicroseconds(500);
  }
  
  delay(1000);
}
