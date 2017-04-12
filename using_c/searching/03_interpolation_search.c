#include<stdio.h>
#include<conio.h>

/*
interpolation probing formula

The idea of formula is to return higher value of pos
when element to be searched is closer to arr[hi]. And
smaller value when closer to arr[lo]
pos = lo + [ (x-arr[lo])*(hi-lo) / (arr[hi]-arr[Lo]) ]

arr[] ==> Array where elements need to be searched
x     ==> Element to be searched
lo    ==> Starting index in arr[]
hi    ==> Ending index in arr[]

*/
int interpolationSearch(int arr[], int data, int length){
     int low = 0;
     int high = length-1;

     while(low <= high && data <= arr[high] && data >= arr[low]){

        int pos = low + (((double)(high-low) /
              (arr[high]-arr[low]))*(data - arr[low]));

        if (arr[pos] == data)
            return pos;

        if (arr[pos] < data)
            low = pos + 1;
        else
            high = pos - 1;
     }

     return -1;

}

int main(){

    int arr[] = {10,20,30,40,50,60,70,80,90};
    int data = 100;

    int length = sizeof(arr)/sizeof(arr[0]);
    int search = interpolationSearch(arr, data, length);
    printf("%d", search);

}
