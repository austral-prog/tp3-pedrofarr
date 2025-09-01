
nombre = input("Pedro")


nombre = nombre.lower()

vocales = ["a", "e", "i", "o", "u"]


for v in vocales:
    print(f"Contiene {v}: {v in nombre}")
