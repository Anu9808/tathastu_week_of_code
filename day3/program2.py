from itertools import permutations
#METHOD 1 (WITH THE HELP OF ITERTOOLS MODULE)

def find_all_permutations(string):
  for i in permutations(string):
    print(''.join(i))
    
# driven code
string = input("Enter the string ")
find_all_permutations(string)
    
#METHOD 2 (WITHOUT USING ANY MODULE)

 def permutations(l):
  if len(l) ==1:
    return [l]
  return [''.join([l[i]] + list(p)) for i in range(len(l)) for p in permutations(l[:i] + l[i+1:])]
  
# driven code
string = input("Enter the string ")
print(permutations(list(string)))

