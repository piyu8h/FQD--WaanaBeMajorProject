import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


ultrasonic_trigger = 23
ultrasonic_echo = 24
relay_in1 = 17
relay_in2 = 27
    

GPIO.setup(ultrasonic_trigger, GPIO.OUT)
GPIO.setup(ultrasonic_echo, GPIO.IN)
GPIO.setup(relay_in1, GPIO.OUT)
GPIO.setup(relay_in2, GPIO.OUT)

def get_distance():
    
    GPIO.output(ultrasonic_trigger, True)
    time.sleep(0.00001)
    GPIO.output(ultrasonic_trigger, False)

    
    while GPIO.input(ultrasonic_echo) == 0:
        start_time = time.time()
    while GPIO.input(ultrasonic_echo) == 1:
        end_time = time.time()

    # Calculate distance
    distance = ((end_time - start_time) * 34300) / 2

    return distance

def stop_conveyor():
    GPIO.output(relay_in1, False)

def start_conveyor():
    GPIO.output(relay_in1, True)

def actuate_second_motor():
    GPIO.output(relay_in2, True)
    time.sleep(3)
    GPIO.output(relay_in2, False)

while True:
    distance = get_distance()
    if distance < 10:  

        stop_conveyor()
        a = classify_fruit()  

        if a == 1:  # If fruit is rotten
            actuate_second_motor()
        start_conveyor()
    time.sleep(0.1)
