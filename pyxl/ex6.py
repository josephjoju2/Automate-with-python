import openpyxl, pprint
print('opening workbook...')
wb=openpyxl.load_workbook('censuspopdata.xlsx')
sheet=wb.get_sheet_by_name('Population by Census Tract')
countydata= {}
for row in range(2,sheet.max_row+1):
    state=sheet['B'+str(row)].value
    county=sheet['C'+str(row)].value
    pop=sheet['D'+str(row)].value
    countydata.setdefault(state,{})
    countydata[state].setdefault(county , {'pop': 0,'tracts': 0})
    countydata[state][county]['tracts'] += 1
    countydata[state][county]['pop'] +=int(pop)
print('writing results')
resultfile=open('census2010.py','w')
resultfile.write('alldata ='+pprint.pformat(countydata))
resultfile.close()
print('done')
