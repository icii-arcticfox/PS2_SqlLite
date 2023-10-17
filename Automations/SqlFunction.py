#type:ignore
from Icii import *

class SqlFunction(PythonAutomation): 
    def ApplyAutomation(self):

        functionText = self.CodeScope.ToString()
        commitNeeded = 'CREATE TABLE' in functionText or 'INSERT INTO' in functionText

        with self.CodeScopeStart:
            conn = sqlite3.connect(databaseName)
            cursor = conn.cursor()

        with self.CodeScopeEnd:
            (|conn.commit()|if commitNeeded |)
            conn.close()