

#!/usr/bin/env python

# Copyright (c) 2019-2020, NVIDIA CORPORATION. All rights reserved.
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.


#!/usr/bin/env python3
#-- coding: utf-8 --

import RPi.GPIO as GPIO
import time

output_pins = {
    'JETSON_XAVIER': 18,
    'JETSON_NANO': 33,
    'JETSON_NX': 33,
    'CLARA_AGX_XAVIER': 18,
    'JETSON_TX2_NX': 32,
    'JETSON_ORIN': 18,
}
output_pin = output_pins.get(GPIO.model, None)
if output_pin is None:
    raise Exception('PWM not supported on this board')


#Use pin 12 for PWM signal
pwm_gpio = 33
frequence = 50
#GPIO.setup(pwm_gpio, GPIO.OUT)
#pwm = GPIO.PWM(pwm_gpio, frequence)

#Set function to calculate percent from angle
def angle_to_percent (angle) :
    if angle > 180 or angle < 0 :
        return False

    start = 4
    end = 12.5
    ratio = (end - start)/180 #Calcul ratio from angle to percent

    angle_as_percent = angle * ratio

    return start + angle_as_percent


#GPIO.setmode(GPIO.BOARD) #Use Board numerotation mode
#GPIO.setwarnings(False) #Disable warnings

def main():
    # Pin Setup:
    # Board pin-numbering scheme
    GPIO.setmode(GPIO.BOARD)
    # set pin as an output pin with optional initial state of HIGH
    GPIO.setup(output_pin, GPIO.OUT, initial=GPIO.HIGH)
    pwm = GPIO.PWM(output_pin, 50)
##    val = 25
##    incr = 5
##    pwm.start(val)

    print("PWM running. Press CTRL+C to exit.")
    try:
        while True:
            #Init at 0°
            pwm.start(angle_to_percent(0))
            time.sleep(1)

            #Go at 90°
            pwm.ChangeDutyCycle(angle_to_percent(90))
            time.sleep(1)

            #Finish at 180°
            pwm.ChangeDutyCycle(angle_to_percent(180))
            time.sleep(1)
##            time.sleep(0.25)
##            if val >= 100:
##                incr = -incr
##            if val <= 0:
##                incr = -incr
##            val += incr
##            p.ChangeDutyCycle(val)
    finally:
        pwm.stop()
        GPIO.cleanup()

if __name__ == '__main__':
    main()





