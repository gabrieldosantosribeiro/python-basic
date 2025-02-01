# Crie uma tupla preenchida com os 10 filmes mais assistidos de todos os tempos, e depois mostre:
#
# Apenas os 3 primeiros mais assistidos
# Os últimos 2 mais assistidos
# A lista em ordem alfabética
# Em que posição está “O rei leão”

filmes = ('Avatar', 'Vingadores: Ultimato', 'Avatar: O Caminho da Água', 'Titanic', 'Star Wars: O Despertar da Força ',
          'Vingadores: Guerra Infinita', 'Homem Aranha: Sem Volta Para Casa', 'Jurassic World',
          'O Rei Leão', 'Os Vingadores')
# 3 Primeiros
for ele in range(0, 3):
    print(filmes[ele])
# 2 Últimos
for ele in range(1, 3):
    print(filmes[-ele])
# Em ordem alfabetica
print(sorted(filmes))
# O Rei Leão
pos = 1
for ele in filmes:
    if ele == 'O Rei Leão':
        print(pos)
    else:
        pos += 1