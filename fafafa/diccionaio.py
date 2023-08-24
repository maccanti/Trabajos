Sapo=dict = {
"SAPO1":("Sapo","sApo"),
"SAPO2":("saPo","sapO"),
"SAPO3":("SApo","SAPo")
}
print(Sapo.get("SAPO1"),("Sapo","sApo"))
print(Sapo["SAPO1"])
print(Sapo.keys())
print(Sapo.values())
valor_elim=Sapo.pop("SAPO1",("Sapo","sApo"))
print(valor_elim)
