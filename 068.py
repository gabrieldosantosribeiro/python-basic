# Escreva um programa que crie um dicionário com as informações de 5 livros,
# como título, autor, ano de lançamento e número de páginas.
# Em seguida, exiba apenas os autores dos livros.

livros = {'1984': ['George Orwell', '328 páginas', 'Publicado em 1949.'],
          'Cem Anos de Solidão': ['Gabriel García Márquez', '417 páginas', 'Publicado em 1967.'],
          'O Senhor dos Anéis: A Sociedade do Anel': ['J.R.R. Tolkien', '576 páginas', 'Publicado em 1954.'],
          'Harry Potter e a Pedra Filosofal': ['J.K. Rowling', '223 páginas', 'Publicado em 1997.'],
          'O Código Da Vinci': ['Dan Brown', '592 páginas', 'Publicado em 2003.']}

for ele in livros:
    print(livros[ele][0])
