#include<stdio.h>
#include<conio.h>

int ternarySearch(int arr[], int data, int low, int length, int max_index){

   if (length >= 1){
       int mid1 = low + (length-low)/3;
       int mid2 = mid1 + (length-low)/3;

       if(data == arr[mid1]){
        if(mid1 > max_index){
            return -1;
        }
        return mid1;
       }

       if(data == arr[mid2]){
        if(mid2 > max_index){
            return -1;
        }
        return mid2;
       }

       if(arr[mid1] > data){
            return ternarySearch(arr, data, low, mid1-1, max_index);
       }else if(arr[mid2] < data){
            return ternarySearch(arr, data, mid2+1, length, max_index);
       }else{
            return ternarySearch(arr, data, mid1+1, mid2-1, max_index);
       }

   }
   return -1;

}

int main(){
    int arr[] = {10,20,30,40,50,60,70,80,90};
    int data = 500;

    int length = sizeof(arr)/ sizeof(arr[0]);
    int search = ternarySearch(arr, data, 0, length, length-1);
    printf("%d", search);

}
