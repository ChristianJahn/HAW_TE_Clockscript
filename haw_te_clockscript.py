#bliotheken einbinden
import RPi.GPIO as GPIO
import time

#GPIO Modus (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

#Warnungen ausschalten
GPIO.setwarnings(False)

#GPIO Pin Belegung
GRUEN = 2
GELB = 14
ROT = 15
TASTER = 18

#Richtung der GPIO-Pins festlegen (IN / OUT)
GPIO.setup(GRUEN, GPIO.OUT) #GRUEN
GPIO.setup(GELB, GPIO.OUT) #gelb
GPIO.setup(ROT, GPIO.OUT) #ROT
GPIO.setup(TASTER, GPIO.IN) #Taster

#Umschaltung definieren
def umschalten():
    #Phase 2
    GPIO.output(GRUEN, True)
    GPIO.output(GELB, True)
    GPIO.output(ROT, False)
    time.sleep(2)
    #Phase 3
    GPIO.output(ROT, True)
    GPIO.output(GRUEN, False)
    GPIO.output(GELB, False)
    time.sleep(4)
    #Phase 4
    GPIO.output(GELB, True)
    GPIO.output(ROT, False)
    time.sleep(3)
    #zurueck zu Phase 1
    GPIO.output(GRUEN, True)
    GPIO.output(GELB, False)

    
def ledtest()
for i in range(1, 5):
	GPIO.output(GRUEN, True)
    GPIO.output(GELB, True)
    GPIO.output(ROT, True)
    time.sleep(1)
    print(time.ctime)
    
#Endlosschleife
while True:
    #Phase 1
    GPIO.output(GRUEN, True)
    GPIO.output(GELB, False)
    GPIO.output(ROT, False)
    
    

    #Status des Tasters einlesen
    tasterStatus = GPIO.input(TASTER)
    if (tasterStatus):
        ledtest()
