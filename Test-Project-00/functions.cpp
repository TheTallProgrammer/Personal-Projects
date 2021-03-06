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


// Points to the address of whatever is passed into the function
// Can't directly dereference it
void printVoidPtrs(void *ptr, char type){

    std::cout << "\n====== TEST 2 ======" << std::endl;

    switch (type) {

        // Handles int pointers
        case 'i':

            // This casts the passed in void ptr and makes it an int pointer
            // The * in the front deferences it as well to get the value
            std::cout << *((int*)ptr) << std::endl;

            break;

        case 'c': // Handle char pointers

            std::cout << *((char*)ptr) << std::endl;
            break;

    } // End of switch()

} // End of printVoidPtrs()


void printArray(){

    std::cout << "\n====== TEST 3 ======" << std::endl;

    // An array is a natural pointer
    int numbers[5] = {3,4,1,7,5};

    // This prints out the address of the first element in the array
    std::cout << "Address of array: " << numbers << std::endl;

    // This prints out the value of the first element in the array
    std::cout << "Value of element 1: " << numbers[0] << std::endl;

    // This also prints out the value of the first element, but in pointer notation
    std::cout << "Value of element 1: " << *(numbers + 0) << std::endl;


} // End of printArrayAdd()


// Finds the min/max value of elements in an array
void getMinAndMax(int numbers[], int size, int *min, int *max){

    std::cout << "\n====== TEST 4 ======" << std::endl;
    std::cout << "Elements: ";
    for (int i =0; i < size; i++){

        // Prints all elements on the same line
        std::cout << numbers[i] << ", ";

        if(numbers[i] > *max){

            *max = numbers[i];

        } else if (numbers[i] < *min){

            *min = numbers[i];

        }
    }

    std::cout << "\nThe size of the array is: " << size << std::endl;
    std::cout << "The min value is: " << *min << std::endl;
    std::cout << "The max value is: " << *max << std::endl;

} // End of getMinAndMax()


void printDynamArray(){

    std::cout << "\n====== TEST 5 ======" << std::endl;

    int size = 5;

    // The 'new' key word allocates, or gives memory that represents 'size'
    // or array size of 5, to the pointer myArray. At the moment, myArray is
    // pointing to the first element in the arrays address,
    // like in test printArray() or test 3. Once you allocate, you have to deallocate
    int *myArray = new int[size];

    for (int i = 0; i < size; i++){
        myArray[i] = i;
    }

    for (int i = 0; i < size; i++){
        std::cout << myArray[i]; // array notation
//        std::cout << *(myArray+i); pointer notation
    }

    // keyword 'delete' de-allocates memory of the array, making it point
    // to a random location in memory
    delete[]myArray;

    // This points array to nothing instead of random memory
    myArray = NULL;

}