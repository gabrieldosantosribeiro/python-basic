# Crie um programa que leia uma frase e mostre:
# Quantas vezes aparece a letra “a”
# Em que posição ela aparece a primeira vez
# Em que posição ela aparece na última vez

# ler a frase
frase = input('digite uma frase: ').strip()
# Quantidade de 'a'
print(frase.count('a'))
# primeira vez
primeira = frase.find('a')
print(primeira)
# última vez
ultima = frase.rfind('a')
print(ultima)


