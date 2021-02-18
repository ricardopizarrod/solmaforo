
import RPi.GPIO as GPIO 
import time 
#Establecemos que vamos a trabjar en modo BCM 
GPIO.setmode(GPIO.BCM)

laser = 14
 
#configuramos el pin GPIO como salida
GPIO.setup(laser, GPIO.OUT)
n=0
#Ingresamos a un lazo infinito
while n<6:
# -------- LAZO INFINITO -------- 
  GPIO.output(laser, GPIO.HIGH)

  time.sleep(1)
  
  GPIO.output(laser, GPIO.LOW)
  
  time.sleep(1)
  
  GPIO.output(laser, GPIO.HIGH)

  time.sleep(1)
  
  GPIO.output(laser, GPIO.LOW)
  
  time.sleep(2)
  
  print ("LAZO INFINITO")
  n=n+1

#--------------------------------
print ("SALIENDO DEL LAZO LOOP")
time.sleep(1)
GPIO.cleanup()  #devuelve los pines a su estado inicial
