import sqlite3

databaseName = "SandboxDatabase"

def create_database():
    conn = sqlite3.connect(databaseName)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER NOT NULL
        )
    ''')

    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_database()

    #Insert data later

    #Query data later