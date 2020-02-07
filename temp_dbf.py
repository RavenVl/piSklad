import dataset
from dbfread import DBF

db = dataset.connect('sqlite:///:memory:')
table = db['sklad']

for record in DBF('g:\\temp\\skladp17.dbf', lowernames=True):
    table.insert(record)
all_rez = table.find(kodpr='11813', kodpl='38')
for rec in all_rez:
    print(rec)

# for record in DBF('g:\\temp\\skladp17.dbf'):
#     if record['KODPR'] == "11813" and record['KODPL'] == 38:
#         print(record['TOVAR'], record['CENA'])
