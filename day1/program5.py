p1 = int(input("enter score of first player "))
p2 = int(input("enter score of second player "))
p3 = int(input("enter score of third player "))

print("strike rate of first player", p1*100/60)
print("strike rate of second player", p2*100/60)
print("strike rate of third player", p3*100/60)

print("Runs score if they played 60 balls more by first player",p1*2)
print("Runs score if they played 60 balls more by second player",p2*2)
print("Runs score if they played 60 balls more by third player",p3*2)

print("maximum number of sixes first player could have",p1//6)
print("maximum number of sixes second player could have",p2//6)
print("maximum number of sixes third player could have",p3//6)
