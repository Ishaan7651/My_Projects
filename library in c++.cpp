#include <iostream>
#include <string>
using namespace std;
class Library{
public:

    int display(){
    string book;
    cout<<"Enter the book name: ";
    getline(cin,book);
    cout<<"The book name is: "<<book;
    return 0;
    }

};


int main(){
Library obj1;
obj1.display();
return 0;
}
