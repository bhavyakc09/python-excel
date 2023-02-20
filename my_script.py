import sys
import openpyxl

# Get the input Excel file path from the command-line arguments
input_file = sys.argv[1]

# Load the Excel file
workbook = openpyxl.load_workbook(input_data.xlsx)

# Get the active worksheet
worksheet = workbook.active

# Get the value of cell A1 and print it
cell_value = worksheet['A1'].value
print(f"Input value is: {cell_value}")
