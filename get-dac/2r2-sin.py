import r2r_dac as r2r
import signal_generator as sg
import time

dac = None

amplitude = 3.2
signal_frequency = 10
sampling_frequency = 1000

try:

    dac = r2r.R2R_DAC(gpio_bits=[16, 20, 21, 25, 26, 17, 27, 22], 
                      dynamic_range=3.18, 
                      verbose=False)

    print(f"Амплитуда: {amplitude} В")
    print(f"Частота сигнала: {signal_frequency} Гц")
    print(f"Частота дискретизации: {sampling_frequency} Гц")

    start_time = time.time()

    point_count = 0

    while True:

        current_time = point_count / sampling_frequency
        

        normalized_amplitude = sg.get_sin_wave_amplitude(signal_frequency, current_time)
        

        voltage = normalized_amplitude * amplitude
        

        dac.set_voltage(voltage)
        

        point_count += 1
        

        sg.wait_for_sampling_period(sampling_frequency)

finally:
    if dac is not None:
        dac.deinit()
