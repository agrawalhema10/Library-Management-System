class student:
    def __init__(self,admno=" ",name=" ",stbno=" ",token=0):
        self.admno=admno
        self.name=name
        self.stbno = stbno
        self.token = token
    def createstud(self):
        print()
        print("\t \t \t Creating Student Record \t \t \t")
        print()
        self.admno = input("\t \t Enter Admission Number:")
        print()
        self.name = input("\t \t Enter Name of the Student:")
        self.stbno = " "
        self.token = 0
        print()
        print()
        print("\t \t \t Student Record Created \t \t \t")
        print()
        print("#" * 70)
        print()
    def showstud(self):
        print()
        print()
        print("\t Admission No.:", self.admno)
        print()
        print("\t Name:", self.name)
        print()
        print("\t Stbno:", self.stbno)
        print()
        print()

    def displaystud(self):
        print()
        print("\t Admission Number of the Student is:", self.admno)
        print()
        print("\t Name of the Student is:", self.name)
        if (self.token == 1):
            print("\t Book Number is:", self.stbno)
    def modifystud(self):
        print()
        print("\t Admission No:", self.admno)
        print()
        self.name =input("\t New Student Name:")
        print()
        print("\t \t Student's Name Modified !!")
    def ret_admno(self):
        return self.admno
    def ret_stbno(self):
        return self.stbno
    def ret_token(self):
        return self.token
    def add_token(self):
        self.token = 1
    def reset_token(self):
        self.token = 0
    def get_stbno(self, t):
        self.stbno = t
    def reportstud(self):
        print(self.admno, self.name, self.token)

