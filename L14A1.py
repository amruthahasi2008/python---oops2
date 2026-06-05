#--- SCORE TRACKER---
# Topic - Asymtotic Analysis| Big - O | Omega| Theta
# Part 1 
# Five players and their scores . We will run three operations and classify each one with formal asymptotic notation
names = ["Aarav","Priya","Dev","Meera","Kabir"]
scores =[90,75,88,62,95]
n = len(scores)
print("--- Score Tracker (n=",n,"players)---")
for i in range (n):
    print(i+1,".",names[i],":",scores[i],sep = "")
print()

#Part 2 - theta 1 
# get the score at position 0 : always exactly 1 step
# best case = worst case = exactly 1
# the cost never changes no matter how many players are there
steps = 1
print("Score at index 0 : ",scores[0],"|steps",steps,"|Theta (1)- tight bound")
print()

# part :3 O(n) 
# search for a name by scanning from the very start
#Omega(1) best case : name is at position 1 step.
#O(n) worst case : name is at position n-1, found after n steps
target = "Aarav"
steps = 0
for name in names :
    steps +=1
    if name == target :
        break
print("search for",target,"|steps=",steps,"|O(n)=",n,"worst case upper bound")
#part 4 : o(n^2)
#compare every player  against every other player
#Asymptotic Anaylysis : actual steps = n*n-1/2
# Dominant term after dropping constants 
steps = 0
target_sum = 150
print("pairs with total score = ",target_sum)
for i in range(n) :
    for j in range (i+1,n):
        steps +=1
    if scores[i] + scores[j] == target_sum :
        print(" ",names[i],"+",names[j],"=",scores[i]+scores[j])
print()


