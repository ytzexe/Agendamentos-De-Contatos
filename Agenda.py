# Aqui criamos uma lista, para salvar o nome e contatos propostos e uma funçao para salvar.
contato=[]
def salvar():
    nome = input('Digite o nome: ')
    numero = int(input('Digite o número: '))
    nomes = (nome, numero)
    contato.append(nomes)
    print('Contato salvo com sucesso!\n\n')
    menu()
#Criamos uma funçao para listar os contatos salvos     
def listar():
    for nome, numero in contato:
        print(f'Nome: {nome}')
        print(f'Numero: {numero}\n\n')
    menu()


#Aqui esta a nossa funçao do menu, para lista algum contato, salvar ou encerrar 
def menu():
    
    print('*** MENU ***')
    print('1 - Salvar contato')
    print('2 - Listar contatos')
    print('3 - Encerrar')
    opcao = int(input('Digite a opção desejada: ')) 
    if opcao == 1:
        salvar()
    elif opcao == 2:
        listar()
    elif opcao == 3:
        print('Encerrando o sistema!')
        exit()
    else:
        print('Opção inválida! \n Favor digitar 1, 2 ou 3.')

menu()
