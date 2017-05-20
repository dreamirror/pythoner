#!/usr/bin/python
# -*- coding: utf-8 -*-

#Author:zhourui

import sys
import xlrd
import os

reload(sys)
sys.setdefaultencoding("utf8")

print('1：批量，2：单件')
type = raw_input("选择功能:")

lua_path = 'E:\excel_lua\lua\\'
excel_path = 'E:\excel_lua\excel\\'
path = "E:\excel_lua\\"
def convert_single():
    print("单件");
    src = raw_input("res file name:")
    workbook = xlrd.open_workbook(excel_path+src)
    writeData = "-- this file create by python\n"
    out = raw_input("out file name:")
    create_one_lua(writeData,workbook,out+'.lua');

def convert_dozen():
    print("henduo");
    res = eachFile(excel_path)
    for file in res:
        workbook = xlrd.open_workbook(file)
        writeData = "-- this file create by python\n"
        excel_file = file.split('\\')[-1]
        out = excel_file.split('.')[0] + '.lua'
        print(out)
        create_one_lua(writeData, workbook, out);

#find all filles
def eachFile(filepath):
    pathDir =  os.listdir(filepath)
    res = []
    for allDir in pathDir:
        child = os.path.join('%s\%s' % (filepath, allDir))
        if child.split('.')[-1] == 'xls' or child.split('.')[-1] == 'xls':
            res.append(child.decode('gbk'))
    else:
        return res

#get the cell name

def create_one_lua(writeData,workbook,out):
    list_name = []
    fileOutput = open(lua_path+out, 'w')
    for booksheet in workbook.sheets():
        for col in xrange(booksheet.ncols):
            for row in xrange(booksheet.nrows):
                if  row == 1 :
                    list_name.append(str(booksheet.cell(row, col).value))

    for booksheet in workbook.sheets():
        writeData = writeData + out.split('.')[0] + ' = {\n'
        for row in xrange(booksheet.nrows):
            for col in xrange(booksheet.ncols):
                if  row == 0 or row == 1 :
                    break;
                elif col ==0:
                    id = int(booksheet.cell(row, col).value)
                    print(id)
                    writeData = writeData + '\t' + '[' + str(id).decode("utf-8").encode("utf-8") + ']' + ' = ' + '{ '
                else :
                    if  str(booksheet.cell(row, col).value)[0:1] == '{':
                        writeData = writeData + list_name[col] + '=' + str(booksheet.cell(row, col).value) + ' , '
                    else:
                        writeData = writeData +list_name[col]+ '="' + str(booksheet.cell(row, col).value) + '" , '
            else :
                writeData = writeData + '} ,\n'
        else :
            writeData = writeData + '}\n\n'
    else :
        fileOutput.write(writeData)
    fileOutput.close()

#eachFile('E:\excel_lua')

print("222")
print(type)

if int(type) == 1:
    print("批量");
    convert_dozen()
elif int(type) == 2:
    print("单件");
    convert_single();