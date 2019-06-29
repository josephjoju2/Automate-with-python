import openpyxl
wb=openpyxl.load_workbook('example.xlsx')
sheet=wb.get_sheet_by_name('Sheet1')
print(tuple(sheet['A1':'C3']))
for rows in sheet['A1':'C3']:
    for elems in rows:
        print(elems.coordinate,elems.value)
    print('end of row')
