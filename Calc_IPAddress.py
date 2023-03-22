import uno
import os

# Open a new instance of LibreOffice Calc
localContext = uno.getComponentContext()
resolver = localContext.ServiceManager.createInstanceWithContext("com.sun.star.bridge.UnoUrlResolver", localContext)
context = resolver.resolve("uno:socket,host=localhost,port=2002;urp;StarOffice.ComponentContext")
desktop = context.ServiceManager.createInstanceWithContext("com.sun.star.frame.Desktop", context)
calcDoc = desktop.loadComponentFromURL("private:factory/scalc", "_blank", 0, ())

# Create a new sheet
calcDoc.Sheets.insertNewByName("IP Addresses")

# Define the IP range to generate
startIP = "192.168.0.1"
endIP = "192.168.0.100"

# Calculate the number of rows required to fit all the IP addresses
numIPs = sum([256**i for i in range(4)])
startIPInt = sum([int(octet)*256**(3-i) for i, octet in enumerate(startIP.split("."))])
endIPInt = sum([int(octet)*256**(3-i) for i, octet in enumerate(endIP.split("."))])
numRows = endIPInt - startIPInt + 1

# Populate the sheet with the IP addresses
sheet = calcDoc.Sheets.getByName("IP Addresses")
for i in range(numRows):
    row = sheet.Rows.getByIndex(i)
    ipInt = startIPInt + i
    ipStr = ".".join([str((ipInt >> (8*j)) & 0xff) for j in range(4)][::-1])
    row.getCellByPosition(0, i).setString(ipStr)

# Save the spreadsheet to disk
calcDoc.storeToURL("file://" + os.path.abspath("IP Addresses.ods"), ())