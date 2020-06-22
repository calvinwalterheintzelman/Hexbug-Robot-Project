import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.OUT,initial=False)
GPIO.setup(17,GPIO.OUT,initial=False)
GPIO.setup(27,GPIO.OUT,initial=False)
GPIO.setup(22,GPIO.OUT,initial=False)
HEAD = GPIO.PWM(22,50)
BOT = GPIO.PWM(4,50)
LEFT = GPIO.PWM(17,50)
RIGHT = GPIO.PWM(27,50)
trig = 18
echo = 23
GPIO.setup(trig,GPIO.OUT,initial = GPIO.LOW)
GPIO.setup(echo,GPIO.IN)

HEAD.start(8)
BOT.start(7.5)
LEFT.start(7.5)
RIGHT.start(7.5)
time.sleep(1)

    
    
def cho():  #return distance
    GPIO.output(trig,GPIO.HIGH)
    time.sleep(0.000015)    
    GPIO.output(trig,GPIO.LOW)
    while not GPIO.input(echo):
        timestart = time.time()
    while GPIO.input(echo):
        timeend = time.time()
    return (timeend-timestart)*340/2*100

def forward():
    BOT.ChangeDutyCycle(6.3)
    time.sleep(0.2)
    LEFT.ChangeDutyCycle(5.5)
    time.sleep(0.2)
    BOT.ChangeDutyCycle(8.1)
    time.sleep(0.2)
    RIGHT.ChangeDutyCycle(9.5)
    time.sleep(0.2)
    BOT.ChangeDutyCycle(7.5)
    time.sleep(0.2)
    LEFT.ChangeDutyCycle(7.5)
    time.sleep(0.2)
    RIGHT.ChangeDutyCycle(7.5)
    time.sleep(0.2)
    
    BOT.ChangeDutyCycle(6.3)
    time.sleep(0.2)
    LEFT.ChangeDutyCycle(5.5)
    time.sleep(0.2)
    BOT.ChangeDutyCycle(8.1)
    time.sleep(0.2)
    RIGHT.ChangeDutyCycle(9.5)
    time.sleep(0.2)
    BOT.ChangeDutyCycle(7.5)
    time.sleep(0.2)
    RIGHT.ChangeDutyCycle(7.5)
    time.sleep(0.2)   
    LEFT.ChangeDutyCycle(7.5)
    time.sleep(0.2)
    return
def backward():
    BOT.ChangeDutyCycle(6.3) #mid
    time.sleep(0.2)
    LEFT.ChangeDutyCycle(9.5)
    time.sleep(0.2)
    BOT.ChangeDutyCycle(8.1)
    time.sleep(0.2)
    RIGHT.ChangeDutyCycle(5.5)
    time.sleep(0.2)
    BOT.ChangeDutyCycle(7.5)
    time.sleep(0.2)
    LEFT.ChangeDutyCycle(7.5)
    time.sleep(0.2)
    RIGHT.ChangeDutyCycle(7.5)
    time.sleep(0.2)
    
    BOT.ChangeDutyCycle(6.3)
    time.sleep(0.2)
    LEFT.ChangeDutyCycle(9.5)
    time.sleep(0.2)
    BOT.ChangeDutyCycle(8.1)
    time.sleep(0.2)
    RIGHT.ChangeDutyCycle(5.5)
    time.sleep(0.2)
    BOT.ChangeDutyCycle(7.5)
    time.sleep(0.2)
    RIGHT.ChangeDutyCycle(7.5)
    time.sleep(0.2)   
    LEFT.ChangeDutyCycle(7.5)
    time.sleep(0.2)
    return
def turnright():
    BOT.ChangeDutyCycle(6.3) #mid
    time.sleep(0.25)
    LEFT.ChangeDutyCycle(5.5)
    time.sleep(0.25)
    BOT.ChangeDutyCycle(8.1)
    time.sleep(0.25)
    RIGHT.ChangeDutyCycle(5.5)
    time.sleep(0.25)
    BOT.ChangeDutyCycle(7.5)
    time.sleep(0.25)
    LEFT.ChangeDutyCycle(7.5)
    time.sleep(0.25)
    RIGHT.ChangeDutyCycle(7.5)
    time.sleep(0.25)
    
    BOT.ChangeDutyCycle(6.3)
    time.sleep(0.25)
    LEFT.ChangeDutyCycle(5.5)
    time.sleep(0.25)
    BOT.ChangeDutyCycle(8.1)
    time.sleep(0.25)
    RIGHT.ChangeDutyCycle(5.5)
    time.sleep(0.25)
    BOT.ChangeDutyCycle(7.5)
    time.sleep(0.25)
    RIGHT.ChangeDutyCycle(7.5)
    time.sleep(0.25)   
    LEFT.ChangeDutyCycle(7.5)
    time.sleep(0.25)
    
def turnleft():
    BOT.ChangeDutyCycle(6.3) #mid
    time.sleep(0.3)
    LEFT.ChangeDutyCycle(9.5)
    time.sleep(0.3)
    BOT.ChangeDutyCycle(8.1)
    time.sleep(0.3)
    RIGHT.ChangeDutyCycle(9.5)
    time.sleep(0.3)
    BOT.ChangeDutyCycle(7.5)
    time.sleep(0.3)
    LEFT.ChangeDutyCycle(7.5)
    time.sleep(0.3)
    RIGHT.ChangeDutyCycle(7.5)
    time.sleep(0.3)
    
    BOT.ChangeDutyCycle(6.3)
    time.sleep(0.3)
    LEFT.ChangeDutyCycle(9.5)
    time.sleep(0.3)
    BOT.ChangeDutyCycle(8.1)
    time.sleep(0.3)
    RIGHT.ChangeDutyCycle(9.5)
    time.sleep(0.3)
    BOT.ChangeDutyCycle(7.5)
    time.sleep(0.3)
    RIGHT.ChangeDutyCycle(7.5)
    time.sleep(0.3)   
    LEFT.ChangeDutyCycle(7.5)
    time.sleep(0.3)

    
def turnHead():
    HEAD.ChangeDutyCycle(3.3)
    time.sleep(0.8)
    HEAD.ChangeDutyCycle(13.5)
    time.sleep(0.8)
    HEAD.ChangeDutyCycle(8)
    time.sleep(0.8)
    return

def stop():
    LEFT.ChangeDutyCycle(7.5)
    time.sleep(0.1)
    RIGHT.ChangeDutyCycle(7.5)
    time.sleep(0.1)
    BOT.ChangeDutyCycle(7.5)
    time.sleep(0.1)
while (True):
    if (cho()>13):
        forward()
    
    if (cho()<30):
        turnHead()
        backward()
        
        turnright()
        turnright()
        turnright()
        
            
    


