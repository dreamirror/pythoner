#!/usr/bin/python
# -*- coding: utf-8 -*-

#Author:zhourui

import sys
import xlrd
import os
import types

reload(sys)
sys.setdefaultencoding("utf8")

if not os.path.exists('lua'):
    os.mkdir('lua')

if not os.path.exists('excel'):
    os.mkdir('excel')

print('1:batch,2:single')
type = raw_input("choose func:")

lua_path = 'lua\\'
excel_path = 'excel\\'

def convert_single():
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
        if child.split('.')[-1] == 'xls' or child.split('.')[-1] == 'xlsx':
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
                if  row == 0 :
                    list_name.append(str(booksheet.cell(row, col).value))

    for booksheet in workbook.sheets():
        writeData = writeData + out.split('.')[0] + ' = {\n'
        for row in xrange(booksheet.nrows):
            for col in xrange(booksheet.ncols):
                if  row == 0 or row == 1 :
                    break;
                elif col ==0:
                    cellStr = booksheet.cell(row, col).value;
                    id = '' if cellStr == '' else int(cellStr)
                    writeData = writeData + '\t' + '[' + str(id).decode("utf-8").encode("utf-8") + ']' + ' = ' + '{ '
                else :
                    cellStr = booksheet.cell(row, col).value
                    if isinstance(cellStr, float):
                        cellStr = int(cellStr) if cellStr % 1 == 0 else cellStr
                    if  str(booksheet.cell(row, col).value)[0:1] == '{':
                        writeData = writeData + list_name[col] + '=' + str(cellStr) + ' , '
                    else:
                        writeData = writeData +list_name[col]+ '="' + str(cellStr) + '" , '
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