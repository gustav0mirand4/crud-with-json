#Modulos da funções
import json 
from pathlib import Path
import colors

#Função para leitura de uma arquivo
def read(file):
    with open(file, 'r') as json_file:
        data = json.load(json_file)
        return data
    
#Função de cadastro dos produtos    
def create(product, file):
    with open(file, 'w') as json_file:
        json.dump(product, json_file, indent=4)

#Verificando se o arquivo existe
def file_exists(file):
    json_file = Path(file)
    if json_file.exists() == False:
        json_file.touch()
        dados = []
        with open(file, 'w') as file_:
            dados = json.dump(dados, file_)
            from colors import green
            green('Arquivo criado com sucesso!')

def product_list(file):
    date = read(file)
    if date == []:
        print("Nenhum produto cadastrado")
    count = 0   
    for x in date:
        print(f"{count} - {x['produto']:<18} R$:{x['preço']:<5} UN:{x['quantidade']}")
        count += 1

def update(file_):
    product_list(file_)
    try:
        products = read(file_)
        update_product = int(input("Escolha um produto da lista para alterar>> "))
    except (ValueError, KeyboardInterrupt):
        colors.red("Opção Invalida")
    else:
        menu(['Alterar nome do roduto','Alterar preço do prouto','Alterar quantidade do produto'])
        option_update_product = int(input("Escolha uma opção [NOME|PREÇO|QUANTIDADE]>> "))
        if option_update_product == 1:
            new_name_product = input("Novo nome>> ")
            products[update_product]['produto'] = new_name_product
            colors.green('Nome do produto alterado com sucesso!')
            create(products, file_)

        if option_update_product == 2:
            new_name_product = input("Novo preço>> ")
            products[update_product]['preço'] = new_name_product
            colors.green('Preço do produto alterado com sucesso!')
            create(products, file_)
        
        if option_update_product == 1:
            new_name_product = input("Nova quantidade>> ")
            products[update_product]['quantidade'] = new_name_product
            colors.green('Quantidade do produto alterado com sucesso!')
            create(products, file_)

        else:
            print("opção invalida")

def delete(file):
    product_list(file)
    product = read(file)
    remove_product = int(input("Escolha o produto que deseja remover>> "))
    del product[remove_product]
    create(product, file)
    colors.green("Produto removido com sucesso!")

#Linhas 
def line():
    print('-'*45)

#Cabeçalho
def head(txt):
    line()
    print(txt.center(45))
    line()

#Lista de itens para o menu
def menu(list):
    c = 1
    for item in list:
        print(f"{c} - {item}")
        c += 1
    line()
