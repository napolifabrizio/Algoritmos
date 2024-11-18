

voted = {}

def verify(name: str):
    if voted.get(name):
        print('Mande embora!')
    else:
        voted[name] = True
        print("Deixa votar!")

verify("Pedro")
verify("Mari")
verify("Pedro")
