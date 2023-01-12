import os

class Column:
    def __init__(self, name, type):
        self.name = name
        self.type = type

class Table:
    def __init__(self, name):
        self.name = name
        self.rows = []
        
    def AddColumn(self, column):
        self.rows.append(column)

class Database:

    def __init__(self, filename):
        self.filename = filename
        self.tables = []

    def SaveStructure(self):
        for i in range(len(self.tables)):
            if not os.path.exists(f"{self.tables[i].name}.db"):
                f = open(f"{self.tables[i].name}.db", "wb")
                for c in range(len(self.tables[i].name)):
                    f.write(self.tables[i].name[c].encode('ascii'))
                f.close()
            else:
                f = open(f"{self.tables[i].name}.db", 'rb')
                print(f.read(16))
                
                f.close()

    def AddTable(self, table):
        self.tables.append(table)
        self.SaveStructure()

    def GetTableByName(self, name):
        for i in range(len(self.tables)):
            if self.tables[i].name == name:
                return self.tables[i] 

    # CRUD

    def Create(self, table, record):
        f = open(f"{table}.db", "wb")
        # zapisz instrukcje w pierwszym rekordzie (nagłówku)
        #f.seek(0)
        #f.write(0)
        for i in range(len("ala ma kota")):
            f.write("ala ma kota"[i])
        f.close()

    def Read(self, table, index):
        f = open(f"{table}.db", "rb")
        
        f.close()

    def Update(self, table, index, record):
        f = open(f"{table}.db", "wb")
        
        f.close()

    def Delete(self, table, index):
        f = open(f"{table}.db", "wb")
        
        f.close()

db = Database("test")
table1 = Table("table1")
table1.AddColumn(Column("column1", type("s")))
db.AddTable(table1)
        
