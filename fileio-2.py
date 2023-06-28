f = open("README.md", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("README.md", "r")
print(f.read())