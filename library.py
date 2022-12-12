class library:
    def __init__(self,list,name):
        self.booklist=list
        self.name=name
        self.lendDict={}
    def displayBooks(self):
        print(f"We have following books in our library {self.name}")
        for i in self.booklist:
            print(i)
    def lendBook(self,user,book):
        if book not in self.booklist:
            print(f"Book {book} is not available in our Library.")
        else:
            if book not in self.lendDict.keys():
                self.lendDict.update({book:user})
                print(f"Lender-Book database has been updated.You can take the book now.")
            else:
                print(f"Book is already being used by {self.lendDict[book]}")
    def addBook(self,book):
        if book not in self.booklist:
            self.booklist.append(book)
            print(f"Book {book} has been added to the book list.")
        else:
            print(f"Book {book} is alredy present in the library.")
    def returnBook(self,book):
        if book not in  self.booklist:
            print(f"Book {book} is not of this library")
        else:
            if book not in self.lendDict.keys():
                print(f"Book {book} is never been lended.")
            else:
                self.lendDict.pop(book)
                print(f"Book {book} is Successfully returned.")
    def deleteBook(self,book):
        if book not in  self.booklist:
            print(f"You cannot delete this Book {book} because the book is not of our library")
        else:
            if book not in self.lendDict.keys():
                self.booklist.remove(book)
                print(f"Book {book} has been deleted Successfully")
            else:
                print(f"You cannot delete the book {book} at this instance beacuse it has been lended to {self.lendDict[book]}.")
l=['python',10,'c','ds','c++','java','daa','csharp']
obj=library(l,"JMIT")
while(True):
    print(f"Welcome to the {obj.name} library.Enter your choice to continue")
    print("1. Display Books")
    print("2. Add Book")
    print("3. Lend Book")
    print("4. Return Book")
    print("5. Delete Book")
    print("6. Quit")
    user_choice=input("Enter your choice: ")
    if user_choice not in ['1','2','3','4','5','6']:
        print("Please enter the valid option")
        continue
    else:
        user_choice=int(user_choice)
    if user_choice==1:
        obj.displayBooks()
    elif user_choice==2:
        book=input("Enter the name of the book you want to add: ")
        obj.addBook(book)
    elif user_choice==3:
        user=input("Enter your name: ")
        book=input("Enter the name of the book you want to lend: ")
        obj.lendBook(user,book)
    elif user_choice==4:
        book=input("Enter the name of the book you want to return: ")
        obj.returnBook(book)
    elif user_choice==5:
        book=input("Enter the name of the book you want to Delete: ")
        obj.deleteBook(book)
    elif user_choice==6:
        print("Thank You! For visting our library.")
        exit()