// https://youtu.be/VB4PDR8w6J8
#include <cstddef>
#include <cstdio>

int main(){

    unsigned long max = 0;
    unsigned long values[] = {10,0,40,12,100,80,200};
    for(size_t i =0; i < 7; i++ ){
        if (values[i] > max){
            max = values[i];
        }

    }
    printf("Max value is %lu", max);
    return 0;

}
