import RPi.GPIO as GPIO 

GPIO.setmode(GPIO.BCM)

leds = [22, 27, 17, 26, 25, 21, 20, 16] 
GPIO.setup(leds, GPIO.OUT, initial=0)

dynamic_range = 3.3
def voltage_to_number(voltage):
    if not (0.0 <= voltage <= dynamic_range):
        print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {dynamic_range:.2f} В)")
        print("Устанавливаем 0.0 В")
        return 0
    return int(voltage / dynamic_range * 255)

def number_to_dac(number):
    return [int(bit) for bit in format(number, 'b').zfill(8)]

try:
    while True:
        try:
            voltage = float(input("Введите напряжение в Вольтах: "))
            number  = voltage_to_number(voltage)
            dac_value = number_to_dac(number)
            for i in range(8):
                GPIO.output(leds[i], dac_value[i])
        except ValueError:
            print("Вы ввели не число. попробуйте еще раз\n")
finally:
    GPIO.output(leds, 0)
    GPIO.cleanup()