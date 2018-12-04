import socket
import sys
import threading
import pickle
import struct
import random

data_packet_acknowledgment = 43690
null_string = 0

def receive_and_process_input(file_name, data, expected_sequence, data_packet_acknowledgment, soc_receiver, checksum, address):
    with open(file_name, 'ab') as file:
        print("FILE received and size of chunk: " + str(checksum))
        file.write(str.encode(data))
        seq_number = struct.pack('=I', expected_sequence)
        null = struct.pack('=H', null_string)
        acknowledgment_sent = struct.pack('=H',data_packet_acknowledgment)
        acknowledgment = seq_number + null + acknowledgment_sent
        soc_receiver.sendto(acknowledgment, address)

def perform_packet_loss_operation(current_number, self, server):
    if send_buffer.get(ack_number):
        try:
            if (time.time()-((send_buffer[ack_number])[1])) >= TIMEOUT_TIMER:
                for packet in range(ack_number, current_number):
                    data = send_buffer [packet][0]
                    send_buffer[packet] = (data, time.time())
                    self.socket_client.sendto(data,server)
                    print('PACKET LOSS,SEQUENCE NUMBER = '+ str(seq_num[0]))
        except KeyError:
            print(" ")

def message_from_sender(message):
    seq_num = message[0:4]
    seq_num = struct.unpack('=L', seq_num)
    checksum = message[4:6]
    checksum = struct.unpack('=H', checksum)
    data_packet_identifier = message[6:8]
    data_packet_identifier = struct.unpack('=h', data_packet_identifier)
    data = (message[8:])
    actual_message = data.decode('ISO-8859-1','ignore')
    return seq_num, checksum, data_packet_identifier, actual_message

def server_receiver():
    port = int(sys.argv[1])
    file_name = sys.argv[2]
    probability = float(sys.argv[3])
    client_port = 4445

    print("Server's port - " + str(port))
    print("filename - " + file_name)
    print("probability - " + str(probability))

    expected_sequence = 1
    soc_receiver = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    soc_sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    host_address = socket.gethostname()
    print(host_address)
    addr = (host_address, client_port)
    soc_receiver.bind((host_address, port))

    while True:
        message, address = soc_receiver.recvfrom(2048)
        print("address"+ str(address))
        seq_num, checksum, data_identifier, data = message_from_sender(message)
        print('seq_num' +str(seq_num))

        if(random.random()<probability):
            print('PACKET LOSS,SEQUENCE NUMBER = '+ str(seq_num[0]))
        else:
            if expected_sequence == seq_num[0]:
                if checksum[0] == checksum_computation(data):
                    receive_and_process_input(file_name, data, expected_sequence, data_packet_acknowledgment, soc_receiver, checksum, address)
                    expected_sequence += 1

def carry_around_add(x, y):
    return ((x + y) & 0xffff) + ((x + y) >> 16)

def checksum_computation(message):
    add = 0
    for i in range(0, len(message) - len(message) % 2, 2):
        message = str(message)
        w = ord(message[i]) + (ord(message[i + 1]) << 8)
        add = carry_around_add(add, w)
    return ~add & 0xffff

if __name__ == '__main__':
    server_receiver()