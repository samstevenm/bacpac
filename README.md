# bacpac
Simple utility to send UDP packets as BACnet

## Usage

Just run packetsend.py
  You must specify an instance ID `-i 1760002` and value.
  Right now it's hard coded with bacnet data type of 5 (binary-value) and a object instance number of 2 (Lighting State for Vive areas)

To turn on lights in first area on a Vive hub with default settings (1760002 lighting state 1):
  `PacketSend.py -i 1760002 -p 1`
