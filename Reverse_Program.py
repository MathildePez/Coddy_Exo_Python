def reverse(w):

    if len(w) <= 1:
        return w
    else:
        return reverse(w[1:]) + w[0]

while True:
    
    text = input("Ecris quelque chose ('bye' pour stopper le programme) : ")
    if text.lower() == 'bye':
        print("B Y E")
        break
    result = reverse(text)
    print("Résultat inversé : ", result)
