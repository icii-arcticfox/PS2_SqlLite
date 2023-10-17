import sqlite3

databaseName = "SandboxDatabase"

#[SqlFunction]
def create_database():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER NOT NULL
        )
    ''')

#[SqlFunction]
def insert_data(name, age):
    cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', (name, age))


#[SqlFunction]
def query_data():
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    return users


if __name__ == "__main__":
    create_database()

    insert_data('Mia', 27)
    insert_data('Malik', 19)
    insert_data('Leo', 42)

    users = query_data()
    print('Users:')
    for user in users:
        print( user )