#Library management system 

class library:
  def __init__(self,program_name="book.txt"):
    self.program_name=program_name
    self.program_name=open("book.txt","+a") # +a modunu açmak hem okur hem de yazar,mevcut değilse dosyayı açar.
  

def listbooks(self):
  self.program_name.tell(0) # programı çağırdım
  books=self.program_name
  
  if not books:
    print("this book is not here")
  else:

     for book in books:
      book_name=book.split(",")  # listeyi bölmesi için split kullanıldı.
      print(f"Booksname: {book_name[0]},Author:{book_name[1]}")

      def addbooks(self):
       booktitle=input("book title:  ")
       bookauthor=input("book author:  ")
      first_release_year=input("release years:  ")
      bookpages=input("pages:  ")
      book_name=(f"{book_title},{bookauthor},{first_release_year},{ bookpages}\n")
  print(book_name)


      def removebook(self):
        self.program_name.tell(0)
   

        



 # new name is created.

  lib=Library()
  
  while true:
   
   print("***MENU***")
   print("1) list books")
   print("2) add books")
   print("3) remove books")
   print("4) exit")

   select=input("please do your select:" )
   

  if select =="1":
       lib.list_books()
  elif select =="2":
      lib.add_books()
  elif select=="3":
       lib.remove_books()
  elif select =="4":
       print("exit")
       
       break
               

