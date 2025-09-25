import RPi.GPIO as GPIO #подкл рп и иное название
import time #импорт библиотеки времени
GPIO.setmode(GPIO.BCM) #подключаем бсм
leds = [16, 12, 25, 17, 27, 23, 22, 24] #подкл пины светодиодов
for pin in leds:
    GPIO.setup(pin, GPIO.OUT) # Настраиваем все GPIO-пины в списке на выход
for pin in leds:
    GPIO.output(pin, GPIO.LOW) # Гасим все светодиоды
up_button = 5    # Пин для кнопки "вверх"
down_button = 6  # Пин для кнопки "вниз"

GPIO.setup(up_button, GPIO.IN) #цифровой вход на пин
GPIO.setup(down_button, GPIO.IN) #цифровой вход на пин
num = 0 # Создаем переменную для хранения текущего числа
sleep_time = 0.2 # Время паузы после нажатия кнопки
def dec2bin(n):# Функция для преобразования числа в двоичное представление
    bin_str = bin(n)[2:].zfill(8)# Преобразуем число в двоичную строку
    return [int(bit) for bit in bin_str]# Преобразуем строку в список целых чисел (битов)
while True:
        if GPIO.input(up_button): # Обработка кнопки "вверх"
        if num < 255:
            num += 1
        print(num, dec2bin(num))
        time.sleep(sleep_time)
        if GPIO.input(down_button):# Обработка кнопки "вниз"
            if num > 0:  # Защита от отрицательных чисел
                num -= 1
            print(num, dec2bin(num))
            time.sleep(sleep_time)
        binary = dec2bin(num) # Выводим двоичное представление числа на светодиоды
        for i in range(8):
            # Старший бит (binary[0]) выводится на первый светодиод (leds[0])
            GPIO.output(leds[i], GPIO.HIGH if binary[i] == 1 else GPIO.LOW)
