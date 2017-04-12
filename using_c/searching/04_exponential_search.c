#include<stdio.h>
#include<conio.h>

int min(int x, int y){
   if(x>y){
       return y;
   }
   return x;
}

int exponentialSearch(int arr[], int data, int length){
    if(arr[0] == data){
        return 0;
    }

    int index = 1;
    while(index < length && arr[index] <= data){
        index = index * 2;
    }

    return binarySearch(arr, index/2, min(index, length), data);

}

int binarySearch(int arr[],int low, int high, int data){
     if(low > high){
        return -1;
     }

     int mid = low + (high-low)/2;

     if (arr[mid] == data){
        return mid;
     }else if(arr[mid] > data){
        return binarySearch(arr, low, mid-1, data);
     }else{
        return binarySearch(arr, mid+1, high, data);
     }
}

int main(){

    int arr[] = {10,20,30,40,50,60,70};
    int data = 80;
    int length = sizeof(arr) / sizeof(arr[0]);

    int search = exponentialSearch(arr, data, length);
    printf("data present at index --> %d", search);

}
