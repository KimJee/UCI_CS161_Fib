import time;
import numpy as np;
import matplotlib.pyplot as plt;


# Table to store data of size n for already done values
fib_table = [None]*1000000;


# Time results for recusive
simple_time = [];
# Time Results for top_down_memoized_fib
top_down_time = [];
# Time Results for bottom_up_memoized_iter_fib()
bottom_up_time = [];

def main():
    
    n = int(30);
    for count in range(n):        
        past = time.time()
        
        # Recursive Fibannaci without memoization
        result = basic_fib(n)
        print("basic_fib() => " + str(result))

        present = time.time()
        print("basic_fib() => Time Taken (in s): " + str((present-past)) + "\n")
        
        simple_time.append(present-past);
        
        # With Top-Down memoization being used
        past = time.time()
        # Our default known values
        fib_table[0] = 0
        fib_table[1] = 1
        result = top_down_memoized_fib(n)
        print("top_down_memoized_fib() => " + str(result))
        present = time.time()
        print("top_down_memoized_fib() => Time Taken (in s): " + str((present-past)) + "\n")
        
        top_down_time.append(present-past);
        fib_table[:n] = [0]*n;
        
        #Bottom-Up approach
        past = time.time()    
        result = bottom_up_memoized_iter_fib(n)
        print("bottom_up_memoized_iter_fib() => " + str(result))
        present = time.time()
        print("bottom_up_memoized_iter_fib() => Time Taken (in s): " + str((present-past)) + "\n")
        
        bottom_up_time.append(present-past);
    # End of the data-gathering function
        
    # Stats
    plt.semilogy();
    plt.plot(simple_time, 'y');
    plt.plot(top_down_time, 'r');
    plt.plot(bottom_up_time, 'b');
    # X-axis (I think there's a function for this but whatever
    # x_axis = [0, n, 0, 0.001];
    # plt.axis(x_axis);
    plt.show();
    
def basic_fib(n):
    if (n == 0):
        return 0;
    if (n == 1):
        return 1;
    return basic_fib(n-1) + basic_fib(n-2);


# Top-down approach to the memoized_fib table
# By starting from top-down, there are still unnecessary calls being done (10 -> {9, 8) ==> so on)
# However, once the calculation is done at least once on any level, it is reused by other levels

def top_down_memoized_fib(n):
    #print(fib_table);
    # Calculate fib
    if (fib_table[n] == None):
        # Calculate the fibinacci based on previous array values
        fib_table[n] = top_down_memoized_fib(n-1) + top_down_memoized_fib(n-2)
    return fib_table[n]

""" Analysis:
        If we've already solved the problem, then it costs O(1)
        Otherwise Fib(i) gets called at most 2-times for each i
        
        Everytime 7 gets called
            1) Does the calculation
            2) Does the look up
            3) Never-happens because by that time the N+1 is already done!

    When I approach a problem, DRAW A DAG (WHY DID I NOT THINK OF THIS BEFORE?) 
"""

# Could you do a top_down_memoized_iterative_fib()

def bottom_up_memoized_iter_fib(n):
    if (n == 0 or n == 1):
        return n;
    a = 0;
    b = 1;
    
    for i in range(1, n):
        c = a + b
        a = b
        b = c
    return c;

if __name__ == "__main__":
    main()
