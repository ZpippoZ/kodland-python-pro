meme_dict = {
    "LOL": "una risposta a qualcosa di divertente",
    "CRINGE": "qualcosa di strano o imbarazzante",
    "SHEESH": "leggera disapprovazione",
    "CREEPY": "spaventoso, inquietante",
    "CHILL": "tranquillo",
    "SNITCH": "spia",
    "SNITCHARE": "fare la spia",
    "BOOMER": "generalmente 40-50 anni o più, persone che hanno difficoltà ad usare le \"tecnologie moderne\"" 
}

print("Ciao boomer, benvenuto!")

for i in range(5):
    word = input("Scrivi un neologismo che non conosci\n").upper()
    print(meme_dict[word]) if word in meme_dict.keys() else print("O non esiste, o non è nel nostro dizionario. Sorry!")
    
print("bye bye boomer")
