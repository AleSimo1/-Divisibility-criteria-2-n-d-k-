from collections import Counter
import matplotlib.pyplot as plt

#Boolean function that checks that an element is inside a list
def is_in(n, list):
    return n in list

#Boolean function that checks that a list is contained in one another
def is_in_l(list1, list2):
    count_list1 = Counter(list1)
    count_list2 = Counter(list2)
    return all(value <= count_list2.get(key, 0) for key, value in count_list1.items()) 

#Function that decomposes a number and inserts the decomposed elements into a list
def scompo(n):
    conta = 2
    scompo = []
    while conta <= n:
        if(n%conta == 0):
            n /= conta
            scompo.append(conta)
        else:
            conta += 1
    
    return scompo

#Boolean function that tells us if a number is boolean or not
def primo(n):
    primo = True
    if n > 1:
        for i in range(2, n):
            if (n % i == 0):
                primo = False
    
    return primo

#Function that prints a list
def stampa(list):
    print(list)

#Function that makes the difference between two lists
def diff(list1, list2):
    c1 = Counter(list1)
    c2 = Counter(list2)

    list_diff = c2-c1
    
    return list(list_diff.elements())


#Main
#Goal: to find a value of n, which is used in the equation 2^n -1, 
# which after executing the equation and decomposing the result has 
# elements of the decomposition d and the rest of the elements are equal to k
# 2^n -1 = d * k

#Definition of variables
d = 1
fattx = []
fattd = []
diffl = []
saved = []
saven = []
#Run numbers (in my pc the highest number was 27, for more powerful pc it can be increased)
while(d<=27):
    n = 1
    #Variable of type bool that identifies us when we have found a number n that reaches the goal
    ok = False
    while(ok != True):
        #Calculation of the equation
        x = pow(2,n)-1
        #List cleaning
        fattx.clear()
        fattd.clear()
        diffl.clear()
        if(not primo(x)):
            fattx = scompo(x)
        
        if(not primo(d)):
            fattd = scompo(d)
        #First print
        if(x == d):
            k = 1
            print("Con n = " + str(n) + " d = " + str(d) + " k = " + str(k))
            saven.append(n)
            saved.append(d)
            #Found
            ok = True
        #Second print
        elif(is_in(d, fattx) and not primo(x) and primo(d)):
            print("Con n = " + str(n) + " d = " + str(d) + " k = ", end='')
            saven.append(n)
            saved.append(d)
            for i in fattx:
                if(i != d):
                    print(str(i) + " ", end='')
            
            print()
            #Found
            ok = True
        #Third print
        elif(is_in_l(fattd, fattx) and not primo(x) and not primo(d)):
            print("Con n = " + str(n), " d = " + str(d) + " k = ",  end='')
            saven.append(n)
            saved.append(d)
            diffl = diff(fattd, fattx)
            for i in diffl:
                print(str(i) + " ", end='')
            
            print()
            #Found
            ok = True
        else: 
            #Not Found, increase n 
            n +=1

    #Increase d for running again
    d += 2


#Lines of code that allow you to print the results inside a graph
saven.append(28)
saved.append(29)

saven.append(5)
saved.append(31)

saven.append(10)
saved.append(33)

saven.append(12)
saved.append(35)
plt.plot(saved, saven, marker = "o", color = 'red')
plt.grid()
plt.title("Grafico")
plt.xlabel("D")
plt.ylabel("N")
plt.xticks(saved)
plt.yticks(saven)
#plt.minorticks_on() #Serve per avere più tick lungo gli assi
plt.show()