import pyodbc

# Строка, определяющая источник ODBC. DefaultDir — директория с DBF-файлом.
path_dbf = "c:\\KS\\TSKL7.LOC\\NetDat\\SKLADP17.DBF "
# s = "Driver={Microsoft dBASE Driver (*.dbf)};DefaultDir=g:\\temp"
# s = "Driver={Microsoft dBASE Driver (*.dbf)};DriverID=277;Dbq=g:\\temp;"
# s = "Driver={Microsoft dBase Driver (*.dbf)};datasource=g:\\temp\\prod.dbf;"
# s = "Provider=Microsoft.ACE.OLEDB.12.0;Data Source=g:\\temp;Extended Properties=dBASE IV;User ID=Admin;Password=;"
# s = "Driver={Microsoft Visual FoxPro Driver};SourceType=DBF;SourceDB=g:\\temp;"
s = "Provider=Microsoft.Jet.OLEDB.4.0;Data Source=g:\\temp; Extended Properties=dBASE IV;"
db = pyodbc.connect(s, autocommit=True)
cursor = db.cursor()

# Пример выборки.
cursor.execute("select * from PROD")
tables = cursor.tables()
for _ in tables:
    print (_)
# Извлечение записи.
# row = cursor.fetchone()
# if row:
#     print(row)
#
# # Закрываем курсор и ресурс.
cursor.close()
db.close()