def main():
  for i in range(0,8):
    for j in range(0,8):
        if j==i or j ==8-(i+1):
            print('*',end='')
        else:
            print(' ',end='')
    print()
main()
