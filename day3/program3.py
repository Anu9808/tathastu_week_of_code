string = input("Enter the string ")
duplicate = set()
new=''

for i in string:
    if i not in duplicate:
        duplicate.add(i)
        new+=i
    else:
        continue
print("string without duplicate characters".format(new))
