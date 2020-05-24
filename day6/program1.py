def create_palindrome(s):
    if s==s[::-1]:
        return 0
    char={}
    for i in s:
        char[i] = char.get(i,0)+1
    list_ = sorted(alpha.values())
    odd_occ = [i for i in list_ if i%2]
    return(len(odd_occ)-1)


def main():

    str = input("Enter string ")
    print("Minimum deletions required:",create_palindrome(st1))         
    
main()
