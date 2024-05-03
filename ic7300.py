from radio_communication import RadioCommunication

class IC7300(RadioCommunication):
    def __init__(self, port):
        super().__init__(port)

    def set_callsign(self, callsign):
        if self.open():
            command = f'FA{callsign};'
            if self.send_command(command):
                print("Callsign set successfully.")
            else:
                print("Failed to set callsign.")
            self.close()
