import openpyxl
wb=openpyxl.load_workbook('example.xlsx')
sheet=wb.active
c=sheet.columns[1]
print(c)
for i in c:
    print(i.value)
r=sheet.rows[0]
for i in r:
    print(i.value)
