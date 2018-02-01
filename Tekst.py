from __future__ import division
import re
import json

class Summering(object):

	def splitt_setninger(self, filen):
		filen = filen.replace("\n", ". ")
		return filen.split(". ")

	def splitt_avsnitt(self, filen):
		return filen.split("\n\n")

	def kalkuler_likhet(self, set1, set2):
		s1 = set(set1.split(" "))
		s2 = set(set2.split(" "))

		return len(s1.intersection(s2)) / ((len(s1) + len(s2)) / 2)


	def formater_setning(self, setn):
		setning = re.sub(r'\W+', '', setn)
		return setning
			
	def ranger_setninger(self, filen):
  		setninger= self.splitt_setninger(filen)

  		n = len(setninger)
  		verdier = [[0 for x in range(n)] for x in range(n) ]

  		for i in range(0,n):
  			for j in range(0,n):
  				verdier[i][j] = self.kalkuler_likhet(setninger[i], setninger[j])

  		setning_lager = {}

  		for i in range(0,n):
  			score = 0
  			for j in range(0,n):
  				if (i==j):
  					continue
  				score += verdier[i][j]
  			setning_lager[self.formater_setning(setninger[i])] = score
  		return setning_lager

	def finn_beste_setning(self, avsnitt, lager):
  		setninger = self.splitt_setninger(avsnitt)

  		if(len(setninger)<2):
  			return ""

  		beste = ""
  		max_verdi = 0

  		for s in setninger:
  			strip_s = self.formater_setning(s)

  			if strip_s:
  				if lager[strip_s] > max_verdi:
  					max_verdi = lager[strip_s]
  					beste = s
  					
  		return beste

	def sammendrag(self, tittel, innhold, dic):
  		
  		paragraf = self.splitt_avsnitt(innhold)
  		#print(paragraf)
  		sammendrag = []
  		sammendrag.append(tittel.strip())
  		sammendrag.append("")

  		for p in paragraf:
  			setning = self.finn_beste_setning(p, dic).strip()
  			#print(setning)
  			if setning:
  				sammendrag.append(setning)
  		return ("\n").join(sammendrag)





sa = Summering()
#filen = open("Tekst.txt","r")
#x = filen.read()
#print(x)
lager = """

    """
dic = sa.ranger_setninger(lager)
#print(lager)
samm = sa.sammendrag("Nyhet", lager, dic)
print(samm)

fila = open("testa.txt","w") 
#fila.write(samm)#(json.dumps(lager))



