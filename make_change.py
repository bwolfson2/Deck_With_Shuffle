#!/bin/python3

"""
Inputs:
	denominations: list of coin denominations 
	n: the desired amount of money 
Output:
	Ways to make n:  the number of ways to make the 

The function runs using dynamic programming. Specifically, make_change take advantage of the fact that given an array N consisting of
N_1_k..N_{m}_{k}...N_{m+1}_{k}...N_n_k, each representing the number of ways to get change for m, using denominations D_1...D_k
adding a new denomination D_{k+1} follows the update rule:
if m == D_{k+1}:
	N_m_{k+1} =  N_m_{k+1} + 1, i.e. there is one new way to get to the value of the denomination
else for m > D_{k+1}:
	N_m_{k+1} = N_{m}_k + N_{m-D_{k+1}}, i.e. the new number of ways to get to m is the old number of ways to get to m 
	added to the number of ways to get to the N_{m-D_{k+1}}

"""

import sys
import itertools as it
def make_change(denominations, n):
    #for visualization/debugging:
    #denominations.sort()

    #NArray N
    ways_to_reach_n = list(it.repeat(0,n+1))
    #Loop through array D
    for denomination in denominations:
        #Update values in N
        for i in range(denomination,n+1):
            if i == denomination:
                ways_to_reach_n[i] =ways_to_reach_n[i]+ 1
            else:
                ways_to_reach_n[i] = ways_to_reach_n[i-denomination]+ways_to_reach_n[i]
    #Return number of ways to get change for n
    return ways_to_reach_n[n]
        
