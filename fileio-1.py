try:
    file = open('README.md')
    content = file.read()
    print(content)
finally:
    file.close()