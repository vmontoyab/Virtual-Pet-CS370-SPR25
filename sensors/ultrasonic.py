import RPi.GPIO as GPIO
import time

TRIG_PIN = 23  # Physical pin 16
ECHO_PIN = 24  # Physical pin 18
TIMEOUT = 0.02  # 20ms
SPEED_OF_SOUND = 0.034  # cm/µs
MAX_VALID_DISTANCE = 200  # Maximum reasonable distance in cm
READING_HISTORY_SIZE = 3  # Number of previous readings to store

# Store recent readings to filter out anomalies
distance_history = []

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(TRIG_PIN, GPIO.OUT)
    GPIO.setup(ECHO_PIN, GPIO.IN)
    # Initialize with empty history
    global distance_history
    distance_history = []

def read_distance_raw():
    """Read raw distance from the ultrasonic sensor"""
    # Ensure TRIG is LOW briefly
    GPIO.output(TRIG_PIN, False)
    time.sleep(0.00005)  # 50 µs

    # Send 10µs pulse
    GPIO.output(TRIG_PIN, True)
    time.sleep(0.00001)
    GPIO.output(TRIG_PIN, False)

    # Wait for ECHO to go HIGH
    pulse_start = None
    start_wait = time.time()
    while GPIO.input(ECHO_PIN) == 0:
        if (time.time() - start_wait) > TIMEOUT:
            return None
        pulse_start = time.time()

    # Wait for ECHO to go LOW
    pulse_end = None
    start_wait = time.time()
    while GPIO.input(ECHO_PIN) == 1:
        if (time.time() - start_wait) > TIMEOUT:
            return None
        pulse_end = time.time()

    if pulse_start is None or pulse_end is None:
        return None

    # Convert from seconds to microseconds
    pulse_duration_us = (pulse_end - pulse_start) * 1_000_000
    distance_cm = (pulse_duration_us * SPEED_OF_SOUND) / 2.0
    
    # Filter out unreasonable values
    if distance_cm > MAX_VALID_DISTANCE or distance_cm < 0:
        return None
        
    return round(distance_cm, 2)

def read_distance():
    """
    Return the filtered distance measurement.
    Uses median filtering to remove outliers.
    Returns None if no valid reading available.
    """
    global distance_history
    
    # Take a new reading
    new_reading = read_distance_raw()
    
    # If invalid reading, try once more
    if new_reading is None:
        time.sleep(0.01)  # Short delay
        new_reading = read_distance_raw()
    
    # If still invalid, use previous reading if available
    if new_reading is None:
        if distance_history:
            return distance_history[-1]
        return None
    
    # Add to history and keep limited size
    distance_history.append(new_reading)
    if len(distance_history) > READING_HISTORY_SIZE:
        distance_history.pop(0)
    
    # Return median of recent readings for stability
    sorted_readings = sorted(distance_history)
    median_index = len(sorted_readings) // 2
    return sorted_readings[median_index]

def cleanup():
    GPIO.cleanup()
