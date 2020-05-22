def main():
    votes_no = int(input("Enter the no of votes: "))
    vote_list = []
    for i in range(votes_no):
        vote_list.append(input("Enter the name of the Candidate to cast the Vote: "))
    vote = []
    for name in set(vote_list):
        vote.append((name, vote_list.count(name)))  
    vote.sort(key = lambda x : x[0] ) # sorting name lexico.
    vote.sort(key = lambda x : x[1],reverse = True) #by no. of votes
    print("The name of the candidate who won the election is", vote[0][0]) #winner
main() 

