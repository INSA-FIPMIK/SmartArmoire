import Jetson.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)


# (where channel is based on the pin numbering mode discussed above)
GPIO.setup(channel, GPIO.IN)

#GPIO.setup(channel, GPIO.OUT, initial = GPIO.HIGH)

def callback_fn(channel):
    print("Evenement en cours %s" % channel)
    

# set rising edge detection on the channel
GPIO.add_event_detect(channel, GPIO.RISING, callback=callback_fn, bouncetime=200)


#Pour desactiver les event
#GPIO.remove_event_detect(channel)


#if GPIO.event_detected(channel):
#    print("eveneement detecte")



#fin du programme
GPIO.cleanup()

