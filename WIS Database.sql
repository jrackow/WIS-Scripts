/* Erstellen der Datenbank WIS */
DROP DATABASE IF EXISTS wis;
CREATE DATABASE IF NOT EXISTS wis;
USE wis;

CREATE USER 'wishub'@'localhost' IDENTIFIED BY 'Test1.';
GRANT ALL PRIVILEGES ON *.* TO 'wishub'@'localhost';
FLUSH PRIVILEGES;

CREATE TABLE SensorData (
	ID INTEGER AUTO_INCREMENT,
	DateAndTime DATETIME DEFAULT(current_Timestamp),
	Temperature FLOAT NOT NULL,
	Humidity FLOAT NOT NULL,
	Moisture1 DOUBLE NOT NULL,
	Moisture2 DOUBLE,
	PRIMARY KEY (ID)
);

INSERT INTO SensorData (Temperature,Humidity,Moisture1, Moisture2) VALUES (20.0,80.0,350,800);
INSERT INTO SensorData (Temperature,Humidity,Moisture1, Moisture2) VALUES (23.0,40.0,360,302);
INSERT INTO SensorData (Temperature,Humidity,Moisture1, Moisture2) VALUES (21.9,20.0,380,502);
INSERT INTO SensorData (Temperature,Humidity,Moisture1, Moisture2) VALUES (32.098,22.120,300,302);
