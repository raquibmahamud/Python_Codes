#include<stdio.h>

void print ( int *temp, int size);
int main( ) {

int a[10]={1,2,3,4,5,6,7, 8, 9, 10}, size = 10;
print(a, size);
return 0;
}
void print ( int *temp, int size){
    if(size){
        print(temp+1, - -size);
    }

}

