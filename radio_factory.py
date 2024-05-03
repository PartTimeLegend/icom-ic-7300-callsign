import serial.tools.list_ports
from ic7300 import IC7300

class RadioFactory:
    @staticmethod
    def create_radio(port):
        if RadioFactory.is_ic7300(port):
            return IC7300(port)
        else:
            return None

    @staticmethod
    def is_ic7300(port):
        try:
            with serial.Serial(port, 9600, timeout=1) as ser:
                ser.write(b'IF;')
                response = ser.readline().decode().strip()
                return response.startswith("IF")
        except serial.SerialException as e:
            print(f"Error checking radio type on port {port}: {e}")
            return False
