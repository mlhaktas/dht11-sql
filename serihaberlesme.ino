#include <dht11.h>
int girdi = 0;
dht11 DHT11;

void setup()
{
  Serial.begin(9600);

}

void loop() {
  int chk = DHT11.read(9);
  if (Serial.available() > 0) {
    int chk = DHT11.read(9);
    girdi = Serial.read();
    if (girdi == 110){
      Serial.println((float)DHT11.humidity, 2);
    }
    if (girdi == 115){
      Serial.println((float)DHT11.temperature, 2); 
    }
  }
}
