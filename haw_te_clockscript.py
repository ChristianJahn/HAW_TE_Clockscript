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
MOND = 26
TASTER = 18

#Richtung der GPIO-Pins festlegen (IN / OUT)
GPIO.setup(GRUEN, GPIO.OUT) #GRUEN
GPIO.setup(GELB, GPIO.OUT) #gelb
GPIO.setup(ROT, GPIO.OUT) #ROT
GPIO.setup(MOND, GPIO.OUT) #MOND
GPIO.setup(TASTER, GPIO.IN) #Taster

def ledtest():
   while True:
	#Status des Tasters einlesen
	tasterStatus = GPIO.input(TASTER)
	
    	if (tasterStatus):
		print("Number of cpu : ", multiprocessing.cpu_count())
		for i in range(1, 10):
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
	
def moonphaseIndicator():
   while True:
	sleep(25)
	for j in range(1,121):
		GPIO.output(MOND, True)
	GPIO.output(MOND, False)


if __name__ == '__main__':
    #Phase 1
    GPIO.output(GRUEN, True)
    GPIO.output(GELB, False)
    GPIO.output(ROT, False)
    GPIO.output(MOND, False)

    thread = multiprocessing.Process(target=modulateSeconds)
    thread.daemon = False
    
    thread2 = multiprocessing.Process(target=ledtest)
    thread2.daemon = False
	
    threadMoon = multiprocessing.Process(target=moonphaseIndicator)
    threadMoon.daemon = False

    thread.start()
    time.sleep(1)
    thread2.start()
    time.sleep(1)
    threadMoon.start()
