"""Write a program to read through the mail box data and
when you find line that starts with “From”, you will split the line into
words using the split function. We are interested in who sent the
message, which is the second word on the From line."""
fname=input("enter a file name: ")
count=0
fhand=open(fname)
for line in fhand:
    if line.startswith("From:"):
        print(line.split(" ")[1])
        count=count+1
print("There were",count,"lines in the file with From as the first word")
