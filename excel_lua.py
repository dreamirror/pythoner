# -*- coding: UTF-8 -*-

#Author:zhourui
import xlrd
src = raw_input("res path:")
print(src)
workbook = xlrd.open_workbook(src)
print "There are {} sheets in the workbook".format(workbook.nsheets)

out = raw_input("out path:")
fileOutput = open(out,'w')
writeData = "-- this file create by python\n"

#get the cell name
list_name = []
for booksheet in workbook.sheets():
    for col in xrange(booksheet.ncols):
        for row in xrange(booksheet.nrows):
            if  row == 0 :
                list_name.append(str(booksheet.cell(row, col).value))




for booksheet in workbook.sheets():
    writeData = writeData + out.split('.')[0] + ' = {\n'
    for row in xrange(booksheet.nrows):
        for col in xrange(booksheet.ncols):
            if  row == 0 :
                break;
            elif col ==0: 
                id = int(booksheet.cell(row, col).value)
                print(id)
                writeData = writeData + '\t' + '[' + str(id) + ']' + ' = ' + '{ '
            else :
                writeData = writeData +list_name[col]+ '="' + str(booksheet.cell(row, col).value) + '" , '
        else :
            writeData = writeData + '} ,\n'
    else :
        writeData = writeData + '}\n\n'
else :
    fileOutput.write(writeData)

fileOutput.close()

