import mcp4725_driver
import signal_generator
import time
import sys

SAMPLING_FREQUENCY = 1000 
SIGNAL_FREQUENCY = 10
DYNAMIC_RANGE = 5.0

def main():
    try:
        dac = mcp4725_driver.MCP4725(DYNAMIC_RANGE, address=0x61, vebrose=False)
        
        print("Генератор сигнала запущен. Нажмите Ctrl+C для остановки.")
        print(f"Частота сигнала: {SIGNAL_FREQUENCY} Гц")
        print(f"Частота дискретизации: {SAMPLING_FREQUENCY} Гц")
        
        start_time = time.time()
        
        while True:
            current_time = time.time() - start_time
            voltage = signal_generator.get_sin_wave_amplitude(SIGNAL_FREQUENCY, current_time)
            dac.set_voltage(voltage)
            signal_generator.wait_for_sampling_period(SAMPLING_FREQUENCY)
            
    finally:
        dac.deinit()
        print("ЦАП отключен.")

if __name__ == "__main__":
    main()
