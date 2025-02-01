# Escreva um programa que crie um dicionário com as informações de 5 países,
# como nome, capital,  população e idioma oficial.
# Em seguida,  permita que o usuário digite o nome de um país e exiba suas informações.
try:
    pais = {'brasil': ['Brasília, 212 milhões, Português'],
            'japão': ['Tóquio, 127 milhões, Japonês'],
            'estados unidos': ['Washington, 331,9 milhões, inglês'],
            'espanha': ['Madrid, 47,42 milhões, espanhol'],
            'lisboa': ['Moscou, 10,33 milhões, português ']}

    print(pais[input('digite o país: ').strip().lower()])
except KeyError:
    print('País não cadastrado.')
