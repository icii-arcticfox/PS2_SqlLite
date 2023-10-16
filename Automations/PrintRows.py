#type:ignore
from Icii import *

class PrintRows(PythonAutomation): 
    def ApplyAutomation(self):

        variable = self.NextVariable()
        name = variable.Name

        singleName = ''
        if name.endswith('s'):
            singleName = name[:-1]
        else:
            singleName = '_' + name;

        with self.CodeAfterNext:
            print('((name.UpperStartCamelCase() )):')
            for ((singleName)) in ((name)):
                print( ((singleName)) )
