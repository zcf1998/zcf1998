from sys import argv
script,textfile1,textfile2=argv #put textfile1 into textfile2
text1=open(textfile1)
s=text1.read()
text1.close()
text2=open(textfile2,'w')
text2.write(s)
text2.close()
