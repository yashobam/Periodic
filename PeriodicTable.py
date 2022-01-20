class PeriodicTable:

	def __init__(self):
		elementsymbols="""H	He	Li	Be	B	C	N	O	F	Ne	Na	Mg	Al	Si	P	S	Cl	Ar	K	Ca	Sc	Ti	V	Cr	Mn	Fe	Co	Ni	Cu	Zn	Ga	Ge	As	Se	Br	Kr	Rb	Sr	Y	Zr	Nb	Mo	Tc	Ru	Rh	Pd	Ag	Cd	In	Sn	Sb	Te	I	Xe	Cs	Ba	La	Ce	Pr	Nd	Pm	Sm	Eu	Gd	Tb	Dy	Ho	Er	Tm	Yb	Lu	Hf	Ta	W	Re	Os	Ir	Pt	Au	Hg	Tl	Pb	Bi	Po	At	Rn	Fr	Ra	Ac	Th	Pa	U	Np	Pu	Am	Cm	Bk	Cf	Es	Fm	Md	No	Lr	Rf	Db	Sg	Bh	Hs	Mt	Ds	Rg	Cn	Uut	Fl	Uup	Lv	Uus	Uuo"""
		elementnames="""Hydrogen	Helium	Lithium	Beryllium	Boron	Carbon	Nitrogen	Oxygen	Fluorine	Neon	Sodium	Magnesium	Aluminium	Silicon	Phosphorus	Sulfur	Chlorine	Argon	Potassium	Calcium	Scandium	Titanium	Vanadium	Chromium	Manganese	Iron	Cobalt	Nickel	Copper	Zinc	Gallium	Germanium	Arsenic	Selenium	Bromine	Krypton	Rubidium	Strontium	Yttrium	Zirconium	Niobium	Molybdenum	Technetium	Ruthenium	Rhodium	Palladium	Silver	Cadmium	Indium	Tin	Antimony	Tellurium	Iodine	Xenon	Caesium	Barium	Lanthanum	Cerium	Praseodymium	Neodymium	Promethium	Samarium	Europium	Gadolinium	Terbium	Dysprosium	Holmium	Erbium	Thulium	Ytterbium	Lutetium	Hafnium	Tantalum	Tungsten	Rhenium	Osmium	Iridium	Platinum	Gold	Mercury	Thallium	Lead	Bismuth	Polonium	Astatine	Radon	Francium	Radium	Actinium	Thorium	Protactinium	Uranium	Neptunium	Plutonium	Americium	Curium	Berkelium	Californium	Einsteinium	Fermium	Mendelevium	Nobelium	Lawrencium	Rutherfordium	Dubnium	Seaborgium	Bohrium	Hassium	Meitnerium	Darmstadtium	Roentgenium	Copernicium	Ununtrium	Flerovium	Ununpentium	Livermorium	Ununseptium	Ununoctium"""
		elesymb=elementsymbols.split("\t")
		elenames=elementnames.split("\t")
		self.Elements={}
		for i in range(len(elesymb)):
			self.Elements[elesymb[i]]=elenames[i]

	def NameToElement(self,word,path="",paths=[],eles=[],elelist=[]):
		if word=="":
			paths+=[path]
			elelist+=[eles]
		else:
			for i in range(1,4):
				if len(word)>i and word[:i].title() in self.Elements:
					self.NameToElement(word[i:], path+word[:i].title(), paths, eles+[self.Elements[word[:i].title()]], elelist)
				elif len(word)==i and word.title() in self.Elements:
					self.NameToElement("", path+word.title(), paths, eles+[self.Elements[word.title()]], elelist)
		return paths,elelist

	def NotPossible(self,word):
		elelist=[]
		path=""
		i=0
		while i < len(word):
			for j in range(3,0,-1):
				if i+j-1<len(word) and word[i:i+j].title() in self.Elements:
					path+=word[i:i+j].title()
					elelist+=[self.Elements[word[i:i+j].title()]]
					i+=j-1
					break
			i+=1

		path=[path]
		elelist=[elelist]

		return path,elelist


def run(word):
	PT=PeriodicTable()
	word.lower()
	words=word.split(" ")
	Names=[]
	Elements=[]
	print(words)
	for i in range(len(words)):
		NameList,ElementList=PT.NameToElement(words[i],"",[],[],[])

		if NameList==[]:
			NameList,ElementList=PT.NotPossible(words[i])
		Names+=[NameList]
		Elements+=[ElementList]
	for i in AllPaths(Names):
		print("Words In Symbols: ",end="")
		for j in range(len(words)):
			print(Names[j][i[j]],end=" ")
		print("\n"+"Words in Elements: ",end="")
		for j in range(len(words)):
			for k in Elements[j][i[j]]:
				print(k,end=" ")
		print()



def AllPaths(Names,index=0,paths=[],path=[]):
	if len(Names)==index:
		paths+=[path]
	else:
		for i in range(len(Names[index])):
			AllPaths(Names,index+1,paths,path+[i])
	return(paths)
#PT=PeriodicTable()
#print(PT.NameToElement('patrick'))


run("yashobam")

