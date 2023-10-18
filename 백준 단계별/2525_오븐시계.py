def main():
    A, B = map(int, input().split())
    C = int(input())
    if B+C>=60:
        h = (B+C)//60
        print((A+h)%24, (B+C)%60)
    else:
        print(A, B+C)

if __name__=='__main__':
    main()