import sqlite3

def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    
    # Létrehozzuk a táblákat
    c.execute('''
        CREATE TABLE IF NOT EXISTS tools (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            quantity INTEGER NOT NULL
        )
    ''')
    
    c.execute('''
        CREATE TABLE IF NOT EXISTS persons (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            address TEXT NOT NULL
        )
    ''')
    
    c.execute('''
        CREATE TABLE IF NOT EXISTS loans (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            person_id INTEGER NOT NULL,
            tool_id INTEGER NOT NULL,
            loan_date DATE NOT NULL,
            return_date DATE NOT NULL,
            FOREIGN KEY(person_id) REFERENCES persons(id),
            FOREIGN KEY(tool_id) REFERENCES tools(id)
        )
    ''')
    
    # Például szerszámok hozzáadása
    tools = [
        ('Kalapács', 10),
        ('Csavarhúzó', 15),
        ('Fúrógép', 5),
        ('Csiszoló', 10),
        ('Gyalu', 3),
        # Adj hozzá több szerszámot szükség szerint
    ]
    c.executemany('INSERT INTO tools (name, quantity) VALUES (?, ?)', tools)
    
    conn.commit()
    conn.close()
    print("Adatbázis inicializálva és szerszámok hozzáadva.")

if __name__ == '__main__':
    init_db()
