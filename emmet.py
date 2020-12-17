# Author : Andalis, Ariane Jane J.
# Course and Year : BS Information Technology, 2nd year
# Filename : emmet.py
# Description : The main emmet file which contains the process in order for an html tag to be converted in an expanded code.
# Honor Code : I have not given nor received any unathorized help in
# completing this exercise. I am also well aware of the
# policies stipulated in the AdNU student handbook.

import re

class Emmet:
	def __init__(self,raw):
	
		self.raw = raw
		
	def emmet_process(self):
			emmet_string = self.raw.split("+") #splits the string if it encounters the + character.
			storage = " "
			
			for tag in emmet_string:
			
				while re.findall("<ul|li", tag): #re.findall returns a list containing all matches
					return("Error: Unrecognized abbreviation\n")
				if ">" not in tag:
					storage = ("<{}> \n</{}> \n".format(tag, tag))
				else:
					tab_list = tag.split(">")
					begin_search = ["\t"*tag + "<" + x + ">" + "\n" for tag, x in enumerate(tab_list)]
					end_search = ["\t"*tag + "</" + x + ">" + "\n" for tag, x in enumerate(tab_list)]
					
				#returns an iterator that accesses the given sequence in reverse order.
					begin_search.extend(reversed(end_search))
					storage += " ".join(begin_search)		
				expandedversion = storage	
					
			return(expandedversion)
			
	def __str__(self):
		return self.emmet_process()
		
w = Emmet("div>nav>p")
print(w.raw)

w = Emmet("div>nav>p>span")
print(w)

w = Emmet("div+nav+p+span")
print(w)

w = Emmet("div>nav+p>span")
print(w)

w = Emmet("div>div+div>nav>p+p>span")
print(w)

w = Emmet("ul<li")
print(w)
w = Emmet("ul<li")
print(w)
