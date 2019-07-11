//www.elegoo.com

#define ENB 5
#define IN1 7
#define IN2 8
#define IN3 9
#define IN4 11
#define ENA 6

void forward()
{
  //go forward
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, HIGH);
}

void backward()
{
  //runing back
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, HIGH);
  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW);
}

void set_speed(int inSpeed)
{

  analogWrite(ENB, inSpeed);
  analogWrite(ENA, inSpeed);
}

void stop_car()
{
  set_speed(0);
}

void setup()
{
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT);
  pinMode(ENA, OUTPUT);
  pinMode(ENB, OUTPUT);
  stop_car();
}

/////////////////////////////////////////////////////////////////////////
//
//  Results
//
/////////////////////////////////////////////////////////////////////////
/*
 We let the car run for one second and measure how much distance did the car move
 The speed is that distance / sec
 
 +-------+---------+
 | Input | Speed   |
 +-------+---------+
 |   31  |  0 in/s |
 |   63  |  0 in/s |
 |  127  | 15 in/s |
 |  255  | 31 in/s |
 +-------+---------+
*/

void loop()
{
  forward();

  for (int carSpeed = 32; carSpeed <= 256; carSpeed = carSpeed * 2)
  {
    // set speed to carspeed
    set_speed(carSpeed - 1);
    // wait for one second
    delay(1000);
    // stop for 15-30 seconds for mesurment and reset
    stop_car();
    delay(30000);
  }
}
