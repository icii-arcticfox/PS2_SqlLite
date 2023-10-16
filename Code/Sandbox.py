import sqlite3

databaseName = "TestDatabase"

#[SqlFunction]#@51920802
def create_database():
#>1#(51920802):(51920802)
    conn = sqlite3.connect(databaseName)
    cursor = conn.cursor()
#<1#(51920802)~%(1509969043)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER NOT NULL
        )
    ''')
#>1#(51920802):(51920802)
    conn.commit()
    conn.close()
#<1#(51920802)~%(-296304079)

#[SqlFunction]#@93040598
def insert_data(name, age):
#>1#(93040598):(93040598)
    conn = sqlite3.connect(databaseName)
    cursor = conn.cursor()
#<1#(93040598)~%(1509969043)
    cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', (name, age))
#>1#(93040598):(93040598)
    conn.commit()
    conn.close()
#<1#(93040598)~%(-296304079)


#[SqlFunction]#@15852783
def query_data():
#>1#(15852783):(15852783)
    conn = sqlite3.connect(databaseName)
    cursor = conn.cursor()
#<1#(15852783)~%(1509969043)
    cursor.execute('SELECT * FROM users')
    #[PrintRows]#@29136542
    users = cursor.fetchall()
#>1#(29136542):(29136542)
    print('Users:')
    for user in users:
        print( user )
#<1#(29136542)~%(675317066) #>1#(15852783):(15852783)
    conn.commit()
    conn.close()
#<1#(15852783)~%(-296304079)



if __name__ == "__main__":
    create_database()

    insert_data('Tim', 32)
    insert_data('Sam', 26)
    insert_data('John', 21)

    query_data()