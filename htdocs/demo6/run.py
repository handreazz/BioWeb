#!C:/BioWeb/python.exe
# -*- coding=utf-8 -*-
import cgi
print("Content-type:text/html\r\n\r\n")
form = cgi.FieldStorage() 
#保留上几行就对了

DNA = form.getvalue('dna')


complementary_DNA = {
	'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C', 'N': 'N'
} #碱基互补配对的字典

transcription = {
	'T': 'U'
} #转录的字典

reverse_transcription = {
	'A': 'T', 'U': 'A', 'C': 'G', 'G': 'C', 'N': 'N'
} #反转录的字典

RNA_codon_Table = {
#	Second Base
#		U			C			 A			G
# U
	'UUU': 'F', 'UCU': 'S', 'UAU': 'Y', 'UGU': 'C', # UxU
	'UUC': 'F', 'UCC': 'S', 'UAC': 'Y', 'UGC': 'C', # UxC
	'UUA': 'L', 'UCA': 'S', 'UAA': '---', 'UGA': '---', # UxA
	'UUG': 'L', 'UCG': 'S', 'UAG': '---', 'UGG': 'W', # UxG
# C
	'CUU': 'L', 'CCU': 'P', 'CAU': 'H', 'CGU': 'R', # CxU
	'CUC': 'L', 'CCC': 'P', 'CAC': 'H', 'CGC': 'R', # CxC
	'CUA': 'L', 'CCA': 'P', 'CAA': 'Q', 'CGA': 'R', # CxA
	'CUG': 'L', 'CCG': 'P', 'CAG': 'Q', 'CGG': 'R', # CxG
# A
	'AUU': 'I', 'ACU': 'T', 'AAU': 'N', 'AGU': 'S', # AxU
	'AUC': 'I', 'ACC': 'T', 'AAC': 'N', 'AGC': 'S', # AxC
	'AUA': 'I', 'ACA': 'T', 'AAA': 'K', 'AGA': 'R', # AxA
	'AUG': 'M', 'ACG': 'T', 'AAG': 'K', 'AGG': 'R', # AxG
# G
	'GUU': 'V', 'GCU': 'A', 'GAU': 'D', 'GGU': 'G', # GxU
	'GUC': 'V', 'GCC': 'A', 'GAC': 'D', 'GGC': 'G', # GxC
	'GUA': 'V', 'GCA': 'A', 'GAA': 'E', 'GGA': 'G', # GxA
	'GUG': 'V', 'GCG': 'A', 'GAG': 'E', 'GGG': 'G', # GxG
#compressed
	'GCN': 'A', 'CGN': 'R', 'MGR': 'R', 'AAY': 'N',
	'GAY': 'D', 'UGY': 'C', 'CAR': 'Q', 'GAR': 'E',
	'GGN': 'G', 'CAY': 'H', 'AUH': 'I', 'YUR': 'L', 'CUN': 'L',
	'AAR': 'K', 'UUY': 'F', 'CCN': 'P', 'UCN': 'S', 'AGY': 'S',
	'ACN': 'T', 'UAY': 'Y', 'GUN': 'V', 'UAR': '---', 'URA': '---'
} #氨基酸密码子表的字典

degenerate_bases = {
	'Y':'C', 'K':'G', 'W':'A',
	'A':'A', 'U':'U', 'C':'C', 'G':'G',
	'S':'S', 'M':'M', 'R':'R', 'B':'B',
	'D':'D', 'H':'H', 'V':'V', 'N':'N', 'T':'U'
} #某些简并碱基的转换字典

pair_base = {
	'A': 'U', 'U': 'A', 'C': 'G', 'G': 'C', 'N': 'N'
} #RNA碱基互补配对字典


#构建一些函数用于处理序列
def dnainfo(seq):
	length  = len(seq) #输出序列长度
	countG = seq.count('G')
	countC = seq.count('C')
	countT = seq.count('T')
	countA = seq.count('A')
	GC_content = float(countC + countG) / length #GC含量计算
	AT_content = float(countA + countT) / length
	ATGC_ratio = float(countA + countT) / (countC + countG) #AT/CG�?
	GC_skew = float(countG-countC) / (countG + countC) #GC偏移
	AT_skew = float(countA-countT) / (countA + countT)
	print("<p>Length: " + str(length) + '</p>') #输出的结果是带html标签�?
	print("<p>GC content: " + str(float('%0.2f'%(GC_content * 100))) + "%" + '</p>')
	print("<p>GC skew: " + str(float('%0.2f'%(GC_skew * 100))) + "%" + '</p>')
	print("<p>AT/GC ratio: " + str(float('%0.2f'%(ATGC_ratio))) + '</p>')

def rnainfo(seq):
	length  = len(seq)
	print("<p>Length: " + str(length) + '</p>')
	if 'AUG' in seq:
		print("<p>This sequence has start codons.</p>")
	else :
		print("<p>This sequence has no start codons.</p>")
	cDNA = ''
	for i in range(len(seq)):
		cDNA += reverse_transcription[seq[i]]
	print("<p>cDNA: " + cDNA + "</p>")

