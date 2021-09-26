//
// Created by Logan on 9/26/2021.
//

#include "main.h"

int main(int argc, char *argv[]){

    // Creating an int variable
    int n = 5;
    // Displays the memory address of the variable
    std::cout << &n << std::endl;

    // Creating the pointer to the memory address of int n
    int *ptr = &n;

    // This displays what the variable is pointing to, which is the address of n
    std::cout << ptr << std::endl;
    // This displays the value of n, putting * in front of it dereferences it
    std::cout << *ptr << std::endl;

    // Have to dereference it in order to change the value, which also changes
    // the value that it's pointing to
    *ptr = 10;
    std::cout << ptr << std::endl;
    std::cout << n << std::endl;
    std::cout << *ptr << std::endl;



    return 0;
}