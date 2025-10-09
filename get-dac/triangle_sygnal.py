import mcp4725_driver
import time
import sys

def generate_triangle_wave(amplitude, frequency, time_val):

    period = 1.0 / frequency
    phase = (time_val % period) / period
    
    if phase < 0.25:
        voltage = amplitude * (phase / 0.25)
    elif phase < 0.75:
        voltage = amplitude * (1 - (phase - 0.25) / 0.5)
    else:
        voltage = amplitude * ((phase - 0.75) / 0.25)
    
    return voltage

def wait_for_sampling_period(sampling_frequency):
    sampling_period = 1.0 / sampling_frequency 
    time.sleep(sampling_period)

def main():

    DEFAULT_AMPLITUDE = 2.5
    DEFAULT_FREQUENCY = 2
    DEFAULT_SAMPLING = 500
    DYNAMIC_RANGE = 5.0
    

    if len(sys.argv) >= 4:
        try:
            amplitude = float(sys.argv[1])
            frequency = float(sys.argv[2])
            sampling = float(sys.argv[3])
        except ValueError:
            print("Ошибка: параметры должны быть числами")
            sys.exit(1)
    else:
        amplitude = DEFAULT_AMPLITUDE
        frequency = DEFAULT_FREQUENCY
        sampling = DEFAULT_SAMPLING
        print("Используются параметры по умолчанию")
        print("Для указания своих параметров: python script.py <амплитуда> <частота> <дискретизация>")

    if not (0 <= amplitude <= DYNAMIC_RANGE):
        print(f"Ошибка: амплитуда должна быть в диапазоне 0-{DYNAMIC_RANGE} В")
        sys.exit(1)
    
    try:
        dac = mcp4725_driver.MCP4725(DYNAMIC_RANGE, address=0x61, vebrose=False)
        
        print("Генератор треугольного сигнала запущен")
        print(f"Амплитуда: {amplitude} В")
        print(f"Частота сигнала: {frequency} Гц")
        print(f"Частота дискретизации: {sampling} Гц")
        print("Нажмите Ctrl+C для остановки\n")
        
        start_time = time.time()
        
        while True:
            current_time = time.time() - start_time
            voltage = generate_triangle_wave(amplitude, frequency, current_time)
            dac.set_voltage(voltage)
            wait_for_sampling_period(sampling)
        finally:
            dac.deinit()


if __name__ == "__main__":
    main()
