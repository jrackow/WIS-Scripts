#include "DHT.h"

// Konfiguration des DHT11 Sensor
#define DHTPIN 3  
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE); 

// Variablen Pumpe
int IN1 = 2;
int Pin1 = A0;
float value1 = 0;


void setup() {
  //Serielle Verbindung starten
  Serial.begin(9600); 

  // Starten des DHT11 Sensors
  dht.begin();
}

void loop() {
  //Auslesen eines Command
  String command = Serial.readString();

  // Eine Messung wird nur auf Command ausgeführt.
  if(command == "measuring"){
    //Zwei Sekunden Vorlaufzeit bis zur Messung (der Sensor ist etwas träge)
    delay(2000); 
  
    // Auslesen der Sensoren
    float Luftfeuchtigkeit = dht.readHumidity();
    float Temperatur = dht.readTemperature();
    int moistureSensor1 = analogRead(0);
    int moistureSensor2 = analogRead(1);
    
    delay(2000);

    // Senden der Daten in Richtung RaspberryPi, über die serielle Konsole
    Serial.println(Temperatur);

    Serial.println(Luftfeuchtigkeit);
    
    Serial.println(moistureSensor1);

    Serial.println(moistureSensor2);

    //Konfiguration der Pumpe
    pinMode(IN1, OUTPUT);
    pinMode(Pin1, INPUT);
    digitalWrite(IN1, HIGH);
    delay(500);

    // Wenn der Mittelwert zwischen den beiden Bodenfeuchtigkeitssensoren unter 500 ist, soll eine Bewässerung stattfinden.
    if((moistureSensor1 + moistureSensor2) / 2 > 500)
    {    
      digitalWrite(IN1, LOW);
      delay(1500);
    }
    digitalWrite(IN1, HIGH);
  }
}
