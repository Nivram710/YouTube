#Alle benötigten Bibliotheken installieren
import RPi.GPIO as GPIO
import time
import random

#Die Pins festlegen
rot = 12
gruen = 32

#GPIO konfigurieren
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(rot, GPIO.OUT)
GPIO.setup(gruen, GPIO.OUT)

GPIO.output(rot, GPIO.LOW)
GPIO.output(gruen, GPIO.LOW)

#Das Passwort festlegen
passwort = "1234"

#Den Nutzer nach dem Passwort fragen
eingabe = input("Passwort: ")

#Überprüfen, ob das Passwort stimmt,
if eingabe == passwort:
  
    #Wenn ja, schreibe Login erfolgreich
    #Lasse die Lampe 3 mal grün blinken
    print("Login erfolgreich!")
    for i in range(3):
        GPIO.output(gruen, GPIO.HIGH)
        time.sleep(0.1 + random.random() / 5)
        GPIO.output(gruen, GPIO.LOW)
        time.sleep(random.uniform(0.1, 0.5))
    
#Wenn nein
else:
    #schreibe Login fehlgeschlagen
    #Lasse die Lampe 3 mal rot blinken
    print("Login fehlgeschlagen!")
    for i in range(3):
        GPIO.output(rot, GPIO.HIGH)
        time.sleep(random.choice([0.5, 1]))
        GPIO.output(rot, GPIO.LOW)
        time.sleep(random.choice([0.5, 1]))
