"""
Digit factorial chains
Problem 74

The number 145 is well known for the property that the sum of the factorial of its 
digits is equal to 145:

1! + 4! + 5! = 1 + 24 + 120 = 145

Perhaps less well known is 169, in that it produces the longest chain of numbers that link back to 169;
 it turns out that there are only three such loops that exist:

169 → 363601 → 1454 → 169
871 → 45361 → 871
872 → 45362 → 872

It is not difficult to prove that EVERY starting number will eventually get stuck in a loop. For example,

69 → 363600 → 1454 → 169 → 363601 (→ 1454)
78 → 45360 → 871 → 45361 (→ 871)
540 → 145 (→ 145)

Starting with 69 produces a chain of five non-repeating terms, but the longest non-repeating chain 
with a starting number below one million is sixty terms.

How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?
"""
import math
def sumfact(x):
    out=0
    for char in str(x):
        out+=math.factorial(int(char))
    return out
    
def stepstorepeat(x):
    i=1
    results=[x]
    current=sumfact(x)
    while current not in results:
        #print("results is:",results,"and current is:",current)
        results.append(current)
        i+=1
        current=sumfact(current)
    #print("the term",current,"appeared in spot#",i)
    #print (x,"had",i,"unique terms before repeating")
    return i
    
def findbig(maximum):
    i=1
    count=0
    out=[]
    while i<maximum:
        if i%(10**4)==0:
            print("passing through i being",i)
        if stepstorepeat(i)>59:
            count+=1
            out.append(i)
        i+=1
    print("there are",len(out),"nums below",maximum,"that took 60 steps:",out)
    return i
    
findbig(10**6) #--> 402 CORRECT