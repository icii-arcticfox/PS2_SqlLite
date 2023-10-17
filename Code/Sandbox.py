import sqlite3

databaseName = "TestDatabase"

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
    #[PrintRows]
    users = cursor.fetchall() 



if __name__ == "__main__":
    create_database()

    insert_data('Tim', 32)
    insert_data('Sam', 26)
    insert_data('John', 21)

    query_data()