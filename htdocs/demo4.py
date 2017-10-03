#!C:/BioWeb/python.exe
# coding: utf-8
import cgi
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

print("Content-type:text/html;charset=utf-8\r\n\r\n")

#第一步：获得用户的输入
DNA = cgi.FieldStorage().getvalue('dna',"ATGGCCATT")#从用户提交的表单中得到<input name="dna">的值，复制给DNA这个变量，如果用户没有输入(你在IDLE中测试)，就会得到后面那个字符串
#如果你修改了HTML中的input的name，这里也要相应修改getvalue的参数

#第二步：调用BioPython这个库来转录翻译
coding_dna = Seq(DNA, IUPAC.unambiguous_dna) #Biopython的方法，变为可以转录的DNA类型，例子：ATGGCCATT
messenger_rna = coding_dna.transcribe()#把转录的模板的T变为U就是mRNA咯，例子：AUGGCCAUU
translation_protein = messenger_rna.translate()#翻译，请百度“密码子表”和“氨基酸缩写”，例子：MAI （甲硫氨酸、丙氨酸、异亮氨酸）

#现在我们已经把所有的东西都计算好了，来输出给用户吧~
#第三步：向用户输出，print就是咯
print("<pre>")#有没有想到为啥用个pre呢
print("%-35s %s" % ("Your input is:",DNA))#这里用了参数化的print，表示用空格自动补全为35个字符长度
print("%-35s %s" % ("mRNA is:",messenger_rna))
print ("%-35s %s" % ("Translation:",translation_protein))
print("</pre>")

