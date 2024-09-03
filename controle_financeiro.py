transacoes = []

transacao = {
    'data': '27/08/2024',
    'tipo': 'receita',  # ou 'despesa'
    'categoria': 'Salário',
    'valor': 1000.0
}

def adicionar_transacao(data, tipo, categoria, valor):
    transacao = {
        'data': data,
        'tipo': tipo,
        'categoria': categoria,
        'valor': valor
    }
    transacoes.append(transacao)

def calcular_saldo():
    saldo = 0
    for transacao in transacoes:
        if transacao['tipo'] == 'receita':
            saldo += transacao['valor']
        elif transacao['tipo'] == 'despesa':
            saldo -= transacao['valor']
    return saldo

def listar_transacoes():
    for transacao in transacoes:
        print(f"{transacao['data']} - {transacao['tipo']} - {transacao['categoria']} - R$ {transacao['valor']:.2f}")

def gerar_relatorio():
    print("Relatório de Transações:")
    listar_transacoes()
    print(f"Saldo Atual: R$ {calcular_saldo():.2f}")

while True:
    print("\nControle Financeiro")
    print("1. Adicionar Receita")
    print("2. Adicionar Despesa")
    print("3. Exibir Saldo")
    print("4. Listar Transações")
    print("5. Gerar Relatório")
    print("6. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        data = input("Data (DD/MM/AAAA): ")
        categoria = input("Categoria: ")
        valor = float(input("Valor: "))
        adicionar_transacao(data, 'receita', categoria, valor)
    elif opcao == '2':
        data = input("Data (DD/MM/AAAA): ")
        categoria = input("Categoria: ")
        valor = float(input("Valor: "))
        adicionar_transacao(data, 'despesa', categoria, valor)
    elif opcao == '3':
        print(f"Saldo Atual: R$ {calcular_saldo():.2f}")
    elif opcao == '4':
        listar_transacoes()
    elif opcao == '5':
        gerar_relatorio()
    elif opcao == '6':
        break
    else:
        print("Opção inválida!")

