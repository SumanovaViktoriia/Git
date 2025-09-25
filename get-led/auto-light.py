import RPi.GPIO as GPIO #подкл рп и называем короче
import time #импортируем модуль времени
GPIO.setmode(GPIO.BCM) #настраиваем режим бсм и работу по пинам
led = 26 #обозначаем пин светодиода
GPIO.setup(led, GPIO.OUT)#включаем цифровой вход для светодиода
svetodiod = 6 #пин фототранзистора
GPIO.setup(svetodiod, GPIO.IN)#включаем цифровой выход для фототранзистора
period = 1.0 #настраиваем временной период
while True:
    photo_state = GPIO.input(svetodiod) #считываем состояние светодиода
    GPIO.output(led, not photo_state) #меняем состояние светодиода на инвертирвоанное
    time.sleep(period) #время перерыва
