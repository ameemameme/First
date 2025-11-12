print("Unwelcome Abode")
print()
print("If it is in bracket & capitalised, type it inside quotes")
print("If it is in bracket just do what it says")
print("Make new terminal and type; git clone (your repository URL code)")
print("git status")
print("cd (FOLDER NAME)")
print("git add (FILE NAME)")
print("git commit -m (FILE NAME added)")
print("git push origin main")
print()
horizontal=int(input("Enter a value for horizontal:"))
vertical=int(input("Enter a value for vertical:"))
for i in range(horizontal):
    for j in range (vertical):
        if j==0 or i==0:
            print("*",end=" ")
    print()
