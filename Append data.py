text=input("enter the text to write to the file: ")
with open("output,txt","w")as file:
    file.write(text+"\n")
print("data succesfully written to output.txt.")
extra_txt=input("enter additional text to append: ")
with open("output.txt","a")as file:
    file.write(extra_txt +"\n")
print("data successfully appended.")
print("\nFinal content of output.txt: ")
with open("output.txt","r") as file:
    for line in file:
        print(line.strip())