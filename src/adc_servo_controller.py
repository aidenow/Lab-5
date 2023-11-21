from hal import hal_adc as adc
from hal import hal_servo as servo

def map_adc_to_servo(adc_value):
    # Map ADC range (0 to 1023) to servo range (0 to 180 degrees)
    return int((adc_value / 1023.0) * 180)

def main():
    adc.init()
    servo.init()

    try:
        while True:
            adc_value = adc.get_adc_value(1)
            servo_position = map_adc_to_servo(adc_value)
            servo.set_servo_position(servo_position)

    except KeyboardInterrupt:
        # Clean up GPIO on Ctrl+C exit
        servo.PWM.stop()
        GPIO.cleanup()

if __name__ == "__main__":
    main()
