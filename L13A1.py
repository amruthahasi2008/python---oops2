# Algorithm Analysis
# Part 1 - set n = 4 rounds
#In the game Round 1 = 1 , 2 = 2 and n = n
# We will solve find the total in 3 ways and count the step each one takes
n = 4
print("-----counting game point(n,", n , "rounds)")
print()

# part 2 
#Algorithm : Use the shortcut formulae to get the answer instantly
#Pseudocode : total = n*(n+1)/2
#Time complexity : 1 step
# Space complexity : 1 variable
total = n*(n+1)/2
print("formula way : total ",total,"1 step")

#part 3
# Algorithm : add each round's point one by one using a loop 
# psedocode : for round from 1 to n : total = total+ round
# Time complexity: n steps
#space complexity : 2 variables

total = 0
steps = 0
for round_num in range(1,n+1) :
    total += round_num
    steps += 1
print("loop way ",total,"steps : 2 steps")

# part 4
# Algorithm : add each round's point one by one using a loop 
# psedocode : for round from 1 to n : for point from one to round total = total+ 1
# Time complexity: n *n steps
#space complexity : 3  variables

total = 0
steps = 0
for round_num in range(1,n+1) :
    for point in range(1,round_num + 1) :
        total += 1
        steps += 1
print("loop way ",total,"steps : 3 steps")

# part 5
 # try n = 10 and see what happens to steps 
n = 10
nested_steps = 0
for round_num in range(1,n+1) :
    for point in range(1,round_num + 1) :
        nested_steps+=1
        print()
print("=== Now with n =", n, "rounds ===")
print(" way : steps = 1 (always just 1!)")
print("Loop way : steps =", n)
print("Nested loop : steps =", nested_steps, "(grows much faster!)")
print()
print("Same answer — but very different costs. That is time complexity!")








