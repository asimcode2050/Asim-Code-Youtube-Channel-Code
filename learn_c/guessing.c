#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int main() {
    int number, guess, attempts = 0;
    srand(time(0));
    number = rand() % 100 + 1;
    printf("Welcome to the Guessing Game!\n");
    printf("I have selected a random number between 1 and 100.\n");
    printf("Your goal is to guess the number in as few attempts as possible.\n");
    do {
        printf("\nEnter your guess: ");
        scanf("%d", &guess);
        attempts++;
        if (guess > number) {
            printf("Too high! Try again.\n");
        } 
        else if (guess < number) {
            printf("Too low! Try again.\n");
        } 
        else {
            printf("Congratulations! You guessed the number in %d attempts!\n", attempts);
        }

    } while (guess != number);

    return 0;
}
