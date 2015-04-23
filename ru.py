from lxml import html

url = "http://legiao.prefeitura.unicamp.br/cardapio.php"

tree = html.parse(url)
tabs = tree.xpath('//table[@class = "fundo_cardapio"]')

almoco = tabs[0]
for x in almoco.xpath(".//td/text()")[:-4]:
    if not x.isspace():
        print(x.lstrip())
    
  

