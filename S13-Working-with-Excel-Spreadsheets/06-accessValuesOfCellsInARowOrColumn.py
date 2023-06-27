import openpyxl
wb = openpyxl.load_workbook('example.xlsx')
sheet = wb.active
list(sheet.columns)[1]  # Get second column's cells.

for cellObj in list(sheet.columns)[1]:
    print(cellObj.value)