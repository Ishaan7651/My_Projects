class library():
    def __init__(self,*new_book):
        
        self.books = ["To Kill a Mockingbird", "1984", "The Great Gatsby", "The Catcher in the Rye", "Pride and Prejudice", "Harry Potter and the Sorcerer's Stone", "The Lord of the Rings", "The Alchemist", "Sapiens: A Brief History of Humankind", "The Martian"] 
        self.books.extend(new_book)
        self.no_of_books = len(self.books)
        print(self.no_of_books)

a = library("Cursed Child","Twisted fate","I can add as many books as i want","hahahahahah")
print(a.books)