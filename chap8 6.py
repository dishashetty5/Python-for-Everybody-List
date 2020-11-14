"""Rewrite the program that prompts the user for a list of
numbers and prints out the maximum and minimum of the numbers at
the end when the user enters “done”. Write the program to store the
numbers the user enters in a list and use the max() and min() functions to
compute the maximum and minimum numbers after the loop completes."""
a=[]
while True:
    n=input("enter the number: ")
    try:
        n=int(n)
        a.append(n)
    except:
        if n== "done":
            break
        else:
            print("Invalid input")
print(max(a),min(a))
