# Melvor Idle Coupon Solver
This script calculates how many times you need to clear a dungeon to get all desired items at least once.  
It can be launched with or without command line arguments.

Arguments:

`-p, --probability-base` - On [wiki](https://wiki.melvoridle.com/w/Main_Page), the chance is shown as a fraction and as a percentage. The bottom number of the fraction is what needs to be entered here.

`-d, --desired-items` - The upper numbers of drop chances for the desired items. For instance, on wiki the chance can be 20/837. 20 is what you need to put here. Make the denominators of all desired items equal to probability_base before putting the numbers here.

`-n, --number-of-trials` - Number of complete item sets to acquire. Default is 10000.

Examples of launches:
```
python coupon-solver.py
python coupon-solver.py -n 100000
python coupon-solver.py -d 3 3 2 2 -p 723
```

Initial draft by vbion. Testing and wrapping by Benjamin#5349.
