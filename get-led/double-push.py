import RPi.GPIO as GPIO # подкл рп и иное название
import time # импорт библиотеки времени

GPIO.setmode(GPIO.BCM) # подключаем бсм

leds = [16, 12, 25, 17, 27, 23, 22, 24] #подкл пины светодиодов
GPIO.setup(leds, GPIO.OUT, initial=0) # Настраиваем все GPIO-пины в списке на выход

up_button = 9    # Пин для кнопки "вверх"
down_button = 10  # Пин для кнопки "вниз"
GPIO.setup(up_button, GPIO.IN) #цифровой вход на пин
GPIO.setup(down_button, GPIO.IN) #цифровой вход на пин

def dec2bin(value):# Функция для преобразования числа в двоичное представление
    return [int(element) for element in bin(value)[2:].zfill(8)]# Преобразуем строку в список целых чисел (битов)

num = 0 # Создаем переменную для хранения текущего числа
sleep_time = 0.2 # Время паузы после нажатия кнопки

while True:

    if GPIO.input(down_button) and GPIO.input(up_button):# обработка двух кнопок одновременно
        num = 255

        binary = dec2bin(num)
        print(num, binary)
        GPIO.output(leds, binary)
        time.sleep(sleep_time)
   
    elif GPIO.input(up_button): # Обработка кнопки "вверх
        num += 1

        if num > 255:
            num = 255
        
        binary = dec2bin(num)
        print(num, binary)
        GPIO.output(leds, binary)
        time.sleep(sleep_time)

    elif GPIO.input(down_button):# Обработка кнопки "вниз"
        num -= 1

        if num < 0:
            num = 0
        
        binary = dec2bin(num)
        print(num, binary)
        GPIO.output(leds, binary)
        time.sleep(sleep_time)

