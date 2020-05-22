def main():
  votes_no = int(input("Enter the no of votes: "))
  vote_list = {}
  for i in range(votes_no):
      name = input("Enter the name of the Candidate ")
      if name not in vote_list:
          vote_list[name] = 1
      else:
          vote_list[name] += 1
  name_li = sorted(vote_list,key = lambda k:k[1],reverse = True)
  name_li.sort()
  print("The name of the candidate who won the election is", name_li[0])
  
main()
