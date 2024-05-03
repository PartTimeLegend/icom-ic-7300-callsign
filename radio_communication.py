import serial
import time

class RadioCommunication:
    def __init__(self, port, baud_rate=9600):
        self.port = port
        self.baud_rate = baud_rate
        self.ser = None

    def open(self):
        try:
            self.ser = serial.Serial(self.port, self.baud_rate, timeout=1)
            return True
        except serial.SerialException as e:
            print(f"Error opening serial port: {e}")
            return False

    def close(self):
        if self.ser:
            self.ser.close()

    def send_command(self, command):
        if self.ser:
            try:
                self.ser.write(command.encode())
                time.sleep(0.1)  # Wait for command to be processed
                return True
            except serial.SerialException as e:
                print(f"Error sending command: {e}")
        return False
