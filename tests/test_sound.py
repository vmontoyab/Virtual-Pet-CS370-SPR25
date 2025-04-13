import RPi.GPIO as GPIO
import time

SOUND_PIN = 17  # e.g. physical pin 11

def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(SOUND_PIN, GPIO.IN)

    try:
        while True:
            if GPIO.input(SOUND_PIN) == GPIO.HIGH:
                print("Sound detected!")
            else:
                print("No sound.")
            time.sleep(0.5)
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    main()
