from machine import Pin, PWM
import utime

#set up leds
r=Pin(11, Pin.OUT)
y=Pin(12, Pin.OUT)
g=Pin(13, Pin.OUT)
b=Pin(14, Pin.OUT)
w=Pin(15, Pin.OUT)


# INITIALIZE HC-SR04 SENSOR
trigger = Pin(3, Pin.OUT)
echo = Pin(2, Pin.IN)
# INITIALIZE VARIABLES #
target_distance = 0.10 

def sensor():
    # turn off trigger, and wait for 2 microseconds
    trigger.low()
    utime.sleep_us(2)
    # turn on trigger, and wait for 5 microseconds
    trigger.high()
    utime.sleep_us(5)
    # turn off trigger
    trigger.low()
    # count time it takes to receive an echo
    while echo.value() == 0:
        signaloff = utime.ticks_us()
    while echo.value() == 1:
        signalon = utime.ticks_us()
    timepassed = signalon - signaloff
    #convert the time to measurements
    #measurement in cm
    #distance = (timepassed * 0.0343) / 2
    #measurement in m
    distance = (timepassed * 0.000343) / 2
    #measurement in feet
      #distance = (timepassed * 1125) / 2
    return distance


# ADD MAIN LOOP TO 'TRY' STATEMENT IN CASE OF ERRORS #
try:
    # CREATE MAIN LOOP #
    while True:
        # GET RESULT FROM SENSOR #
        result = sensor()
        if result < target_distance:
            r.value(1)
            y.value(1)
            g.value(1)
            b.value(1)
            w.value(1)
        elif result < target_distance*2:
            r.value(1)
            y.value(1)
            g.value(1)
            b.value(1)
            w.value(0)
        elif result < target_distance*3:
            r.value(1)
            y.value(1)
            g.value(1)
            b.value(0)
            w.value(0)
        elif result < target_distance*4:
            r.value(1)
            y.value(1)
            g.value(0)
            b.value(0)
            w.value(0)
        elif result < target_distance*5:
            r.value(1)
            y.value(0)
            g.value(0)
            b.value(0)
            w.value(0)
        else:
            r.value(0)
            y.value(0)
            g.value(0)
            b.value(0)
            w.value(0)

        print("Distance: %s m" % (str(result)))
        utime.sleep_ms(100)            
except KeyboardInterrupt:
    pass


