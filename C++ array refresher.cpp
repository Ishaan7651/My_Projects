#include<iostream>
using namespace std;


int main(){

    int r,c,j,i;

cout<<"Enter the number of Rows you want: ";
cin>>r;
cout<<"Enter the number of columns you want: ";
cin>>c;

int arr[r][c];
for(j=0;j<r;j++)
{
    cout<<"Enter the values for the row ";
  for(i=0;i<c;i++)
  {
   cin>>arr[j][i];

  }

}

for(j=0;j<r;j++)
{

  for(i=0;i<c;i++)
  {
    cout<<arr[j][i]<<"\t";

  }
cout<<"\n";
}

}
