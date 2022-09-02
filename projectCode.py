from gpiozero import AngularServo, DistanceSensor from guizero import App, Slider
from picamera import PiCamera
from PiAnalog import *
import requests import time

p = PiAnalog()
servo = AngularServo(18, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000)\ servo.angle = 0
clockwise = False
sensor = DistanceSensor(echo=23, trigger=24)
  
EVENT = 'motion_detected'
BASE_URL = 'https://maker.ifttt.com/trigger/' KEY = 'b6RuwC9i0TRlmqghPD42U'
camera = PiCamera()

while True:
  Res_Sensor = p.read_resistance()
  
  while Res_Sensor < 500: #Checks if it is daytime
    if (servo.angle > -90 && clockwise == True):#Rotates Camera clockwise 
      servo.angle -= 0.2
    elif (servo.angle < 90 && clockwise == False): #Rotates Camera counter-clockwise 
      servo.angle += 0.2
    
    if (sevo.angle == -90): 
      clockwise = False #Switches camera direction from clockwise to counter-clockwise
    elif(servo.angle == 90):
      clockwise = True  #Switches camera direction from counter-clockwise to clockwise
      
    inch = (sensor.distance * 100) /2.5 #Checks sensor distance in inches
    
    if (inch < 10): #Checks for movement
      pic = camera.capture('test.jpg')
      url = BASE_URL + EVENT + 'with_key/' + KEY data = {'value1' : pic}
      response = requests.post(url, json=data) #Sends out a url give that activates the ifttt
    Res_Sensor = p.read_resistance()
    
print("It's nightime") 
time.sleep(5)
