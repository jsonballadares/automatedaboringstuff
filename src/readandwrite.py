hello_file = open("data/hello.txt")
content = hello_file.readlines()
print(content)
hello_file.close()

hello_file = open("data/hello2.txt", 'w')
hello_file.write("Hello!")
hello_file.write("Hello!")
hello_file.write("Hello!")
hello_file.write("Hello!")
hello_file.close()