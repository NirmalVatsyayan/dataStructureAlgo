#include<stdio.h>
#include<conio.h>

void printList(int arr[], int length){

    int index;
    for(index =0; index<length; index++){

        printf("%d ",arr[index]);
    }
    printf("\n");

}

void insertionSort(int arr[], int length){
   int i, key, j;
   for (i = 1; i < length; i++)
   {
       key = arr[i];
       j = i-1;

       /* Move elements of arr[0..i-1], that are
          greater than key, to one position ahead
          of their current position */
       while (j >= 0 && arr[j] > key)
       {
           arr[j+1] = arr[j];
           j = j-1;
       }
       arr[j+1] = key;
   }
}

int main(){
    int arr[]={18,11,14,12,13,19,20,10,15,16,17};
    int length = sizeof(arr) / sizeof(arr[0]);

    printList(arr, length);
    insertionSort(arr, length);
    printList(arr, length);

}
