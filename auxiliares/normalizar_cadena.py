import unicodedata

def normalizar_cadena(cadena):
    s_decomposed = unicodedata.normalize('NFD', cadena) #Normalization Form Decomposed
    s_filtered = ''.join(
        c for c in s_decomposed if unicodedata.category(c) != 'Mn') #Mn: Mark, Nonspacing
    return s_filtered.lower()
