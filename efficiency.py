import time #needed for later


# Project euler problem 5 is:
#      2520 is the smallest number that can be divided by
#      each of the numbers from 1 to 10 without any remainder.
#      What is the smallest positive number that is evenly
#      divisible by all of the numbers from 1 to 20?
# (https://projecteuler.net/problem=5)

# Here is one way to solve the problem:
# 1.  guess that the answer is n
# 2a. Check if guess is divisible by 1.
# 2b. Check if guess is divisible by 2.
# 2... Keep checking for divisibility until reaching n
# 3a. If at any point guess is not divisble, increase guess
#     by 1, go back to step 2.a
# 3b. If guess is divisble up to n, return guess.

# The following function follows the above algorithm:
def euler5(n):
    guess = n
    max_divisor = 1
    while max_divisor <= n:
        if guess % max_divisor == 0:
            max_divisor+= 1
        else:
            guess+= 1
            max_divisor = 1
    return guess
#answer = euler5(10)
#print("euler5(10): ", answer)

#==================================================
# Problem 0

# We want to be able to discuss how long this function takes to run.
# We can measure this in time, or in number of loop iterations.
# Let us start with loop iterations

# Below is the euler5 function, modify it such that before it ends
# it prints out the total number of loops needed to get the answer.

def euler5_loop_count(n):
    guess = n
    max_divisor = 1

    while max_divisor <= n:

        if guess % max_divisor == 0:
            max_divisor+= 1
        else:
            guess+= 1
            max_divisor = 1

    return guess
# To test, use this, it should take 25 loops to get the answer
# which is 12
answer = euler5_loop_count(4)
print("euler5(4): ", answer)

# End Problem 0
#==================================================

#==================================================
# Problem 1

# We can also talk about how long a fucntion takes measured in seconds.
# time.time() will return the number of seconds since 1/1/1970. This is
# known as EPOCH time.

# Below are 2 calls to euler5_loop_count. Add code above and below
# each call to display the number of seconds taken to run each.

print("Timing slow version:")

# YOUR CODE HERE

answer = euler5_loop_count(10)
# YOUR CODE HERE

print("elapsed time: ")
print("euler5(10): ", answer)


print("Second slow version test:")
#YOUR CODE HERE

answer = euler5_loop_count(10)
#YOUR CODE HERE

print("elapsed time: ")
print("answer euler5(20): ", answer)

# End Problem 1
#==================================================


#==================================================
# Problem 2

# Hopefully, you noticed that the loop count and time to
# get the answer for 20 were both quite large.

# Now we can look at the algorithm from the begining and
# ask ourselves: can we make it faster?

# Below is a copy of euler_5_loop_count, first, add
# the code to count and print the number of loops from
# Problem 0

# Then, try to decrease the number of loops run.
# Think about what you need to do each time to
# have to reset your guess. Can you make it better?

# An initial goal should be to get the loop count for
# 20 down to 416,181,955.

# But eventually, you should be able to get the loop count
# for 20 down to 51,473,642.
def euler5_better(n):
    guess = n
    max_divisor = 1

    while max_divisor <= n:

        if guess % max_divisor == 0:
            max_divisor+= 1
        else:
            guess+= 1
            max_divisor = 1

    return guess

print("\nBetter version:")
# Dont forget to include time code as well
# YOUR CODE HERE

answer = euler5_better(20)
# YOUR CODE HERE
print("elapsed time: ")
print("answer euler5(20): ", answer)


#==================================================
# An advanced approach

# Perhaps the number above is not good enough for you.
# Well, try this on for size!

# This function will find the least common multiple of
# 2 integers.
def lcm(max_divisor, guess):
    m = guess
    while m % max_divisor != 0:
        m+= guess
    return m

# Can you use this to make your solution for euler5
# even better?
# Write a new version, and test it, measuring
# both time and loop counts.
# To keep track of loop counts, you may need
# to consolodate the lcm function into your main
# euler5 function.





# End advanced approach
#==================================================
