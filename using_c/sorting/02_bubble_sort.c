#include<stdio.h>
#include<conio.h>

void swap(int *x, int *y){
     int temp = *x;
     *x = *y;
     *y = temp;
}


void bubbleSort(int arr[], int length){

    int i,j;

    for (i=0; i<length-1; i++){
        for (j=0; j<length-1-i; j++){
            if (arr[j] > arr[j+1]){
                swap(&arr[j], &arr[j+1]);
            }
        }
    }

}

void printList(int arr[], int length){

    int index;
    for(index =0; index<length; index++){

        printf("%d ",arr[index]);
    }
    printf("\n");

}


int main(){
    int arr[]={18,11,14,12,13,19,20,10,15,16,17};
    int length = sizeof(arr) / sizeof(arr[0]);

    printList(arr, length);
    bubbleSort(arr, length);
    printList(arr, length);

}
