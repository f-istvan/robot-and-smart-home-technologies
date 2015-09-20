#!/usr/bin/python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD) ## Use BOARD pin numbering
GPIO.setup(7, GPIO.OUT) ## Setup GPIO pin 7 to OUT

def blink(num_of_blinks, speed):
  for i in range(0, num_of_blinks):
    GPIO.output(7, True) ## Turn on GPIO pin 7
    time.sleep(speed)
    GPIO.output(7, False) ## Switch off GPIO pin 7
    time.sleep(speed)
  GPIO.cleanup()

def main():
  num_of_blinks = raw_input("Enter the number of blinks: ")
  speed = raw_input("Enter the length of each blink in seconds (e.g.: 0.5) : ")
  blink(int(num_of_blinks), float(speed))

main()
