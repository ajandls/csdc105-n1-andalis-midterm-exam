# Author : Andalis, Ariane Jane J.
# Course and Year : BS Information Technology, 2nd year
# Filename : test.py
# Description : The file that accepts input from the command-line and prints and expanded html code.
# Honor Code : I have not given nor received any unathorized help in
# completing this exercise. I am also well aware of the
# policies stipulated in the AdNU student handbook.

from emmet import Emmet

while True:

	html_tags = input()
	
	if html_tags == "quit" or html_tags == "exit":
		break
	else:
		w = Emmet(html_tags)
		print(w)
