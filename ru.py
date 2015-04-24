import itertools as it

from lxml import html


url = "http://legiao.prefeitura.unicamp.br/cardapio.php"

tree = html.parse(url)
tabs = tree.xpath('//table[@class = "fundo_cardapio"]')

listas = []
for periodo in tabs:
    listas.append([])
    l = listas[-1]
    for x in periodo.xpath(".//td[not(strong='Observações:')]/text()"):
        if not x.isspace():
            l.append(x.lstrip())

linhas = it.zip_longest(*listas, fillvalue='')
fills_v = [max(map(len, x)) + 3 for x in listas]
str_formato = "{0[0]:{0[1]}} {1[0]:{1[1]}} {2[0]:{2[1]}}"
tabela = '\n'.join(str_formato.format(*zip(x, fills_v)) for x in linhas)
print(tabela)
    
  

