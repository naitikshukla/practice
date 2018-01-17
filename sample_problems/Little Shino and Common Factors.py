def gcd(a,b):
     
    # Everything divides 0 
    if (a == 0 or b == 0):
            False
    # base case
    if (a == b):
        return a
 
    # a is greater
    if (a > b):
        return gcd(a-b, b)
    return gcd(a, b-a)

# Write your code here
n = input()                         # Reading input from STDIN , for hackerearth
l3,l4 = [int(i) for i in n.split()] #extracting integer numbers
num = gcd(max(l3,l4),min(l3,l4))    #
count = 0                           #initializing counter
for i in range(1,round(num**(1.0/2)):     #starting loop
    if num%i==0:                     #checking first condition if satisfies then only enters
      #if l4%i==0:                   #if previous true then check this for divident 0
      count += 1                  #if both true increment the counter
print(count)                        #print the result


'''
Sample Input : "10 15"
Sample Output : "2" (because of 1 and 5)
'''
