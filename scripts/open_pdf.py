# Le rag = open.pdf -> indexer -> rag -> chat_bot

import pdfplumber
from pathlib import Path  


def extraction_pages(chemin_pdf):

    """Extrait le texte d'un fichier PDF page par page.

    Reçoit "chemin_pdf", le chemin du fichier PDF à lire.

    Renvoie une liste de dictionnaires, un par page, avec les clés :
            - "numero" : le numéro de la page (à partir de 1) ;
            - "texte"  : le texte extrait de la page ;
            - "source" : le nom du document, tiré du nom du fichier (ex. "RGPD").""" 

    index = []

    source = Path(chemin_pdf).stem

    with pdfplumber.open(chemin_pdf) as pdf:
        for numero, page in enumerate(pdf.pages, start=1):
            texte = page.extract_text() 
            index.append({
                        "numero" : numero,
                        "texte" : texte,
                        "source": source,
                        })
           
    return index

def extraction_corpus(chemin_du_dossier):

    """Extrait le texte de tous les fichiers PDF d'un dossier, page par page.

    Reçoit "chemin_du_dossier", le chemin du dossier qui contient les PDF (ex. "corpus").

    Renvoie une seule liste de dictionnaires, une entrée par page, tous fichiers confondus,
    avec les mêmes clés que extraction_pages :
            - "numero" : le numéro de la page dans son document (à partir de 1) ;
            - "texte"  : le texte extrait de la page ;
            - "source" : le nom du document d'origine (ex. "RGPD", "LIL")."""
     
    pages = []

    for fichier in Path(chemin_du_dossier).glob("*.pdf"):
        page_du_fichier = extraction_pages(fichier)
        pages.extend(page_du_fichier)
        
    return pages


if __name__ == "__main__":
    resultat = extraction_corpus("corpus")
    print(len(resultat))