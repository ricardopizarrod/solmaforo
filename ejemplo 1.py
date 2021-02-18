import adafruit_dht
from board import *

# GPIO17
SENSOR_PIN = D7

dht11 = adafruit_dht.DHT11(SENSOR_PIN, use_pulseio=False)

temperature = dht11.temperature
humidity = dht11.humidity

print(f"Humidity= {humidity:.2f}")
print(f"Temperature= {temperature:.2f}°C")