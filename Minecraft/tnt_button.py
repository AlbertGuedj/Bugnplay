from  mcpi.minecraft import Minecraft

import RPi.GPIO as gpio
import time

mc = Minecraft.create()


## pin numbers
led1 = 14
button2 = 15
led = led1
button1 = 18
t = 0.1

gpio.setmode(gpio.BCM)
gpio.setup(led1, gpio.OUT)
gpio.setup(button1, gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.setup(button2, gpio.IN, pull_up_down=gpio.PUD_UP)

previous= False

while True:
    current =  gpio.input(button2)
    if not gpio.input(button1):
        x,y,z=mc.player.getPos()
        mc.setBlock(x,y-2,z,46,1)
    if  previous and (not current):
        mc.postToChat("pushed")
        x,y,z = mc.player.getPos()
        mc.player.setPos(x,y+10,z)
    if (not previous and current):
        mc.postToChat("released")
    previous =  current
