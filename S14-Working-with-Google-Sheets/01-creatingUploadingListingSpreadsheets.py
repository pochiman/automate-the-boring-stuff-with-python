import ezsheets
ss = ezsheets.Spreadsheet('1J-Jx6Ne2K_vqI9J2SO-TAXOFbxx_9tUjwnkPC22LjeU')
ss
ss.title

# To make a new, blank spreadsheet
ss = ezsheets.createSpreadsheet('Title of My New Spreadsheet')
ss.title

# To upload an existing Excel, OpenOffice, CSV, or TSV spreadsheet to Google Sheets
ss = ezsheets.upload('my_spreadsheet.xlsx')
ss.title

# You can list the spreadsheets in your Google account
ezsheets.listSpreadsheets()