num='15'                                                                #input 1
array = "1 2 3 4 5 6 7 8 9 10 89 21 27 98 56 23 12 23 43 98 198 22210"  #input 2
array = [int(i) for i in array.split()]                                 #convert to list in integer
num = int(num)                                                          #cast integer

sm = sum(array)                                                         #Find sum
#print("sum is",sm)
print("result is",int(sm/num)+1)                                        #final result
