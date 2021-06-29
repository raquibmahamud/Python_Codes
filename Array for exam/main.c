#include <stdio.h>

int main() {
    overflow();
    /*if (arr[i]>arr[5]){
        print("This is an overflow error ")
    }*/

    return 0;
}
void overflow(){
    int arr[5], i;

    for(i = 0; i < 6; i++)
    {
        printf("Enter a[%d]: ", i);
        scanf("%d", &arr[i]);

        if (i+1 == 5){
        printf(" This is an overflow");
        break;
        }

        if(0 == arr[i])
            {
            break;
            }
    }
    /*if (arr[i] > arr[5]){
        printf(" This is an overflow");
    }*/
    printf("\nPrinting elements of the array: \n\n");
for (i = 0; i < arr[i]; i++)
    {
        printf("%d", arr[i]);
        if (i < 5)
        printf(", ");
    }

}
