/*
Finding the minimum and maximum values for an array in C
YouTube Channel: Asim Code
https://youtu.be/2qhXa2sTbJ4
*/
#include <stdio.h>
int find_min(int size , int arr[]);
int find_max(int size , int arr[]);
int main(void){
    int my_array[] = {50,7,9,100,50,13,2};
    int size = sizeof(my_array)/ sizeof(int);
    int min_value = find_min(size,my_array);
    int max_value = find_max(size,my_array);
    printf("Min Value : %d ",min_value);
    printf(" Max Value : %d ",max_value);
    return 0;
}
int find_min(int size , int arr[]){
    int min = arr[0];
    for(int i = 0; i < size;i++){
        if(arr[i] < min){
            min = arr[i];
        }
    }
    return min;
}

int find_max(int size , int arr[]){
    int max = arr[0];
    for(int i =0 ; i < size ; i++){
        if(arr[i] > max){
            max = arr[i];
        }
    }
  return max;  
}
