# bacpac
Simple utility to send UDP packets as BACnet

## Usage

  1. Run `PacketSend.py` You must at least specify: 
		+ `-i INSTANCE_ID ` example `-i 1760002` and 
		+ `-p PRESENT_VALUE` example `-p 1`
	2. You may optionally specify:
		+ `-a IP_ADDRESS` defaults to 192.168.3.1 (Vive Hub default, when directly connected)
		+ `-b BACNET_PORT` defaults to 47808 (Vive Hub default)
		+ `-n NETWORK_NUMBER` defaults to 1 (Vive Hub default)
		+ `-c PROPERTY_CODE` defaults to 85 (present-value)

### TODO
  1. Right now, ALOT is still hardcoded:
		+ bacnet write property (15) 
		+ bacnet data type of 5 (binary-value) 
		+ an object instance number of 2 (Lighting State for Vive areas, Load Shed for Vive Hubs)
  2. Other stuff TBD:

### Example Command
To turn on lights in the first created area on a Vive hub with default settings (1760002, lighting state 1):
 
 ```PacketSend.py -i 1760002 -p 1```
