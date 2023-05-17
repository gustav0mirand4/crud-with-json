#Importações 
import colors
import functions

#Nome do arquivo onde os produtos serão armazenados
FILE_NAME = 'dados.json'

functions.file_exists(FILE_NAME)

#Menu principal 
while True:
    functions.head("SISTEMA DE CADASTRO")
    functions.menu(['Lista de Produtos','Cadastrar Produtos','Atualizar Produtos','Remover Produtos','Sair'])    
    try: 
        option = int(input("Escolha uma opção>> "))
    except (ValueError, KeyboardInterrupt):
        colors.red("error")
    else:
        if option == 1:
            functions.product_list(FILE_NAME)
        if option == 2:
            product = functions.read(FILE_NAME)
    
            new_product = {
                "produto":"",
                "preço":0,
                "quantidade":0
            }
            for key in new_product:
                new_product[key] = input(key + ":")
            product.append(new_product)
            functions.create(product, FILE_NAME)
            colors.green('Produto cadastrado com sucesso!')
        
        if option == 3:
            functions.update(FILE_NAME)

        if option == 4:
            functions.delete(FILE_NAME)
        if option == 5:
            colors.yellow('PROGRAMA ENCERRADO')
            break 