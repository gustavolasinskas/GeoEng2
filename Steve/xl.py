from openpyxl import load_workbook

wb = load_workbook('template.xlsx')
ws = wb.get_sheet_by_name('TEMPLATE')

for row in ws.rows:
    for cell in row:
        print(cell.value)
