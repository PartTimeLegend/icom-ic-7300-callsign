import serial
from radio_factory import RadioFactory

def main():
    ic7300_ports = [port.device for port in serial.tools.list_ports.comports() if RadioFactory.is_ic7300(port.device)]
    if ic7300_ports:
        print("Found IC-7300 radios on ports:", ic7300_ports)
        selected_port = ic7300_ports[0]  # Just select the first found radio for simplicity
        radio = RadioFactory.create_radio(selected_port)
        if radio:
            callsign = input("Enter callsign: ")
            radio.set_callsign(callsign)
        else:
            print("Failed to create IC-7300 radio object.")
    else:
        print("No IC-7300 radio found.")

if __name__ == "__main__":
    main()
