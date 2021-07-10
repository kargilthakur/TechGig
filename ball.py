''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def isprime(num):
    flag = False
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                flag = True
                break
        return flag

def main():

 # Write code here 
 i = int(input())
 l = input().split()
 moves=0
 for k in range(0,i):
     y=int(l[k])
     x=int(l[k])
     if x == 1:
         moves = moves + 1
     while(x>1):
        for j in range(2,int((x/2)+1)):
            print(x)
            if x == 1:
                break
            elif isprime(int(x))==False:
                moves=moves+y
                x=1
            elif x%j==0:
                if x == y:
                    x=(x/j)
                    moves = moves + 1
                else:
                    x=(x/j)
                    moves = moves + (y/x) 
            print("move count",moves)          
        # moves = moves + y
 return moves
res=main()
print(res)

