class Book:
    
    def __init__(self,title,author,pages):
        self.title=title
        self.author=author
        self.pages=pages
    
    def display(self):
        print("Title: ",self.title)
        print("Author: ",self.author)
        print("pages: ",self.pages)
        
    def Big(self):
        if self.pages>=300:
            print("the book is big")
        else:
            print("The book is not big")

user1=Book("New day","jeeva",18)
user2=Book("Pleasant One","Suriya",400)

user1.display()
user2.Big()
