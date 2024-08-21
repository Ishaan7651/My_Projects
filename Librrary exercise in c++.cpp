#include <iostream>
#include <string>
using namespace std;
class Library{
public:

    Library(){
    string book["To Kill a Mockingbird", "1984", "The Great Gatsby", "The Catcher in the Rye", "Pride and Prejudice", "Harry Potter and the Sorcerer's Stone", "The Lord of the Rings", "The Alchemist", "Sapiens: A Brief History of Humankind", "The Martian"];


    }

};


int main(){
Library obj1;
obj1.display();
return 0;
}
