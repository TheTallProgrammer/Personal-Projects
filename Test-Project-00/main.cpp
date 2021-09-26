//
// Created by Logan on 9/26/2021.
//

#include "main.h"

int main(int argc, char *argv[]){

    // Initializing/Declaring variables
    int n = 5;

    printTestVars();

    // Passing the address reference of the variable because the function takes a
    // memory address and dereferences it and prints the value
    printVoidPtrs(&n);

    return 0;
}