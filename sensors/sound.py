import RPi.GPIO as GPIO

SOUND_PIN = 17  # e.g. physical pin 11
sound_listening_enabled = False  # Global flag to enable/disable sound detection

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(SOUND_PIN, GPIO.IN)

def sound_detected():
    """
    Returns True if:
    1. Sound listening is enabled AND
    2. The sensor is outputting HIGH (noise above threshold)
    Otherwise returns False.
    """
    if not sound_listening_enabled:
        return False
    return bool(GPIO.input(SOUND_PIN))

def enable_listening():
    """Enable sound detection"""
    global sound_listening_enabled
    sound_listening_enabled = True

def disable_listening():
    """Disable sound detection"""
    global sound_listening_enabled
    sound_listening_enabled = False

def cleanup():
    GPIO.cleanup()