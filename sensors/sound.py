import RPi.GPIO as GPIO

SOUND_PIN = 17  # e.g. physical pin 11

GPIO.setmode(GPIO.BCM)
GPIO.setup(SOUND_PIN, GPIO.IN)

def sound_detected():
    """
    Returns True if the sensor is outputting HIGH (noise above threshold),
    or False if it's LOW (quiet).
    """
    return bool(GPIO.input(SOUND_PIN))

def cleanup():
    GPIO.cleanup()