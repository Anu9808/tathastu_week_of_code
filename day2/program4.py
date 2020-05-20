def main():
    l=[]
    for i in range(1,6):
        l.append((' '*(2*i)).center(12,'*'))
    for i in l:  
        print(i)
    for i in reversed(l):
        print(i)
main()
