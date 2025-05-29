contato = {}

function salvar()
    io.write('Digite o nome: ')
    local nome = io.read()
    io.write('Digite o número: ')
    local numero = tonumber(io.read())
    local nomes = {nome, numero}
    table.insert(contato, nomes)
    print('Contato salvo com sucesso!\n')
    menu()
end

function listar()
    for i, v in ipairs(contato) do
        print('Nome: ' .. v[1])
        print('Numero: ' .. v[2] .. '\n')
    end
    menu()
end

function menu()
    print('*** MENU ***')
    print('1 - Salvar contato')
    print('2 - Listar contatos')
    print('3 - Encerrar')
    io.write('Digite a opção desejada: ')
    local opcao = tonumber(io.read())

    if opcao == 1 then
        salvar()
    elseif opcao == 2 then
        listar()
    elseif opcao == 3 then
        print('Encerrando o sistema!')
        os.exit()
    else
        print('Opção inválida! \nFavor digitar 1, 2 ou 3.')
        menu()
    end
end

menu()
