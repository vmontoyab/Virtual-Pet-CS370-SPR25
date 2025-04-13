import RPi.GPIO as GPIO
import time

TRIG_PIN = 23
ECHO_PIN = 24
TIMEOUT  = 0.02  # 20ms
SPEED_OF_SOUND = 0.034  # cm/µs

def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(TRIG_PIN, GPIO.OUT)
    GPIO.setup(ECHO_PIN, GPIO.IN)

    try:
        while True:
            distance = read_distance()
            if distance is None:
                print("No echo received (timeout).")
            else:
                print(f"Distance: {distance:.2f} cm")
            time.sleep(0.5)
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()

def read_distance():
    # Ensure TRIG is LOW briefly
    GPIO.output(TRIG_PIN, False)
    time.sleep(0.00005)  # 50 µs

    # Send a 10µs pulse
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
    # Distance in cm
    distance_cm = (pulse_duration_us * SPEED_OF_SOUND) / 2.0
    return round(distance_cm, 2)

if __name__ == "__main__":
    main()