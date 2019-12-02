stringToLevel = {
    'topsecret': 0,
    'secret': 1,
    'confidential': 2,
    'unclassified':3
}
levelToString = {v:k for k,v in stringToLevel.items()}

class sFile:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.content=''

class sUser:
    def __init__(self, name, password, level):
        self.name = name
        self.password = password
        self.level = level

class sFileSystem:
    def __init__(self):
        self.files={}
    
    def createFile(self, filename, level):
        self.files[filename] = sFile(filename, level)
    
    def openFile(self, filename, user, mode):
        reqFile = self.files[filename]
        if mode == 'r':
            if user.level <= reqFile.level:
                return reqFile
            else:
                print('Cannot read up')
        elif mode == 'w':
            if user.level >= reqFile.level:
                return reqFile
            else:
                print('Cannot write down')
    
    def showFiles(self):
        print('File\t\tLevel')
        for key, value in self.files.items():
            print('{}\t{}'.format(key, levelToString[value.level]))

class sUserSystem:
    def __init__(self):
        self.users = {}
    
    def createUser(self, name, password, level):
        self.users[name] = sUser(name, password, level)
    
    def loginUser(self, name, password):
        user = self.users[name]
        if user.password == password:
            return user
        else:
            print("Wrong Password")

class sComputer:
    def __init__(self):
        self.userSystem = sUserSystem()
        self.userSystem.createUser('admin', 'admin', 0)
        self.fileSystem = sFileSystem()
        self.fileSystem.createFile('LVL0.txt', 0)
        self.fileSystem.createFile('LVL1.txt', 1)
        self.fileSystem.createFile('LVL2.txt', 2)
        self.fileSystem.createFile('LVL3.txt', 3)

    def start(self):
        user = None
        while True:
            if user is None:
                choice = int(input('Menu:\n1.Create User\n2.Login\n3.Shutdown\nChoice: '))
                if choice == 1:
                    print('Enter name, password, level(topsecret, secret, confidential,unclassified):')
                    name = input() 
                    password = input() 
                    level = input()
                    self.userSystem.createUser(name, password, stringToLevel[level]);
                elif choice == 2:
                    print('Enter name, password:')
                    name = input()
                    password = input()
                    user = self.userSystem.loginUser(name, password)
                else:
                    break
            elif user is not None:
                choice = int(input('Logged in as {} with {} access\nMenu:\n1.Create File\n2.ReadFile\n3.Write File\n4.Show Files\n5.Logout\nChoice: '.format(user.name,levelToString[user.level])))
                if choice == 1:
                    print('Enter filename, level(topsecret, secret, confidential, unclassified):')
                    filename = input() 
                    level = input()
                    self.fileSystem.createFile(filename, stringToLevel[level])
                elif choice == 2:
                    filename = input('Enter filename:\n')
                    opFile = self.fileSystem.openFile(filename, user, 'r')
                    if opFile:
                        print(opFile.content)
                elif choice == 3:
                    filename = input('Enter filename:\n')
                    opFile = self.fileSystem.openFile(filename, user, 'w')
                    if opFile:
                        opFile.content += input('Enter content:\n')
                elif choice == 4:
                    self.fileSystem.showFiles()
                else:
                    user = None

computer = sComputer()
computer.start()
