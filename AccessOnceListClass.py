class SecureList():

    def __init__(self, myList):
        self.myList = myList.copy()

    def __str__(self):
            try:
                return str(self.myList)
            finally:
                self.myList.clear()

    def __repr__(self):
            self.myList.__repr__()
            self.myList.clear()
        
    def __getitem__(self, key):
            try:
                return self.myList[key]
            finally:
                self.myList.remove(self.myList[key])
    
    def __len__(self):
        return len(self.myList)


a = [1,2,3,4]
b = SecureList(a)

print("test %s" %b )

print("test %s" %b )