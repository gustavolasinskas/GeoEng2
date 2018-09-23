#!/usr/bin/env python3

import openpyxl, os

os.chdir('/users/alex/desktop')

workbook = openpyxl.load_workbook('example.xlsx')

type(workbook)

sheet = workbook.get_sheet_by_name('Sheet1')
type(sheet)

workbook.get_sheet_names()
sheet['B1']
cell = sheet["B1"]
print (cell.value)
print ('\n')

for i in range (1,8):
    print (sheet.cell(row=i, column=2).value)
