from sys import argv
script,textfile=argv
text=open(textfile,'a+')
line1="hello"
line2="good morning"
line3="goodbye"
text.write(line1)
text.write("\n")
text.write(line2)
text.write("\n")
text.write(line3)
text.write("\n")
text.seek(0,0)
print text.read()
text.close()
