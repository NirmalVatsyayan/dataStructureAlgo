#include<stdio.h>
#include<conio.h>


void swap(int *x, int *y){
     int temp = *x;
     *x = *y;
     *y = temp;
}

void selectionSort(int arr[], int length){
    int i, j, min_index;

    for (i =0; i<length-1; i++){
        min_index = i;
        for(j=i+1; j< length; j++){
            if(arr[j] < arr[min_index]){
                min_index = j;
            }
        }
        swap(&arr[min_index], &arr[i]);

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
    int arr[] = {19,12,11,18,15,20,17,10,14,13,16};
    int length = sizeof(arr)/ sizeof(arr[0]);

    printList(arr, length);
    selectionSort(arr, length);
    printList(arr, length);

}
