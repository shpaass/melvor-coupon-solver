# Melvor Idle Coupon Solver
This script calculates how many times you need to clear a dungeon to get all desired items at least once.  
It can be launched with or without command line arguments.

Arguments:

`-p, --probability-base` - The denominator (bottom number) of the drop chance. On the [wiki](https://wiki.melvoridle.com/w/Main_Page), the chance is shown as a fraction and as a percentage. The bottom number of the fraction is what needs to be entered here. Take the largest common denominator.

`-d, --desired-items` - The nominators (top numbers) of the drop chances for the desired items. For instance, the chances can be 1/17 and 3/34. You need to bring everything to common demoninator, which will be 2/34 and 3/34. In this example, `2 3` is what this argument should be.

`-n, --number-of-trials` - Number of complete item sets to acquire. Default is 10000. The larger it is, the more precise the result will be, but also the longer it will take for the program to run.

Overall, the program gets the data about the desired items with `-p` and `-d`, and then acquires them `-n` times to get the final array on which the statistics are done.

Examples of launches:
```
python coupon-solver.py
python coupon-solver.py -n 100000
python coupon-solver.py -d 3 3 2 2 -p 723
```

Initial draft by me. Testing and wrapping by Benjamin#5349.
