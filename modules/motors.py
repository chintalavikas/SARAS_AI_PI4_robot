from gpiozero import Motor
from time import sleep

motor = Motor(forward=27, backward=22)

motor.forward()
sleep(2)

motor.backward()
sleep(2)

motor.stop()