file_name="output.txt"
with open(file_name,'a') as file:
    file_input=input("Enter the text to be written in file: ")
    file.write(file_input)
    print(f"Data successfully written to {file_name}:")
    file.write("\n")
    file_input_2=input("Enter additional text to be written in file: ")
    file.write(file_input_2)

with open(file_name,'r') as file2:
    print(f"Final content of {file_name}:")
    print(file2.read())