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

    AMPLITUDE = 3.0
    SIGNAL_FREQUENCY = 5
    SAMPLING_FREQUENCY = 1000
    DYNAMIC_RANGE = 5.0 

    try:
 
        dac = mcp4725_driver.MCP4725(DYNAMIC_RANGE, address=0x61, vebrose=False)
        
        print(f"Амплитуда: {AMPLITUDE} В")
        print(f"Частота сигнала: {SIGNAL_FREQUENCY} Гц")
        print(f"Частота дискретизации: {SAMPLING_FREQUENCY} Гц")

        
        start_time = time.time()
        

        while True:
            current_time = time.time() - start_time
            

            voltage = generate_triangle_wave(AMPLITUDE, SIGNAL_FREQUENCY, current_time)
            

            dac.set_voltage(voltage)
            

            wait_for_sampling_period(SAMPLING_FREQUENCY)
            

finally:
    dac.deinit()


if __name__ == "__main__":
    main()
