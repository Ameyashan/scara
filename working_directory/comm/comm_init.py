from utils import serial_ports_setup

arduino1_connected = True
arduino2_connected = True
dynamixel_connected = False

if(arduino1_connected and arduino2_connected):
	[arduino1_serial_object,arduino2_serial_object] = serial_ports_setup.get_connected_arduino_objects() # CHANGE send True,True
