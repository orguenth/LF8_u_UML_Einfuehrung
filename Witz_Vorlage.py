###############################################################################
#
# Klasse: Witz
# 
# Vorlage für Aufgabe
#
# Aufgabe: Einbau einer Benotung für einen Witz
#
###############################################################################

class Witz:
    
    def __init__(self, text):
        self.text = text
        
    def erzaehlen(self):
        print("Witz erzaehlen:",
              self.text)        

w = Witz("Es war ...!")

w.erzaehlen()

print()