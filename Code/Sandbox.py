import sqlite3

databaseName = "TestDatabase"

#[SqlFunction]#@39691436
def create_database():
#>1#(39691436):(39691436)
    conn = sqlite3.connect(databaseName)
    cursor = conn.cursor()
#<1#(39691436)~%(1509969043)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER NOT NULL
        )
    ''')
#>1#(39691436):(39691436)
    conn.commit()
    conn.close()
#<1#(39691436)~%(-296304079)

#[SqlFunction]#@62173632
def insert_data(name, age):
#>1#(62173632):(62173632)
    conn = sqlite3.connect(databaseName)
    cursor = conn.cursor()
#<1#(62173632)~%(1509969043)
    cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', (name, age))
#>1#(62173632):(62173632)
    conn.commit()
    conn.close()
#<1#(62173632)~%(-296304079)


#[SqlFunction]#@98070473
def query_data():
#>1#(98070473):(98070473)
    conn = sqlite3.connect(databaseName)
    cursor = conn.cursor()
#<1#(98070473)~%(1509969043)
    cursor.execute('SELECT * FROM users')
    #[PrintRows]#@43106813
    users = cursor.fetchall()
#>1#(98070473):(98070473)
    conn.close()
#<1#(98070473)~%(334436407) #>1#(43106813):(43106813)
print('Users:')
for user in users:
    print( user )
#<1#(43106813)~%(675317066)



if __name__ == "__main__":
    create_database()

    insert_data('Tim', 32)
    insert_data('Sam', 26)
    insert_data('John', 21)

    query_data()