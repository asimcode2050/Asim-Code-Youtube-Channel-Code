#include <stdio.h>
#include <string.h>

int main(void)
{
    const char *string ="This is a test";
    char char_search = 'k';
    if(strchr(string,char_search)!=NULL){
        printf("\'%c\' was found in \"%s\".\n",char_search,string);

    }
    else{
        printf("\'%c\' was not found", char_search);
    }
}
