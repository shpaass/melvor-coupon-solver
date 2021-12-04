# The version where I don't optimize the item check. 
# Each roll goes linearly through the list of desired items until it fits or the list runs out.

def generate_thresholds(desired_items):
    threshold_list = []
    counter = 0
    
    for i in desired_items:
        counter += i
        threshold_list.append([counter, False])   
    
    return threshold_list

def reset_item_hits(threshold_list):
    for i in threshold_list:
        if not i[1]:
            print('threshold_list:', threshold_list)
            print('Critiacl error. Threshold is False when hit_counter says all items were hit.', \
                'Terminating the process.')
            exit()
        i[1] = False
        
    return threshold_list

import random
import statistics
import numpy

print ('\r\n Melvor Idle drop probability calculator\r\n')
print ('Starting the simulation with the parameters in the source file:')

# Probability base of the drop table. 
# On wiki, the chance is shown as a fraction and as percentage.
# The bottom number of the fraction is what needs to be entered here.
probability_base = 723

# The upper numbers of drop chances for the desired items.
# For instance, on wiki the chance can be 20/837. 20 is what you'd need to put here.
# Make the denominators of all desired items equal to probability_base before putting the numbers here.
desired_items = [3, 3, 2, 2]

# Number of trials to get the final average from.
number_of_trials = 10000

threshold_list = generate_thresholds(desired_items)

print ('Probability base:', probability_base)
print ('Desired items:', desired_items)
print ('Number of trials:', number_of_trials, '\r\n')
print ('Thresholds list:', threshold_list, '\r\n')

rng_value = 0
roll_counter = 0
hit_counter = 0
previous_threshold = 0
success_roll_numbers = []

for i in range(number_of_trials):
    while True:
        rng_value = random.uniform(0, probability_base)
        roll_counter += 1
        previous_threshold = 0
        for i in threshold_list:
            if not i[1] and rng_value < i[0] and rng_value >= previous_threshold:
                i[1] = True
                hit_counter += 1
                break
            previous_threshold = i[0]
                
        if hit_counter == len(threshold_list):
            success_roll_numbers.append(roll_counter)
            break
            
        if hit_counter > len(threshold_list):
            print('Critial error, hit_counter is', hit_counter, \
                'when the number of the desired items is', len(threshold_list), \
                '. Hit_counter should have always been less or equal.', 'Terminating the process.')
            exit()
    
    roll_counter = 0
    hit_counter = 0
    threshold_list = reset_item_hits(threshold_list)

print('The average number of rolls to hit all desired items is', statistics.mean(success_roll_numbers))
print('The median is', statistics.median(success_roll_numbers))
print('Q1:', numpy.percentile(success_roll_numbers, 25))
print('Q3:', numpy.percentile(success_roll_numbers, 75))
print('95%:', numpy.percentile(success_roll_numbers, 95))
