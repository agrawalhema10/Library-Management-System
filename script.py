from pickle import load,dump
from os import remove,rename
import os
import random
import time
from functions import *
def adminmenu():
    ch="Y"
    while ch=="Y":
        print("\n \n \n \t \t \t ADMINISTRATION MENU \t \t \t \n \n \n ")
        print("\t 1. CREATE STUDENT RECORD")
        print()
        print("\t 2. DISPLAY ALL STUDENTS RECORD")
        print()
        print("\t 3. DISPLAY SPECIFIC STUDENT RECORD")
        print()
        print("\t 4. MODIFY STUDENT RECORD")
        print()
        print("\t 5. DELETE STUDENT RECORD")
        print()
        print("\t 6. CREATE BOOK RECORD")
        print()
        print("\t 7. DISPLAY ALL BOOKS")
        print()
        print("\t 8. DISPLAY SPECIFIC BOOK")
        print()
        print("\t 9. MODIFY BOOK RECORD")
        print()
        print("\t 10.DELETE BOOK RECORD")
        print()
        ch1=int(input("\t \t Enter Your Choice:"))
        print()
        os.system("cls")
        if ch1==1:
            writestudent()
        elif ch1==2:
            display_alls()
        elif ch1==3:
            print()
            print()
            ad=input("\t \t Enter Student's Admno to be Displayed:")
            display_sps(ad)
        elif ch1==4:
            modify_student_record()
        elif ch1==5:
            del_stud()
        elif ch1==6:
            writebook()
        elif ch1==7:
            display_allb()
        elif ch1==8:
            print()
            print()
            bn=input("\t \t ENTER BOOK NUMBER TO BE DISPLAYED:")
            display_spb(bn)
        elif ch1==9:
            modify_bookrecord()
        elif ch1==10:
            del_book()
            print()
            ch=input("\t \t Do you want Continue with ADMINMENU<y/n>:")
            ch=ch.upper()
            print()
            os.system("cls")
            if ch=="Y":
                continue
            else:
                mainmenu()
def mainmenu():
    ch="Y"
    while ch=="Y":
        print()
        print()
        print("\t \t \t MAIN MENU \t \t \t")
        print()
        print("\t 1. BOOK ISSUE")
        print()
        print("\t 2. BOOK DEPOSIT" )
        print()
        print("\t 3. ADMINISTRATION MENU")
        print()
        print("\t 4. EXIT")
        print()
        ch1=int(input("\t \t Enter Your Choice:"))
        print()
        print("\t \t Loading ....")
        time.sleep(5)
        os.system("cls")
        if ch1==1:
            book_issue()
        elif ch1==2:
            book_deposit()
        elif ch1==3:
            adminmenu()
        else:
            exit(0)
        print()
        ch=input("\t \t \t Do You Want to Continue <y/n>:")
        ch=ch.upper()
        if  ch=="N":
            break
        print()
        print()
        print("\t \t Loading...")
        time.sleep(20)
        os.system("cls")
os.system("cls")
mainmenu()