import sqlite3

databaseName = "SandboxDatabase"

#[SqlFunction]#@68572024
def create_database():
#>1#(68572024):(68572024)
    conn = sqlite3.connect(databaseName)
    cursor = conn.cursor()
#<1#(68572024)~%(1509969043)

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER NOT NULL
        )
    ''')
#>1#(68572024):(68572024)
    conn.commit()
    conn.close()
#<1#(68572024)~%(-296304079)



if __name__ == "__main__":
    create_database()

    #Insert data later

    #Query data later