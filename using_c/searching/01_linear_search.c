#include<stdio.h>
#include<conio.h>

int linearSearch(int arr[], int data, int length){
   int index;

   for(index=0; index<length; index++){
       if(arr[index] == data){
            return index;
       }
   }

   return -1;

}

int main(){
   int arr[] = {1,2,3,4,5};
   int length = sizeof(arr)/ sizeof(arr[0]);
   int data = 4;

   int search = linearSearch(arr, data, length);
   if(search == -1){
        printf("%d not found !!", data);
   }else{
        printf("%d found at index -> %d !!", data, search);
   }

}
