with open('README.md','w') as file:
    file.write("Hello, Pythonista!")
try:
    file = open('README.md')
    content = file.read()
    print(content)
finally:
    file.close()
