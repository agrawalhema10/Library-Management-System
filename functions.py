from Book import book
from pickle import load,dump
from student import student
from os import remove,rename
import os
import random
import time
def writebook():
    ch="Y"
    fp=open("book1.dat","ab")
    while ch=="Y":
        bk.create_book()
        dump(bk,fp)
        print()
        ch=input("\t \t Do You Want to Continue<y/n>:")
        print()
        print("#"*70)
        print()
        ch=ch.upper()
def writestudent():
    ch="Y"
    fp=open("student1.dat","ab")
    while ch=="Y":
        st.createstud()
        dump(st,fp)
        ch=input("\t \t Do You Want to Continue <y/n>:")
        ch=ch.upper()
        print()
def display_alls():
    fin=open("student1.dat","rb")
    if not (fin):
        print("\t \t File is Not Found..")
    else:
        try:
            while True:
                print()
                st=load(fin)
                st.showstud()
        except EOFError:
            pass
            fin.close()
def display_allb():
    fin=open("book1.dat","rb")
    if not (fin):
        print()
        print()
        print("Book File is Not Found..")
    else:
        try:
            while True:
                bk=load(fin)
                bk.show_book()
        except EOFError:
            pass
    fin.close()
def display_spb(no):
    flag=0
    fin=open("book1.dat","rb")
    try:
        while True:
            bk=load(fin)
            if(bk.ret_bno()==no):
                bk.show_book()
                flag=1
    except EOFError:
        pass
    fin.close()
    if flag==0:
        print()
        print()
        print("\t \t \t \t BOOK NOT PRESENT..!!")
def display_sps(n):
    flag=0
    fin=open("student1.dat","rb")
    try:
        while True:
            st=load(fin)
            if(st.ret_admno()==n):
                st.showstud()
                flag=1
    except EOFError:
            pass
    fin.close()
    if flag==0:
        print()
        print("\t \t \t STUDENT NOT PRESENT..!!")
def modify_bookrecord():
    found=0
    print()
    print()
    print("\t \t \t Modify Book")
    print()
    print()
    n=input("\t \t Enter Book Number to be Modified:")
    print()
    fin=open("book1.dat","rb")
    fout=open("temp.dat","wb")
    try:
        while True:
            bk=load(fin)
            if bk.ret_bno()==n:
                print()
                print("\t \t \t Book Details")
                bk.show_book()
                print()
                print("\t \t  Enter New Details")
                print()
                print()
                bk.modify_book()
                dump(bk,fout)
                found=1
            else:
                dump(bk,fout)
    except EOFError:
        pass
        if found==0:
            print("\t \t \t \t Book Not Present")
    fin.close()
    fout.close()
    remove("book1.dat")
    rename("temp.dat","book1.dat")
def modify_student_record():
    found=0
    print()
    print("\t \t \t Modify Student Record")
    print()
    print()
    n=input("\t \t Enter Student's Admission Number to be Modified:")
    print()
    fin=open("student1.dat","rb")
    fout=open("temp.dat","wb")
    try:
        while True:
            st=load(fin)
            if st.ret_admno()==n:
                print()
                print("\t \t \t STUDENT DETAILS")
                st.showstud()
                print()
                print("\t \t \t Enter New Student Details:")
                st.modifystud()
                dump(st,fout)
                found=1
            else:
                dump(st,fout)
    except EOFError:
        pass
        if found==0:
            print("\t \t \t \t STUDENT NOT PRESENT")
    fin.close()
    fout.close()
    remove("student1.dat")
    rename("temp.dat","student1.dat")
def del_stud():
    flag=0
    print()
    print()
    n=input("\t \t Enter Admission to be Deleted:")
    print()
    fin=open("student1.dat","rb")
    fout=open("temp.dat","wb")
    try:
        while True:
            st=load(fin)
            if st.ret_admno()!=n:
                dump(st,fout)
            else:
                flag=1
    except EOFError:
        pass
    fin.close()
    fout.close()
    remove("student1.dat")
    rename("temp.dat","student1.dat")
    if flag==1:
        print()
        print("\t \t \t \t RECORD DELETED..!!")
    else:
        print()
        print("\t \t \t \t SORYY..!! RECORD DOES NOT EXIST..!!..")

