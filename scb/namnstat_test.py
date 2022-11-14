from pyscbwrapper import SCB

scb = SCB('sv')
scb.go_down('BE')
scb.go_down('BE0001')
scb.go_down('BE0001G')
scb.go_down('BE0001T06AR')
vars = scb.get_variables()
scb.set_query(tilltalsnamn = 'Stefan', tabellinnehåll = 'Antal bärare', år = '2021')
scb.get_query()
data = scb.get_data()
print(data)
antal = data['data'][0]['values'][0]
print(antal)
