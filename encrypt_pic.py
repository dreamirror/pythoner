# -*- coding: utf-8 -*-
import  random
import os
import sys

encrypt_key = random.randint(1,255)

first_flag = 0x12
second_flag = 0x34
third_flag = 0x56

def encrypt_pic(path):
    f = open(path,'rb')
    data = f.read()
    f.close()
    file_bytes = bytearray(data)
    if (file_bytes[0] == first_flag and file_bytes[1] == second_flag and third_flag == file_bytes[2]):
        print('file encrypted!!')
    else:
        temp_data = bytearray(0)
        temp_data.append(first_flag)
        temp_data.append(second_flag)
        temp_data.append(third_flag)
        temp_data.append(encrypt_key)
        leng = len(file_bytes)
        print(leng)
        for byte in file_bytes:
            encoded = byte ^ encrypt_key
            temp_data.append(encoded)
        file_name = path.split('.')[0]
        #os.remove(path)
        f2 = open(file_name,'wb')
        f2.write(temp_data)
        f2.close()

def decode_pic(path):
    f = open(path,'rb')
    data = f.read()
    f.close()

    file_bytes = bytearray(data)
    if (file_bytes[0] == first_flag and file_bytes[1] == second_flag and third_flag == file_bytes[2]):
        encrypt_key = file_bytes[3]
        file_bytes = file_bytes[4:]
        temp_data = bytearray(0)
        leng = len(file_bytes)
        print(leng)
        for byte in file_bytes:
            encoded = byte ^ encrypt_key
            temp_data.append(encoded)
        type = get_type(temp_data[0:8],temp_data[-2:])
        f2 = open('decode\\'+path+'.'+type,'wb')
        f2.write(temp_data)
        f2.close()
        print("decode finish")
    else:
        print('wrong file');

def compare_byte(bytes1,bytes2):
    i = 0
    for byte in bytes1:
        if byte != bytes2[i]:
            return False;
        i = i + 1
    return True

def get_type(bytes,bytes_end):
    jpg = [0xff,0xd8]
    tag = [0x00,0x00,0x02,0x00,0x00]
    png = [0x89,0x50,0x4e,0x47,0x0d,0x0a,0x1a,0x0a]
    git = [0x47,0x49,0x46,0x38,0x39,0x61]
    tiff = [0x4d,0x4d,0x49,0x49]
    ico = [0x00,0x00,0x01,0x00,0x01,0x00,0x20,0x20]
    cur = [0x00,0x00,0x02,0x00,0x01,0x00,0x20,0x20]
    iff = [0x46,0x4f,0x52,0x4d]
    ani = [0x52,0x49,0x46,0x46]
    bmp = [0x42,0x4d]
    pcx = [0x0a]
    if compare_byte(jpg,bytes):
        print bytes_end[0],bytes_end[1]
        if bytes_end[0] == 0xff and bytes_end[1] == 0xd9 :
            print('jpg')
            return 'jpg'
    elif compare_byte(png,bytes):
        return 'png'
        print('png')
    elif compare_byte(tag,bytes):
        return 'tag'
        print('tag')
    elif compare_byte(git,bytes):
        return 'git'
        print('git')
    elif compare_byte(tiff,bytes):
        return 'tiff'
        print('tiff')
    elif compare_byte(ico,bytes):
        return 'ico'
        print('ico')
    elif compare_byte(cur,bytes):
        return 'cur'
        print('cur')
    elif compare_byte(iff,bytes):
        return 'iff'
        print('iff')
    elif compare_byte(ani,bytes):
        return 'ani'
        print('ani')
    elif compare_byte(bmp,bytes):
        return 'bmp'
        print('bmp')
    elif compare_byte(pcx,bytes):
        return 'pcx'
        print('pcx')

    print('get type')

#encrypt_pic('1.jpg')
decode_pic('1')
