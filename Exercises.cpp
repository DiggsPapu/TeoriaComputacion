/**
 * @file Exercises.cpp
 * @author Diego Andres Alonzo Medinilla (alo20172@uvg.edu.gt) 20172
 * @brief Ejercicios de lab 8 de la teoria de la computacion
 * @version 0.1
 * @date 2023-10-06
 * 
 * @copyright Copyright (c) 2023
 * 
 */
#include <iostream>
#include <cstdlib>
#include <fstream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <list>

void ex1(int n){
    int i, j , k, counter = 0;
    for (i = n/2; i <= n; i++){
        for (j=1; j+n/2<= n; j++ ){
            for (k = 1; k <= n; k = k*2){
                counter++;
            }
        }
    }
}

void ex2(int n){
    if (n>1) {
        int i, j;
        for (i = 1; i <= n; i++){
            for (j = 1; j <= n; j++){
                printf("Sequence");
                break;
            }
        }
    }
}

void ex3(int n){
    int i, j;
    for (i = 1; i <= n/3; i++){
        for (j = 1; j <= n; j+=4){
            printf("Sequence\n");
        }
    }
}
int main(){
    for (int l = 0; l<7; l++){
        ex1(10^l);
    }
}