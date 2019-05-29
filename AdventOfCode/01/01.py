//Advent of Code uloha z 2018 c.1.
// Vypocet frekvencie zo suboru pomocou algoritmu quicksort
import random
import bisect 

num = 0
sum = 0
with open("input.txt") as file:
    for line in file:
        num +=1
        line=line.strip()
        number = int(line[1:])
        if(line[0] == "+"):
            sum += number
        elif(line[0] == "-"):
            sum -= number

print(sum, " je suma")       
print("Pocet riadkov:", num)


# 2 cast -list ukolu
def quicksort(frequency_list):
    if len(frequency_list) <= 1:
        return frequency_list
    maximum = len(frequency_list) 
    pivot = random.randrange(maximum)

    smaller_than_pivot =[]
    pivot_list =[]
    bigger_than_pivot = []

    for item in frequency_list:
        if(item < pivot):
            smaller_than_pivot.append(item)
        elif(item > pivot):
            bigger_than_pivot.append(item)
        else:
            pivot_list.append(item)

    return quicksort(smaller_than_pivot) + pivot_list + quicksort(bigger_than_pivot)
def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
def binarySearch(alist,item):
    if (len(alist) == 0):
        return False
    else:
        midpoint = len(alist)//2
        print("midpoint",midpoint)
        if alist[midpoint]==item:
          print("True")
          return True
        else:
          if item<alist[midpoint]:
            return binarySearch(alist[:midpoint],item)
          else:
            return binarySearch(alist[midpoint+1:],item)

frequency_list = [0]
frequency=0

def checkLines( frequency_list,frequency):
    with open("input.txt") as file:
        for line in file:
            line = line.strip()
            number = int(line[1:])

            if(line[0] == "+"):
                frequency += number
            elif(line[0] == "-"):
                frequency -= number
            
            if( frequency_list.__contains__(frequency) == frequency):
                print("Duplicate frequency is:", frequency)
                return frequency
            else:
                bisect.insort(frequency_list,frequency)
                print("pridal som",frequency)
    checkLines( frequency_list,frequency)

frequency = checkLines( frequency_list,frequency)
print(frequency)  

"""
nekonečný cyklus:
   hodnota = radky[i % pocet_radku]
   i++
   if hodnota in slovnik:
      konec
   pridej hodnotu do slovniku
   """
