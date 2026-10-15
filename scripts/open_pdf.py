# Le rag = open.pdf -> indexer -> rag -> chat_bot

import pdfplumber

#-----------Le open pdf------------- 

def extraction_pages(chemin_pdf):

    """Cette fonction recoit le numéro de la page et renvoie l'article qui correspond""" 

    index = []

    with pdfplumber.open(chemin_pdf) as pdf:
            for numero, page in enumerate(pdf.pages, start=1):
                texte = page.extract_text() 
                index.append({
                            "numero" : numero,
                            "texte" : texte,
                            })
           
    return index

if __name__ == "__main__":
    fichier_pdf = "/home/leonard/Documents/CODE/Projets/GDPR_AUDIT_V2/corpus/CELEX_32016R0679_FR_TXT.pdf"
    resultat =  extraction_pages(fichier_pdf)
    print(resultat[35]["texte"])