def del_book():
    flag=0
    print()
    print()
    n=input("\t \t Enter Book No to be Deleted:")
    print()
    fin=open("book1.dat","rb")
    fout=open("temp.dat","wb")
    try:
        while True:
            bk=load(fin)
            if bk.ret_bno()!=n:
                dump(bk,fout)
            else:
                flag=1
    except EOFError:
        pass
    fin.close()
    fout.close()
    remove("book1.dat")
    rename("temp.dat","book1.dat")
    if flag==1:
        print("\t \t \t Record Deleted")
    else:
        print("\t \t \t SORRY..!! RECORD NOT PRESENT..")
def book_issue():
    sn=" "
    bn=" "
    found=0
    flag=0
    print()
    print()
    print("\t \t \t BOOK ISSUE.. \t \t \t")
    print()
    print()
    sn=input("\t \t Enter the Student's Admission Number:")
    print()
    fin1=open("book1.dat","rb")
    fin2=open("student1.dat","rb")
    fout=open("temp.dat","wb")
    try:
        while True:
            st=load(fin2)
            if (st.ret_admno()==sn):
                st.showstud()
                found=1
                if st.ret_token()==0:
                    bn=input("\t \t Enter Book Number:")
                    try:
                        while True:
                            bk=load(fin1)
                            if bk.ret_bno()==bn:
                                bk.show_book()
                                flag=1
                                st.add_token()
                                st.get_stbno(bk.ret_bno())
                                dump(st,fout)
                                os.system("cls")
                                print()
                                print()
                                print("\t \t \t Book Issued Successfully \t \t \t" )
                                print()
                                print("\t PLEASE NOTE : Write the current date in backside")
                                print("\t \t and submit within 15 days")
                                print()
                                print("\t \t Fine Rs.20 for each day after 15 days period.")
                                print
                    except EOFError:
                        pass
                    else:
                        print("\t You have not returned the last book..")
    except EOFError:
        pass
    if(flag==0):
        print("\t \t \t No Such Book Present !!!")
    if(found==0):
        print("\t \t \t No Such Student Exists !!!")
    fin1.close()
    fin2.close()
    fout.close()
    remove("student1.dat")
    rename("temp.dat","student1.dat")
def book_deposit():
    print()
    print()
    print()
    print("\t \t \t BOOK DEPOSITING.")
    sn=" "
    found=0
    flag=0
    day=0
    fine=0
    print()
    print()
    sn=input("\t \t Enter Students Admission Number:")
    print()
    fin1=open("student1.dat","rb")
    fin2=open("book1.dat","rb")
    fout=open("temp.dat","wb")
    try:
        while True:
            st=load(fin1)
            if st.ret_admno()==sn:
                found=1
                print()
                print("\t Student Token Number",st.ret_token())
                if st.ret_token()==1:
                    try:
                        while True:
                            bk=load(fin2)
                            if bk.ret_bno()==st.ret_stbno():
                                bk.show_book()
                                flag=1
                                print()
                                days=int(input("\t Book Deposited In no. of days:"))
                                if days>=15:
                                    fine=(days-15)*20
                                    print()
                                    print("\t Fine : Rs.",fine)
                                    st.reset_token()
                                    st.get_stbno(0)
                                    st.showstud()
                                    dump(st,fout)
                                    print()
                                    print("\t \t BOOK DEPOSITED !!!")
                    except EOFError:
                        pass
                else:
                    print()
                    print("\t \t You have not issued the  book..")
    except EOFError:
        pass
        if(found==0):
            print()
            print("\t No Such Student Exists" )
        fin1.close()
        fin2.close()
        fout.close()
        remove("student1.dat")
        rename("temp.dat","student1.dat")
bk=book()
st=student()