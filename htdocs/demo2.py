#!C:/BioWeb/python.exe
# coding: utf-8
import cgi

print("Content-type:text/html;charset=utf-8\r\n\r\n")

form = cgi.FieldStorage()
dna = form.getvalue("dna","Unknown")

DNA = dna.upper()
count = {"A":0,"T":0,"G":0,"C":0}
for i in ["A","T","G","C"]:
    count[i] = DNA.count(i)

print("<pre>")
for i in ["A","T","G","C"]:
    print("{}: {}".format(i,count[i]))
print("</pre>")