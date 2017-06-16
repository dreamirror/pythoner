# -*- coding: utf-8 -*-
import  random
import os
import sys

encrypt_key = random.randint(1,255)

first_flag = 0x12
second_flag = 0x34
third_flag = 0x56
pic_type = 0 # 0:png 1:jpg

def encrypt_pic(path):
    f = open(path,'rb')
    data = f.read()
    data_len = f.tell()
    f.close()
    file_bytes = bytearray(data)
    if (file_bytes[0] == first_flag and file_bytes[1] == second_flag and third_flag == file_bytes[2]):
        print('file encrypted!!')
    else:
        file_name = path.split('.')[-1]
        if str(file_name) == 'png':
            pic_type = 0
        elif str(file_name) == 'jpg':
            pic_type = 1

        temp_data = bytearray(0)
        temp_data.append(first_flag)
        temp_data.append(second_flag)
        temp_data.append(third_flag)
        temp_data.append(encrypt_key)
        #temp_data.append(pic_type)

        for byte in file_bytes:
            encoded = byte ^ encrypt_key
            temp_data.append(encoded)
        file_name = path.split('.')
        os.remove(path)
        f2 = open(path,'wb')
        f2.write(temp_data)
        f2.close()

encrypt_pic('1.jpg')

