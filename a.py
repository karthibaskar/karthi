def main():
    a= 0
    N= int(input())
    while (N> 0):
      N = N//10
      a= a+ 1
    print (a)

if __name__ == '__main__':
    main()
