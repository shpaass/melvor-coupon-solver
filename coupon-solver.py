# The version that can be launched as a file with parameters.

import random
import statistics
import numpy
import argparse

def generate_thresholds(desired_items):
    threshold_list = []
    cum_wgt = 0
    
    for wgt in desired_items:
        cum_wgt += wgt
        threshold_list.append([cum_wgt, False])   
    
    return threshold_list

def reset_item_hits(threshold_list):
    for e in threshold_list:
        if not e[1]:
            print('threshold_list:', threshold_list)
            print('Critiacl error. Threshold is False when hit_counter says all items were hit.', \
                'Terminating the process.')
            exit()
        e[1] = False
        
    return threshold_list

def roll_all_items(wgt_list, total_wgt, number_of_trials=10000):
    threshold_list = generate_thresholds(wgt_list)
    success_roll_numbers = []

    for i in range(number_of_trials):
        hit_counter = 0
        roll_counter = 0
        while hit_counter < len(threshold_list):
            rng_value = random.uniform(0, total_wgt)
            roll_counter += 1
            prev_item_th = 0
            for item in threshold_list:
                if not item[1] and rng_value < item[0] and rng_value >= prev_item_th:
                    item[1] = True
                    hit_counter += 1
                    break
                prev_item_th = item[0]
                    
        success_roll_numbers.append(roll_counter)
        threshold_list = reset_item_hits(threshold_list)

    return success_roll_numbers


if __name__ == '__main__':
    # Probability base of the drop table. 
    # On wiki, the chance is shown as a fraction and as percentage.
    # The bottom number of the fraction is what needs to be entered here.
    probability_base = 723

    # The upper numbers of drop chances for the desired items.
    # For instance, on wiki the chance can be 20/837. 20 is what you'd need to put here.
    # Make the denominators of all desired items equal to probability_base before putting the numbers here.
    desired_items = [3,3,2,2]

    # Number of times to acquire the whole set of desired items. 
    # We get the final statistics from the array that will be as long as this number.
    number_of_trials = 10000

    example_text = '''examples:
    python coupon-solver.py
    python coupon-solver.py -n 100000
    python coupon-solver.py -d 3 3 2 2 -p 723'''

    parser = argparse.ArgumentParser(epilog=example_text, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-n', '--number-of-trials', default=number_of_trials, type=int)
    parser.add_argument('-d', '--desired-items', nargs='+', default=desired_items, type=int)
    parser.add_argument('-p', '--probability-base', default=probability_base, type=int)
    args = parser.parse_args()

    print ('\r\n Melvor Idle coupon solver\r\n')
    print ('Starting the simulation with the parameters in the source file:')

    print ('Probability base:', args.probability_base)
    print ('Desired items:', args.desired_items)
    print ('Number of trials:', args.number_of_trials, '\r\n')

    success_roll_numbers = roll_all_items(args.desired_items, args.probability_base, args.number_of_trials)

    print('The average number of rolls to hit all desired items is', statistics.mean(success_roll_numbers))
    print('The median is', statistics.median(success_roll_numbers))
    print('Q1:', numpy.percentile(success_roll_numbers, 25))
    print('Q3:', numpy.percentile(success_roll_numbers, 75))
    print('95%:', numpy.percentile(success_roll_numbers, 95))
