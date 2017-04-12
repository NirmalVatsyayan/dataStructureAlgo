#include<stdio.h>
#include<conio.h>

int binarySearch(int arr[], int low, int high, int data){

      if (low > high){
        return -1;
      }
      int mid = low + (high - low)/2;
      if(arr[mid] == data){
        return mid;
      }else if(arr[mid] > data){
        return binarySearch(arr, 0, (mid-1), data);
      }else{
        return binarySearch(arr, (mid+1), high, data);
      }

}

int main(){
    int arr[] = {121,222,344,421,533,611};
    int length = sizeof(arr) / sizeof(arr[0]);

    int data = 421;

    int search = binarySearch(arr, 0, length-1, data);
    printf("%d", search);
}
