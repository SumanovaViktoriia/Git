import pwm_dac as pwm
import signal_generator as sg
import time

amplitude = 3.2
signal_frequency = 10
sampling_frequency = 1000

dac = None

try:

    dac = pwm.PWM_DAC(gpio_pin=12, 
                      frequency=500,       
                      dynamic_range=3.29,    
                      verbose=False)
    

    print(f"Амплитуда: {amplitude} В")
    print(f"Частота сигнала: {signal_frequency} Гц")
    print(f"Частота дискретизации: {sampling_frequency} Гц")
    print(f"Частота ШИМ: 500 Гц")
    print(f"Динамический диапазон: 3.29 В")

    
    start_time = time.time()
    point_count = 0
    

    while True:

        current_time = point_count / sampling_frequency
        

        normalized_amplitude = sg.get_sin_wave_amplitude(signal_frequency, current_time)

        voltage = min(normalized_amplitude * amplitude, 3.29)

        dac.set_voltage(voltage)

        point_count += 1

        sg.wait_for_sampling_period(sampling_frequency)
    
finally:
    if dac is not None:
        dac.deinit()
