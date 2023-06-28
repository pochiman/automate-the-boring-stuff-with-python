import ezsheets
ss = ezsheets.createSpreadsheet('Delete me')  # Create the spreadsheet.
ezsheets.listSpreadsheets()  # Confirm that we've created a spreadsheet.

ss.delete()  # Delete the spreadsheet.
ezsheets.listSpreadsheets()

# ss.delete(permanent=True)