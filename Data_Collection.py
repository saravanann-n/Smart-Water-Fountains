#Sensor Data Collection: 
#Code to collect data from the IoT sensors, including flow rate, water level, temperature, and pressure.

import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
import Adafruit_DHT
import RPi.GPIO as GPIO
 
# Setup SPI for ADC communication
SPI_PORT = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))
 
# Setup GPIO for DHT11 temperature and humidity sensor
DHT_SENSOR_PIN = 4
DHT_SENSOR_TYPE = Adafruit_DHT.DHT11
 
# Setup GPIO for water level sensor
WATER_LEVEL_PIN = 17
 
# Setup GPIO for flow rate sensor
FLOW_RATE_PIN = 27
 
# Setup GPIO for pressure sensor
PRESSURE_PIN = 22
 
def read_flow_rate():
    pulse_count = 0
 
    def count_pulse(channel):
        nonlocal pulse_count
        pulse_count += 1
 
    GPIO.add_event_detect(FLOW_RATE_PIN, GPIO.FALLING, callback=count_pulse)
 
    time.sleep(1)
 
    GPIO.remove_event_detect(FLOW_RATE_PIN)
    flow_rate = pulse_count / 7.5
 
    return flow_rate
 
def read_water_level():
    if GPIO.input(WATER_LEVEL_PIN):
        return "Full"
    else:
        return "Empty"
 
def read_temperature():
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR_TYPE, DHT_SENSOR_PIN)
    return temperature
 
def read_pressure():
    adc_value = mcp.read_adc(PRESSURE_PIN)
    voltage = adc_value * (3.3 / 1023.0)
    pressure = voltage * 15.0
    return pressure
 
if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(FLOW_RATE_PIN, GPIO.IN)
    GPIO.setup(WATER_LEVEL_PIN, GPIO.IN)
 
    while True:
        flow_rate = read_flow_rate()
        water_level = read_water_level()
        temperature = read_temperature()
        pressure = read_pressure()
 
        print(f"Flow Rate: {flow_rate} L/min")
        print(f"Water Level: {water_level}")
        print(f"Temperature: {temperature}°C")
        print(f"Pressure: {pressure} kPa")
 
        time.sleep(1)
