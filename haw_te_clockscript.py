#Bibliotheken einbinden
import RPi.GPIO as GPIO
import time

#GPIO Modus (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

#Warnungen ausschalten
GPIO.setwarnings(False)

#GPIO Pin Belegung
ROT = 2
GELB = 14
GRUEN = 15
TASTER = 7

#Richtung der GPIO-Pins festlegen (IN / OUT)
GPIO.setup(ROT, GPIO.OUT) #rot
GPIO.setup(GELB, GPIO.OUT) #gelb
GPIO.setup(GRUEN, GPIO.OUT) #gruen
GPIO.setup(TASTER, GPIO.IN) #Taster

#Umschaltung definieren
def umschalten():
    #Phase 2
    GPIO.output(ROT, True)
    GPIO.output(GELB, True)
    GPIO.output(GRUEN, False)
    time.sleep(2)
    #Phase 3
    GPIO.output(GRUEN, True)
    GPIO.output(ROT, False)
    GPIO.output(GELB, False)
    time.sleep(15)
    #Phase 4
    GPIO.output(GELB, True)
    GPIO.output(GRUEN, False)
    time.sleep(3)
    #zurueck zu Phase 1
    GPIO.output(ROT, True)
    GPIO.output(GELB, False)

#Endlosschleife
while True:
    #Phase 1
    GPIO.output(ROT, True)
    GPIO.output(GELB, False)
    GPIO.output(GRUEN, False)
    
    #Status des Tasters einlesen
    tasterStatus = GPIO.input(TASTER)
    if (tasterStatus):
        umschalten()
