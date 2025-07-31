dict={
    "Saurav":85,
    "Sanjay":97,
    "Gaurav":76,
    "Akash":87
}
try:
    Name=input("Enter the student's name: ")
    print(f"{Name}'s marks: ",dict[Name])
except:
    print(f"{Name} is not a valid student name")