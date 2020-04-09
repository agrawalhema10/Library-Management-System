class book:
    def __init__(self,bno=" ",bname=" ",authorname=" "):
        self.bno=bno
        self.bname=bname
        self.authorname=authorname
    def create_book(self):
        print()
        print("\t\t\t Creating Book Record \t\t\t")
        print()
        self.bno=input("\t Enter Book Number:")
        print()
        self.bname=input("\t Enter Name of the Book:")
        print()
        self.authorname=input("\t Enter Name of the Author:")
        print()
        print()
        print("\t \t \t Book Created \t \t \t")
    def show_book(self):
        print()
        print()
        print("\t \t Book Number:",self.bno)
        print()
        print("\t \t Book Name:",self.bname)
        print()
        print("\t \t Author Name:",self.authorname)
        print()
        print()
    def modify_book(self):
        print()
        print()
        print("\t \t Book No.: ",self.bno)
        print()
        self.bname=input("\t \t Enter New Book Name:")
        print()
        self.authorname=input("\t \t Enter New Author Name:")
        print()
        print()
        print("\t \t Book Modified")
        print()
    def ret_bno(self):
        return (self.bno)
    def report_book(self):
        print(self.bno,self.bname,self.authorname)