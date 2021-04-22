import openpyxl
import os

os.chdir('data/excel/')

work_book = openpyxl.Workbook()
print(type(work_book))
sheet = work_book.get_sheet_by_name('Sheet')
print(sheet)
sheet['A1'].value = 42
sheet['A2'].value = 'Hello'
work_book.save('example.xlsx')
work_book.close()