def comp(seq):
	comp_seq = ''
	for i in range(len(seq)):
		comp_seq += complementary_DNA[seq[i]]
	print("<p>Complementary chain: " + comp_seq + '</p>')

def read_frame(target_seq, frame):
	if frame == 1:
		return target_seq
	if frame == 2:
		return target_seq[1:len(target_seq)]
	if frame == 3:
		return target_seq[2:len(target_seq)]

def translate(seq_frame):
	met = seq_frame.find('M')
	stop = seq_frame.find('---')
	prot = ''

	for i in range(0, len(seq_frame) - (len(seq_frame) % 3), 3):
		codon = seq_frame[i:i+3]
		try :
			prot += RNA_codon_Table[codon]
		except :
			prot += "X"
	return prot

def highlight(prot):
	a = prot.split('---')
	output = ''
	for i in range(len(a)):
		M = a[i].find('M')
		if i < (len(a)-2):
			if M == -1:
				output += a[i] + '---'
			else :
				output += a[i][:M] + '<span style="background-color: #F5A2A3">' + a[i][M:] + '</span>---'
		elif i == (len(a)-2):
			if M == -1:
				output += a[i] + '---'
			else :
				output += a[i][:M] + '<span style="background-color: #F5A2A3">' + a[i][M:] + '</span>---'
		else:
			if M == -1:
				output += a[i]
			else :
				output += a[i][:M] + '<span style="background-color: #F5A2A3">' + a[i][M:] + '</span>'
	return output

input_seq = DNA
seq = input_seq.upper()

for i in range(len(seq)):
	if (not (seq[i] == 'A' or seq[i] == 'T' or seq[i] == 'C' or seq[i] == 'G' or seq[i] == 'U')) :
		print("Error!\n")
		raise SystemExit(1)
if ('T' in seq and 'U' in seq): #判断是不是DNA
	print("Error!\n")
	raise SystemExit(1)
print('<h3>' + seq + '</h3>')
if (not 'U' in seq and 'T' in seq):
	seqtype = 'DNA'
	DNA = seq
	print('<p>Sequence type: ' + seqtype + '</p>')
	dnainfo(DNA)
	comp(DNA)
	
if (not 'T' in seq and 'U' in seq): #判断是不是RNA
	seqtype = 'RNA'
	RNA = seq
	print('<p>Sequence type: ' + seqtype + '</p>')
	rnainfo(RNA)
	if 'AUG' in seq:
		obvseq = ''
		revseq = ''
		for i in range(len(seq)):
			obvseq += degenerate_bases[seq[i]]
		revseq_ = obvseq[::-1]
		for i in range(len(revseq_)):
			revseq += pair_base[revseq_[i]]

		f1 = read_frame(obvseq, 1)
		f2 = read_frame(obvseq, 2)
		f3 = read_frame(obvseq, 3)
		f4 = read_frame(revseq, 1)
		f5 = read_frame(revseq, 2)
		f6 = read_frame(revseq, 3)
		prot1 = translate(f1)
		prot2 = translate(f2)
		prot3 = translate(f3)
		prot4 = translate(f4)
		prot5 = translate(f5)
		prot6 = translate(f6)
		print('<p>Possible amino acid sequences(<a href="http://en.wikipedia.org/wiki/Open_reading_frame">Open reading frames</a> are highlighted in <span style="background-color: #F5A2A3"> red</span>.): </p>')
		print(r"<p>5'-3' Frame1: " + highlight(prot1) + "</p>")
		print(r"<p>5'-3' Frame2: " + highlight(prot2) + "</p>")
		print(r"<p>5'-3' Frame3: " + highlight(prot3) + "</p>")
		print(r"<p>3'-5' Frame1: " + highlight(prot4) + "</p>")
		print(r"<p>3'-5' Frame2: " + highlight(prot5) + "</p>")
		print(r"<p>3'-5' Frame3: " + highlight(prot6) + "</p>")
	else :
		print("<p>Possible amino acid sequences: No</p>")
if (not ('T' in seq or 'U' in seq)):
	seqtype = 'Either'
	print('<p>Sequence type: ' + seqtype + '</p>')
	length  = len(seq)
	countG = seq.count('G')
	countC = seq.count('C')
	countT = seq.count('T')
	countA = seq.count('A')
	countU = seq.count('U')
	GC_content = float(countC + countG) / float(length)
	AT_content = float(countA + countT) / float(length)
	ATGC_ratio = float(countA + countT) / float(countC + countG)
	GC_skew = float(countG-countC) / float(countG + countC)
	AT_skew = float(countA-countT) / float(countA + countT)
	print("<p>Length: " + str(length) + '</p>')
	print("<p>GC content: " + str(float('%0.2f'%(GC_content * 100))) + "%" + '</p>')
	print("<p>GC skew: " + str(float('%0.2f'%(GC_skew * 100))) + "%" + '</p>')	
print("Analysis Done")


