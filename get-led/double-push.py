import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
leds = [16, 12, 25, 17, 27, 23, 22, 24]
for pin in leds:
    GPIO.setup(pin, GPIO.OUT)
for pin in leds:
    GPIO.output(pin, GPIO.LOW)
up_button = 5    # Кнопка "вверх"
down_button = 6  # Кнопка "вниз"
GPIO.setup(up_button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(down_button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
num = 0
MAX_VALUE = 255  # Максимальное значение для 8 бит
sleep_time = 0.2# Время паузы после нажатия кнопки
def dec2bin(n):# Функция для преобразования числа в двоичное представление
    bin_str = bin(n)[2:].zfill(8)
    return [int(bit) for bit in bin_str]
def display_binary(n):# Функция для отображения числа на светодиодах
    binary = dec2bin(n)
    for i in range(8):
        GPIO.output(leds[i], GPIO.HIGH if binary[i] == 1 else GPIO.LOW)

try:
        num = MAX_VALUE# Устанавливаем максимальное значение при запуске
    display_binary(num)
    print(f"Установлено максимальное значение: {num}, двоичное: {dec2bin(num)}")
        while True:
        if GPIO.input(up_button):# Обработка кнопки "вверх"
            if num < MAX_VALUE:
                num += 1
            else:
                num = 0  # Сброс к 0 при достижении максимума
            print(f"Число: {num}, Двоичное: {dec2bin(num)}")
            display_binary(num)
            time.sleep(sleep_time)
        if GPIO.input(down_button):# Обработка кнопки "вниз"
            if num > 0:
                num -= 1
            else:
                num = MAX_VALUE  # Установка максимума при достижении 0
            print(f"Число: {num}, Двоичное: {dec2bin(num)}")
            display_binary(num)
            time.sleep(sleep_time)
        
        time.sleep(0.01)
