def main():
 n=int(input(""))
 temp=n
 k=0
 while(n>0):
    dig=n%10
    k=k*10+dig
    n=n//10
 if(temp==k):
    print("yes")
 else:
    print("No")

if __name__ == '__main__':
    main()

