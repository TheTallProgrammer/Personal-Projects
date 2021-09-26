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


    return 0;
}