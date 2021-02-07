import time

import serial
import serial.tools.list_ports

import constants as cte


def connect_duel_disk():
    print("Connecting to Duel Disk System")
    ser = serial.Serial(
        port=cte.DUEL_DISK_COMM_PORT,
        baudrate=9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1)
    ser.readline()
    ser.flushInput()
    print("Duel Disk on port: " + ser.portstr)
    return ser


def verify_serial(ser):
    connected = check_connection(ser)
    if connected:
        pass
    else:
        while not connected:
            try:
                ser.close()
                ser = connect_duel_disk()
            except serial.SerialException:
                pass
            connected = check_connection(ser)
            time.sleep(1)
    return ser


def check_connection(ser) -> bool:
    dd_port = ser.portstr
    my_ports = [tuple(p) for p in list(serial.tools.list_ports.comports())]
    connected = False
    for port in my_ports:
        if dd_port not in port[0]:
            print("Duel Disk Disconnected")
            connected = connected or False
        else:
            connected = connected or True
    return connected


def select_card_id(ser) -> int:
    """ Read card data from serial connection return int"""
    time.sleep(0.4)
    user_input = ser.readline().decode("utf-8")
    ser.flushInput()
    if user_input == '':
        user_input = select_card_id(ser)
    elif user_input[0] not in [cte.BACK, cte.NEXT_PHASE]:
        user_input = user_input[0:8]
        if user_input == '00000000' or user_input == '11111111':
            user_input = select_card_id(ser)
            ser.flushInput()
    else:
        user_input = user_input[0]
    return user_input
