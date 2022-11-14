from pyscbwrapper import SCB

scb = SCB('sv')
# Vi går ner genom trädet
scb.go_down('BE')
scb.go_down('BE0001')
scb.go_down('BE0001G')
# För nodinformation:
# scb.info()
scb.go_down('BE0001T06AR')
# alternativt, kortare:
# scb = SCB('sv','BE','BE0001','BE0001G','BE0001T06AR')
# Nu är vi nere på lövnivå och kan hämta grejer
vars = scb.get_variables()
scb.set_query(tilltalsnamn = 'Stefan', tabellinnehåll = 'Antal bärare', år = '2021')
scb.get_query()
data = scb.get_data()
print(data)
antal = data['data'][0]['values'][0]
print(antal)
