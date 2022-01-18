"""Creo la clase findpal para que cuente las palabrasque aparecen en una frase"""

class FindPal:
    def __init__(self, archivo_palabras, archivo_frases):
        ap = open(archivo_palabras, "r")
        self.palabras = {}
        for linea in ap:
            self.palabras[linea.strip()] = []
        ap.close()

        af = open(archivo_frases, "r")
        self.frases = []
        for linea in af:
            self.frases.append(linea.strip())
        af.close()


    def encuentra_palabras(self):

        palabras = self.palabras
        frases = self.frases
        for pal in palabras:
            for f in frases:
                palabras[pal].append(f.lower().count(pal))
        return palabras