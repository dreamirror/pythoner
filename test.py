#coding: utf-8
import sys
import os
import csv
import xlrd
from xlutils.copy import copy
from openpyxl import load_workbook

global gl_sheet_name
global gl_excel_path
global is_lower

def write_excel():
    global gl_excel_path,gl_sheet_name,is_lower
    if is_lower:
        gl_sheet_name = gl_sheet_name.name
    if gl_excel_path == None or gl_excel_path == '':
        print('None gl path')
        return
    
    data = xlrd.open_workbook(gl_excel_path)
    tmpData = copy(data)

    csvfile = open(gl_sheet_name+"_1.csv","rb")
    from csv import reader
    readers = reader(csvfile)
    n = 0
    m = 0
    for row in readers:
        for i in row:
            tmpData.get_sheet(gl_sheet_name).write(n,m,unicode(i,'utf-8'))
            m = m + 1
        else:
            m = 0
            n = n +1
    tmpData.save(gl_excel_path)

def eachFile(filepath):
    pathDir =  os.listdir(filepath)
    res = []
    for allDir in pathDir:
        child = os.path.join('%s\%s' % (filepath, allDir))
        if child.split('.')[-1] == 'xls' or child.split('.')[-1] == 'xlsx':
            res.append(child.decode('gbk'))
    else:
        return res

def get_excel_name():
    Excel_1 = ''
    Excel_2 = ''

    res = eachFile('Excel_1')
    for file in res:
        Excel_1 = file
    res = eachFile('Excel_2')
    for file in res:
        Excel_2 = file

    excel2csv(Excel_1,Excel_2)

    return Excel_1,Excel_2

def create_csv(filename,sheet):
    if sheet == None:
        print("no such sheet!!")
        return
    try:
        num = filename[6:7]
        xlsx_file_reader = load_workbook(filename)
        csv_filename = sheet.encode('utf_8')+'_'+str(num)+'.csv'
        csv_file = file(unicode(csv_filename,'utf-8'), 'wb')
        csv_file_writer = csv.writer(csv_file)
        sheet_ranges = xlsx_file_reader[sheet]

        for row in sheet_ranges.rows:
            row_container = []
            for cell in row:
                if type(cell.value) == unicode:
                    value = cell.value.encode('utf-8')
                    if value == 'None':
                        value = ''
                    row_container.append(value)
                else:
                    value = str(cell.value)
                    if value == 'None':
                        value = ''
                    row_container.append(value)
            csv_file_writer.writerow(row_container)
        csv_file.close()
    except Exception as e:
        print e

def create_csv_lower(filename,sheet):
    if sheet == None:
        print("no such sheet!!")
        return
    try:
        num = filename[6:7]
        xlsx_file_reader = xlrd.open_workbook(filename)
        csv_filename = sheet.name.encode('utf_8')+'_'+str(num)+'.csv'
        csv_file = file(unicode(csv_filename,'utf-8'), 'wb')
        csv_file_writer = csv.writer(csv_file)

        for row in range(sheet.nrows):
            row_container = []
            for cell in sheet.row_values(row):
                if type(cell) == unicode:
                    value = cell.encode('utf-8')
                    if value == 'None':
                        value = ''
                    row_container.append(value)
                else:
                    value = str(cell)
                    if value == 'None':
                        value = ''
                    row_container.append(value)
            csv_file_writer.writerow(row_container)
        csv_file.close()
    except Exception as e:
        print e


def excel2csv(filename,filename2):
    csv_filename = ''
    csv_filename1 = ''
    if str(filename) == '':
        print 'import excel is None!'
        sys.exit(0)
    elif str(filename).endswith('x'):
        print "office 2007 and a higher version"
        global is_lower
        is_lower = False;
        try:
            xlsx_file_reader = load_workbook(filename)
            sheets = []
            for sheet in xlsx_file_reader.get_sheet_names():
                sheets.append(sheet)
            i = 0
            for sheet in sheets:
                print(str(i)+":"+sheet)
                i = i +1;
            index = raw_input("choose sheet:")
            global gl_sheet_name
            choose_sheet = sheets[int(index)]
            gl_sheet_name = choose_sheet;
            create_csv(filename,choose_sheet)
            create_csv(filename2,choose_sheet)
            global  gl_excel_path
            gl_excel_path = filename2
        except Exception as e:
            print e
        return csv_filename
    elif str(filename).endswith('s'):
        print "office 2007 and a lower version"
        global is_lower
        is_lower = True;
        try:
            xls_file_reader = xlrd.open_workbook(filename)
            length = len(xls_file_reader.sheets())
            sheets = []
            for sheet in xls_file_reader.sheets():
                sheets.append(sheet)
            i = 0
            for sheet in sheets:
                print(str(i) + ":" + sheet.name)
                i = i + 1;
            index = raw_input("choose sheet:")
            global gl_sheet_name
            choose_sheet = sheets[int(index)]
            gl_sheet_name = choose_sheet;
            create_csv_lower(filename, choose_sheet)
            create_csv_lower(filename2, choose_sheet)
            global gl_excel_path
            gl_excel_path = filename2

        except Exception as e:
            print e
        return csv_filename1

if not os.path.exists('Excel_1'):
    os.mkdir('Excel_1')

if not os.path.exists('Excel_2'):
    os.mkdir('Excel_2')

get_excel_name()

do = raw_input("write_table? y/n")
if do == 'y':
    write_excel()
else:
    print("baibai")