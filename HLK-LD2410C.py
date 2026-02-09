import time
import binascii
import serial

PORT = "/dev/ttyUSB0"  # Windows example: "COM5"
for BAUD in (256000, 57600):
    print("\nTrying baud:", BAUD)
    ser = serial.Serial(PORT, BAUD, bytesize=8, parity="N", stopbits=1, timeout=0.3)
    ser.reset_input_buffer()

    cmd = bytes.fromhex("FD FC FB FA 02 00 A0 00 04 03 02 01")  # read firmware
    ser.write(cmd)
    time.sleep(0.05)
    data = ser.read(64)

    print("RX:", binascii.hexlify(data).decode() or "(nothing)")
    ser.close()
