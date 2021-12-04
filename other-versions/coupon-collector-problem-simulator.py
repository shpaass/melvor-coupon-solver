# The version where I solve the coupon collector problem as if only the desired items can drop.
# The probability ratios are saved. The sum of probabilities for the desired items is 1.
# After I get data on this problem, I multiply it by how many tries on average it would take 
#  to hit that probability pool in the actual drop table.

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
import time

print ('\r\n The simulator of coupon collector problem for Melvor Idle\r\n')
print ('Starting the simulation with the parameters in the source file:')

# Probability base of the drop table. 
# On wiki, the chance is shown as a fraction and as percentage.
# The bottom number of the fraction is what needs to be entered here.
probability_base = 723

# The upper numbers of drop chances for the desired items. All natural numbers.
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
success_roll_numbers = []

for i in range(number_of_trials):
    while True:
        rng_value = random.uniform(0, threshold_list[-1][0])
        roll_counter += 1
        for i in threshold_list:
            if not i[1] and rng_value < i[0]:
                i[1] = True
                hit_counter += 1
                break
        if hit_counter == len(threshold_list):
            success_roll_numbers.append(roll_counter)
            break
            
        if hit_counter > len(threshold_list):
            print('Critial error, hit_counter is', hit_counter, \
                'when the number of the desired items is', len(threshold_list), \
                '. Hit_counter should have always been less.', 'Terminating the process.')
            exit()
    
    roll_counter = 0
    hit_counter = 0
    threshold_list = reset_item_hits(threshold_list)
    
adjusted_success_roll_numbers = [i * probability_base * 1.0 / sum(desired_items) for i in success_roll_numbers]

print('The average number of rolls to hit all desired items is', statistics.mean(adjusted_success_roll_numbers))
print('The median and quartiles are wrong because we scale the result on a much larger interval, but they are here if you need them.')
print('The median is', statistics.median(adjusted_success_roll_numbers))
print('Q1:', numpy.percentile(adjusted_success_roll_numbers, 25))
print('Q3:', numpy.percentile(adjusted_success_roll_numbers, 75))
