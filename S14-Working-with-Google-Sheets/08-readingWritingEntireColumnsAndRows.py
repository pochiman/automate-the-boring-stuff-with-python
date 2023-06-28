import ezsheets
ss = ezsheets.upload('produceSales.xlsx')
sheet = ss[0]
sheet.getRow(1)  # The first row is row 1, not row 0.

sheet.getRow(2)

columnOne = sheet.getColumn(1)
sheet.getColumn(1)

sheet.getColumn('A')  # Same result as getColumn(1)

sheet.getRow(3)

sheet.updateRow(3, ['Pumpkin', '11.50', '20', '230'])
sheet.getRow(3)

columnOne = sheet.getColumn(1)
for i, value in enumerate(columnOne):
    # Make the Python list contain uppercase strings:
    columnOne[i] = value.upper()

sheet.updateColumn(1, columnOne)  # Update the entire column in one request.

# Then you pass it to the updateRows() method:
rows = sheet.getRows()  # Get every row in the spreadsheet.
rows[0] #  Examine the values in the first row.

rows[1]

rows[1][0] = 'PUMPKIN'  # Change the produce name.
rows[1]

rows[10]

rows[10][2] = '400'  # Change the pounds sold.
rows[10][3] = '904'  # Change the total.
rows[10]

sheet.updateRows(rows)  # Update the online spreadsheet with the changes.

sheet.rowCount          # The number of rows in the sheet.
sheet.columnCount       # The number of columns in the sheet.

sheet.columnCount = 4   # Change the number of columns to 4.
sheet.columnCount