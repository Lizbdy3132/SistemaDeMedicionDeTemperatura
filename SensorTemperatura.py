from abc import ABC, abstractmethod
import random


class SensorTemperatura(ABC):
    @abstractmethod
    def obtener_temperatura(self):
        pass


class SensorCelsius(SensorTemperatura):
    def __init__(self):
        self._last_reading = None
    
    def obtener_temperatura(self):
        self._last_reading = random.uniform(-20.0, 50.0)
        return self._last_reading
    
    def convertir_a_fahrenheit(self):
        if self._last_reading is not None:
            fahrenheit = self._last_reading * 9.0 / 5.0 + 32.0
            return fahrenheit
        return None


class SensorFahrenheit(SensorTemperatura):
    def __init__(self):
        self._last_reading = None
    
    def obtener_temperatura(self):
        self._last_reading = random.uniform(-4.0, 122.0)
        return self._last_reading
    
    def convertir_a_celsius(self):
        if self._last_reading is not None:
            celsius = (self._last_reading - 32.0) * 5.0 / 9.0
            return celsius
        return None


if __name__ == "__main__":
    print("=== SISTEMA DE MEDICIÓN DE TEMPERATURA ===\n")
    
    sensor_c = SensorCelsius()
    sensor_f = SensorFahrenheit()
    
    print("--- SENSOR CELSIUS ---")
    temp_c = sensor_c.obtener_temperatura()
    print(f"Temperatura: {temp_c:.2f} °C")
    temp_f = sensor_c.convertir_a_fahrenheit()
    print(f"Convertido a Fahrenheit: {temp_f:.2f} °F\n")
    
    print("--- SENSOR FAHRENHEIT ---")
    temp_f = sensor_f.obtener_temperatura()
    print(f"Temperatura: {temp_f:.2f} °F")
    temp_c = sensor_f.convertir_a_celsius()
    print(f"Convertido a Celsius: {temp_c:.2f} °C")