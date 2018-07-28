textfile=raw_input("please input filename\n")
text=open(textfile)
print "The content of %s:"%textfile
print text.read()
text.close()
