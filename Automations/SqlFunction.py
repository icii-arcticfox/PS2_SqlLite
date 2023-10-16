#type:ignore
from Icii import *

class SqlFunction(PythonAutomation): 
    def ApplyAutomation(self):


        with self.CodeScopeStart:
            conn = sqlite3.connect(databaseName)
            cursor = conn.cursor()

        with self.CodeScopeEnd:
            
               conn.commit()
               conn.close()
