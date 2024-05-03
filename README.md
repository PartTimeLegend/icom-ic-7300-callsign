# IC-7300 Call Sign Setter

This project provides a Python-based system to control IC-7300 radios via serial communication. It supports setting the callsign.

## Structure

The project is split into several modules:

- `radio_communication.py`: Handles the basic serial communication functionalities.
- `ic7300.py`: Specific implementation for the IC-7300 radio, including functions to set the callsign.
- `radio_factory.py`: Factory for creating radio objects based on the type of radio detected.
- `main.py`: Entry point of the application that orchestrates the flow of execution.

## Setup

### Requirements

- Python 3.6+
- `pyserial` package

### Installation

1. Install Python 3.6 or higher if it's not already installed.
2. Clone the repository or download the source files into a directory of your choice.

```bash
git clone https://github.com/PartTimeLegend/icom-ic-7300-callsign.git
```

3. Install Python requirements.
```bash
pip install -r requirements.txt
```

### Running the Application

To run the application, navigate to the directory containing `main.py` and execute the following command:

```bash
python main.py
```

The application will attempt to detect any connected IC-7300 radios. If a radio is found, it will prompt you to enter a callsign, which will then be set on the radio.

## Issues

For any issues or enhancements, please open an issue on the GitHub repository page.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
