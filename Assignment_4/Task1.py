file_name= "sample.txt"
try:
    with open(file_name,'r') as file:
        reading_file=file.readlines()
        for i in reading_file:
            print(i)
except Exception as e:
    print(f"The file {file_name} was not found")