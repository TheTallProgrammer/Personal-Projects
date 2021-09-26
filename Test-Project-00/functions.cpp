//
// Created by Logan on 9/26/2021.
//

#include "functions.h"

void printTestVars(){

    std::cout << "\n====== TEST 1 ======" << std::endl;

    // Creating an int variable
    int n = 5;
    // Displays the memory address of the variable
    std::cout << "\nint n value: " << n << std::endl;
    std::cout << "&n mem address: " << &n << std::endl;

    // Creating the pointer to the memory address of int n
    int *ptr = &n;

    // This displays what the variable is pointing to, which is the address of n
    std::cout << "\nptr mem address that's pointing to n: " << ptr << std::endl;
    // This displays the value of n, putting * in front of it dereferences it
    std::cout << "defref ptr value " << *ptr << std::endl;

    // Have to dereference it in order to change the value, which also changes
    // the value that it's pointing to
    *ptr = 10;
    std::cout << "\nptr mem address after changing deref value: " << ptr << std::endl;
    std::cout << "new n value from changing the deref value of ptr: " << n << std::endl;
    std::cout << "new ptr defref value: " << *ptr << std::endl;

    // Can also make a pointer that holds a value, doesn't have to be set to
    // a variable
    // Sometimes it does though, because it needs an address to go off of, so
    // we'd use a variable to make an address for the pointer to use
    int v;
    int *ptr2 = &v;
    std::cout << "\nptr2 mem address: " << ptr2 << std::endl;
    std::cout << "deref ptr2 value w/ nothing assigned yet: " << *ptr2 << std::endl;

    // Dereference it and assign it a value
    *ptr2 = 20;
    std::cout << "\nptr2 mem address w/ value assigned: " << ptr2 << std::endl;
    std::cout << "ptr2 deref w/ new value assigned: " << *ptr2 << std::endl;

} // End of printTestVars()

void printVoidPtrs(int *numPtr){

    std::cout << "\n====== TEST 2 ======" << std::endl;

    std::cout << *numPtr << std::endl;

} // End of printVoidPtrs()