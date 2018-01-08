#Die Benötigten Bibliotheken importieren
import time
import RPi.GPIO as GPIO

#Den Farben Zahlen (Pins) zuweisen
rot = 3
gelb = 5
gruen = 7

#GPIO einrichten
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.cleanup()

#Die Output-Pins festlegen
GPIO.setup(rot, GPIO.OUT)
GPIO.setup(gelb, GPIO.OUT)
GPIO.setup(gruen, GPIO.OUT)

#Alle Lampen ausschalten
GPIO.output(rot, GPIO.LOW)
GPIO.output(gelb, GPIO.LOW)
GPIO.output(gruen, GPIO.LOW)

print("Ampel aktiv")

#Dauerhaft wiederholen:
while True:
    #Die Ampel auf rot schalten und warten
    GPIO.output(rot, GPIO.HIGH)
    time.sleep(3)

    #Das gelbe Licht dazu schalten und warten
    GPIO.output(gelb, GPIO.HIGH)
    time.sleep(1.5)

    #Rotes und gelbes Licht ausschalten und
    #gruenes Licht einschalten und warten
    GPIO.output(rot, GPIO.LOW)
    GPIO.output(gelb, GPIO.LOW)
    GPIO.output(gruen, GPIO.HIGH)
    time.sleep(3)

    #Das gruene Licht ausschalten und das
    #gelbe Licht einschalten und warten
    GPIO.output(gruen, GPIO.LOW)
    GPIO.output(gelb, GPIO.HIGH)
    time.sleep(2)

    #Das gelbe Licht ausschalten
    GPIO.output(gelb, GPIO.LOW)

    #Oben wieder Anfangen und rot einschalten
