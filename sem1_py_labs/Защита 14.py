import struct

def convert_format():
    return struct.Struct('I')

# Сортировка и запись
def binary_sort_and_write(filename):
    while True:
        with open (filename, "rb+") as f:
            cnt1 = 0
            cnt2 = 4
            is_sorted = True
            while True:
                data1 = f.read(4)
                if not(data1):
                    break
                data2 = f.read(4)
                if not(data2):
                    break
                digit1 = struct.unpack('I', data1)[0]
                digit2 = struct.unpack('I', data2)[0]
                if digit1 > digit2:
                    f.seek(cnt1)
                    digit2 = struct.pack('I', digit2)
                    f.write(digit2)
                    f.seek(cnt2)
                    digit1 = struct.pack('I', digit1)
                    f.write(digit1)
                    is_sorted = False
                cnt1 += 4
                cnt2 += 4
        if is_sorted:
            break

def binary_out(fname):
    with open(fname, 'rb') as f:
        numbers = []
        while True:
            data = f.read(4)
            if not(data):
                break
            data = struct.unpack('i', data)[0]
            numbers.append(data)
        print(numbers)


binary_sort_and_write("output.bin")
binary_out("output1.bin")
