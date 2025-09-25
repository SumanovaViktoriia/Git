import RPi.GPIO as GPIO #подкл рп и иное название
import time #спорт библтотеки времени
GPIO.setmode(GPIO.BCM) #настройка бсм и пинов
leds = [24, 22, 23, 27, 17, 25, 12, 16] #переменная с подключенными пинами светодиодов
GPIO.setup(leds, GPIO.OUT) #настраиваем на выход (управление сигналом)
GPIO.output(leds, 0) #асим все светодиоды в блоке
light_time = 0.2 #переменная которая хранит вермя свечения одного светодиода
for led in leds:
    GPIO.output(led, 1) #вкл один светодиод
    time.sleep(light_time) #время свечения
    GPIO.output(led, 0) #выкл
for led in reversed(leds): #циул по прохождению в обратную сторону
    GPIO.output(led, 1) #вкл один светодиод
    time.sleep(light_time)#время свечения
    GPIO.output(led, 0)#выкл
