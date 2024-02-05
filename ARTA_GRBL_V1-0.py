#
#
# ARTA GRBL Translator
# Dr. Heinrich Weber & Ralf Grafe
#
# 02.02.2024
#
#
#
#
import configparser
import serial
import sys
import time

class SerialPort:
    def __init__(self, settings, command_mappings, grbl_paramater):
        self.ser = serial.Serial(
            port=settings['SerialSettings']['port'], 
            baudrate=int(settings['SerialSettings']['baud_rate']), 
            timeout=int(settings['SerialSettings']['timeout'])
        )
        self.command_mappings = command_mappings
        self.grbl_parameter = grbl_parameter


    def send(self, data):
        if self.ser.is_open:
            self.ser.write(("\r\n\r\n").encode())                                               # Wake up GRBL
            time.sleep(2)                                                                       # Wait for GRBL to initialize 
            self.ser.flushInput()                                                               # Flush startup text in serial input
            # Opening of the serial port triggers DTR, which performs reset on an Arduino!! 
            try:
                # Attempt to convert to a float
                test = float(data)
                # print (f"'{data}' is a floating-point number.")
          
                translated_data = self.command_mappings.get(data, data)  # Translate the command
                
                # grbl_speed = f"{self.grbl_parameter.get('grblspeed', '')}"
                # print(f"grbl_speed: {grbl_speed}")
                
                modified_data = f"G1X{translated_data}F{self.grbl_parameter.get('grblspeed', '')}"  # Add 'G1X' in front of recieved float plus 'F' and Speed from config file
                self.ser.write((modified_data + "\r").encode())
                print(f"Data sent: {modified_data}")
                time.sleep(0.5)  # Wait a bit for the response
                self.read_response()
            except ValueError:
                # Input is not a number
                # print (f"'{data}' contains characters or is otherwise non-numeric.")
                
                translated_data = self.command_mappings.get(data, data)  # Translate the command
                
                self.ser.write((translated_data + "\r").encode())
                print(f"Data sent: {translated_data}")
                time.sleep(0.5)  # Wait a bit for the response
                self.read_response()
        else:
            print("Serial port is not open.")

    def read_response(self):
        if self.ser.is_open:
            response = self.ser.read_all()
            if response:
                print("Received response:\r\n", response.decode())
            else:
                print("No response received.")

    def close(self):
        if self.ser.is_open:
            self.ser.close()
            #print("Serial port closed.")

def load_config(filename):
    config = configparser.ConfigParser()
    config.read(filename)
    return config

def load_command_mappings(config):
    return dict(config.items('CommandMappings'))
    
def load_grbl_parameter(config):
    return dict(config.items('GRBLParameter'))
    
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python ARTA_GRBL.py <command>\r\n")
        print("Possible Commands are:\r")
        print("-r\r")
        print("A numerical value between 1 and 360\r")
        print("A GRBL V1.1 Command")
        sys.exit(1)

    command = sys.argv[1]

    config_file = 'config.cfg'
    config = load_config(config_file)
    command_mappings = load_command_mappings(config)
    grbl_parameter = load_grbl_parameter(config)

    serial_port = SerialPort(config, command_mappings, grbl_parameter)
    
    try:
        serial_port.send(command)
    finally:
        serial_port.close()
