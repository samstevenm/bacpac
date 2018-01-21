import socket
import argparse

bacnetDataType = 5 # BV-5, AV-2, MSV-19

bacnetInstanceNumber = 3 # Load Shed-2, Lighting State-2, Lighting Level-3, Occ-8

bacnetPropertyCode = 85 # present-value=85

# The main function
def main():
	
	# Parse the command line arguments
	parser = argparse.ArgumentParser(description='Send UDP Packets as BACnet.')
	
	parser.add_argument('-a', '--ip-address', help='IP Address (default 192.168.3.1)', default='192.168.3.1')
	parser.add_argument('-b', '--bacnet-port', help='BACnet port (default 47808)', type=int, default=47808)
	
	parser.add_argument('-i', '--instance-id', help='The Instance ID', type=int, required=True)
	parser.add_argument('-n', '--network-number', help='BACnet network-number (default 1)', type=int, default=1)
	parser.add_argument('-c', '--property-code', help='BACnetPropertyCode (default 85)', type=int, default=85)
	parser.add_argument('-p', '--present-value', help='Present value to Send', type=int, required=True)
	
	args = parser.parse_args()
	
	# Variables needed for socket
	hubIP = args.ip_address
	bacnetPort = args.bacnet_port
	
	# Variables needed for packet (as hex)
	hexInstanceID = "%08x"%(args.instance_id)
	networkNumber = "%04x"%(args.network_number)
	propertyCode = "%02x"%(args.property_code)
	binPresentValueValue = "%02x"%(args.present_value)
	
	# Concat the variables to consruct the packet (as hex)
	packet=(
		'810a00210124' 
		+ networkNumber 
		+'060000' 
		+ hexInstanceID 
		+ 'ff0075080f0c0140000319' 
		+ propertyCode 
		+ '3e91' 
		+ binPresentValueValue 
		+ '3f4910'
		)
	#packet="810a002101240001060000001adb04ff0075080f0c0140000319553e91003f4910"
	
	# Get packet as bytes
	fullPacket = bytes.fromhex(packet)
	
	# Provide user feedback
	print("UDP Target port:", bacnetPort)
	print("UDP Target IP:", hubIP)
	print("Instace ID:", args.instance_id)
	print("NetworkNumber:", args.network_number)
	print("PropertyCode:", args.property_code)
	print("Present-Value:", args.present_value)
	print("HexPacket:", packet)
	print("Confirmed-REQ:", fullPacket)
	
	# Setup the socket
	sock = socket.socket(socket.AF_INET, # Internet
						socket.SOCK_DGRAM) # UDP
	
	# Send the packet to socket (oneshot)
	sock.sendto(fullPacket, (hubIP, bacnetPort))
	
	# Get response from socket
	data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
	
	# Provide user feedback
	print("Simple-ACK:", data)

# Script starts here
if __name__ == "__main__":
	main()
