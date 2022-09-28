import serial
import time
import mysql.connector
import sys
print("[Weather-dependent Irrigation System]")
print("[WIS] Script wurde gestartet")
print("")

#Definiert das SQL Statement zum inserten der Daten
insertQuery = "INSERT INTO SensorData (Temperature,Humidity,Moisture1,Moisture2) VALUES (%s, %s, %s, %s)"

# Definiert die Zeit die zwischen den Messungen gewartet wird.
measureTime = 300

# Stellt die Verbindung zum seriellen Anschluss her
s = serial.Serial('/dev/ttyACM0', 9600)

# Wartet bis der Sensor hochgefahren ist
time.sleep(5)

#Methode Measurement
def measurement():
    print("[WIS] Messung wurde gestartet")
    print("[WIS] Stelle Verbindung zur Datenbank her")

    # Stelle Verbindung zur Datenbank her
    try:
        cnx = mysql.connector.connect(user='wishub', password='Test1.',
                              host='0.0.0.0',
                              database='wis')
        cursor = cnx.cursor()
    except mysql.connector.Error as err:
        print("Etwas ist schief gelaufen: {}".format(err))

    print("[WIS] Fordere Messdaten an")

    #Fordere Messdaten an
    s.write('measuring'.encode())

    #Warte auf die Daten
    time.sleep(5)

    #Auslesen der Daten
    response1 = s.readline()
    response2 = s.readline()
    response3 = s.readline()
    response4 = s.readline()

    # Entfernen des \r\n aus dem ankommenden String
    response1 = response1.strip("\r\n".encode())
    response2 = response2.strip("\r\n".encode())
    response3 = response3.strip("\r\n".encode())
    response4 = response4.strip("\r\n".encode())

    print("[WIS] Sensoren wurden gelesen")

    #Schreiben der Daten in eine Datenbank
    queryData = (response1, response2, response3, response4)
    cursor.execute(insertQuery, queryData)

    cnx.commit()
    print("[WIS] Daten wurden in der Datenbank gespeichert.")
    print("")

    #Schließen der Datenbank Connection
    cursor.close()
    cnx.close()

# ProgressBar
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    if iteration == total:
        print()

#Alle 5 Minuten wird eine Messung gestartet. (Das Skript kann durch STRG C beendet werden.)
try:
    while True:
        print("[WIS] Countdown bis zur nächsten Messung (5min)")
        timeCount = 0;
        for x in range(0, measureTime):
            time.sleep(1)
            timeCount = timeCount + 1
            printProgressBar(timeCount, measureTime)
        measurement()
except KeyboardInterrupt:
    print('[WIS] Script wurde beendet')
