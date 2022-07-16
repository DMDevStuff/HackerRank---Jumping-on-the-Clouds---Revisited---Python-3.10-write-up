##    https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited/problem
##
##    Visit link above for official problem description

##### ##### ##### #####

#   renamed input variables:

#   c => cloud_list
#   k => move_size

##### ##### ##### #####

#   O(n)
#   n is the length of cloud_list
#   Algo:
#       1. initalize variables to keep track of energy levels
#           and list index => O(1)
#       2. loop through the given cloud_list with steps of size move_size => O(n)
#           lower the energy level for each step by 1 => O(1)
#           if cloud_list[index] = 1, lower the energy level by an additional 2 => O(1)
#           when current_index = 0, return energy level => O(1)

#   Notes on loop termination:
#       while loop chosen over for loop for readability
#       n = length of cloud_list
#       if n mod(move_size) is zero, we will reach index zero
#       again after one pass and terminate the loop
#       if n mod(move_size) is not zero, then we will end up touching each
#       element of cloud_list before returning to index zero.
#       giving us at worst O(n)

def jumpingOnClouds(cloud_list, move_size):
    
    energy_remaining = 100
    current_index = 0
    
    while True:
        
        current_index = (current_index + move_size) % len(cloud_list)
        energy_remaining -= 1
        
        if cloud_list[current_index] == 1:
            
            energy_remaining -= 2
            
        if current_index == 0:
            
            return energy_remaining
