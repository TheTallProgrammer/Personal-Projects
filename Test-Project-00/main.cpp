//
// Created by Logan on 9/26/2021.
//

#include "main.h"

int main(int argc, char *argv[]){

    printTestVars();

    // Initializing/Declaring variables
    int n = 5;
    char letter = 'a';

    // Passing the address of the variable because the function takes a
    // memory address and dereferences it and prints the value
    printVoidPtrs(&n,'i');
    printVoidPtrs(&letter,'c');

    printArray();

    int numbers[5] = {4,3,-4,54,5};
    int min = numbers[0];
    int max = numbers[0];
    getMinAndMax(numbers, 5, &min, &max);

    printDynamArray();

    return 0;
}