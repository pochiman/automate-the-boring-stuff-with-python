import ezsheets
ss = ezsheets.Spreadsheet('1J-Jx6Ne2K_vqI9J2SO-TAXOFbxx_9tUjwnkPC22LjeU')
ss.sheets       # The Sheet objects in this Spreadsheet, in order.

ss.sheets[0]    # Gets the first Sheet object in this Spreadsheet.

ss[0]           # Also gets the first Sheet object in this Spreadsheet.