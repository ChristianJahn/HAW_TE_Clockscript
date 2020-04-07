#bliotheken einbinden
import RPi.GPIO as GPIO
import time
import multiprocessing

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

    

def ledtest():
   while True:
	#Status des Tasters einlesen
	tasterStatus = GPIO.input(TASTER)
	
    	if (tasterStatus):
   	print("Number of cpu : ", multiprocessing.cpu_count())
   	for i in range(1, 55):
		GPIO.output(GRUEN, False)
		GPIO.output(GELB, True)
		GPIO.output(ROT, True)
		time.sleep(0.5)
		GPIO.output(GRUEN, True)
		GPIO.output(GELB, False)
		GPIO.output(ROT, False)
		time.sleep(0.5)

def modulateSeconds():
   while True:
      GPIO.output(GRUEN, False)
      time.sleep(0.5)
      GPIO.output(GRUEN, True)
      time.sleep(0.5)


if __name__ == '__main__':
    #Phase 1
    GPIO.output(GRUEN, True)
    GPIO.output(GELB, False)
    GPIO.output(ROT, False)


    #Status des Tasters einlesen
    #tasterStatus = GPIO.input(TASTER)
    #if (tasterStatus):
        #ledtest()

    thread = multiprocessing.Process(target=modulateSeconds)
    thread.daemon = True
    
    thread2 = multiprocessing.Process(target=ledtest)
    thread2.daemon = Frue

    thread.start()
    time.sleep(1)
    thread2.start()
