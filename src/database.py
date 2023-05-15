import sqlite3


class Database:
    def __init__(self):
        self.conn = sqlite3.connect('data.db')
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS domains (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                domain_name TEXT
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS records (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                domain_id INTEGER,
                name TEXT,
                value TEXT,
                FOREIGN KEY (domain_id) REFERENCES domains (id)
            )
        ''')
        self.conn.commit()

    def add_domain(self, domain):
        self.cursor.execute('INSERT INTO domains (domain_name) VALUES (?)', (domain.domain_name,))
        self.conn.commit()
        domain.id = self.cursor.lastrowid

    def update_domain(self, domain):
        self.cursor.execute('UPDATE domains SET domain_name = ? WHERE id = ?', (domain.domain_name, domain.id))
        self.conn.commit()

    def delete_domain(self, domain):
        self.cursor.execute('DELETE FROM domains WHERE id = ?', (domain.id,))
        self.conn.commit()

    def get_domains(self):
        self.cursor.execute('SELECT * FROM domains')
        rows = self.cursor.fetchall()
        domains = []
        for row in rows:
            domain = Domain(row[1])
            domain.id = row[0]
            domains.append(domain)
        return domains

    def get_domain(self, domain_id):
        # ...
        for row in rows:
            record = Record(row[2], row[3])
            record.id = row[0]
            domain.add_record(record)
        return domain


class Domain:
    def __init__(self, domain_name):
        self.id = None
        self.domain_name = domain_name
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def get_record(self, record_id):
        for record in self.records:
            if record.id == record_id:
                return record
        return None

    def delete_record(self, record):
        self.records.remove(record)


class Record:
    def __init__(self, name, value):
        self.id = None
        self.name = name
        self.value = value
