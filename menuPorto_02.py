# Carolina Estevam Rodgerio 554975
# Enrico Andrade D’Amico 557706
# Vinicius Prates Altafini 559183

# Variáveis para armazenar dados do usuário
nome = ""
senha = ""
email = ""
cpf = ""
planoDeContratacao = ""
cep = ""
carro = []  # Lista para armazenar dados do carro: [ano, modelo, cor, placa]
descricao_problema = ""

# Função para mostrar o menu estilizado


def mostrar_menu():
    print("\n===========MENU============")
    print("1. Iniciar Chat")
    print("2. Mecânicas perto da minha casa")
    print("3. Alterar Dados")
    print("4. Alterar Plano")
    print("5. Ver Dados")
    print("6. Encerrar Sessão")
    print("=============================")


# Preenchimento do cadastro do usuário
print("=== Cadastro ===")
nome = input("Nome: ")
email = input("E-mail: ")

while True:
    cpf = input("O seu CPF (apenas números): ")
    if len(cpf) != 11:
        print("CPF inválido. Digite apenas números (11 números).")
    else:
        break

cpf_formatado = '{}.{}.{}-{}'.format(cpf[:3], cpf[3:6], cpf[6:9], cpf[9:])

while True:
    cep = input("cep (apenas números): ")
    if len(cep) != 8:
        print("CEP inválido. Digite apenas números (8 números).")
    else:
        break

cep_formatado = '{}-{}'.format(cep[:5], cep[5:])

senha = input("Senha: ")

planoDeContratacao = int(input(
    "Nível de Plano Atual: \n(1) Plano A\n(2) Plano B\n(3) Plano C\nEscolha: "))
while planoDeContratacao not in [1, 2, 3]:
    print("\nOpção inválida. Digite apenas uma das opções do menu.")
    planoDeContratacao = int(input(
        "\nNível de Plano Atual: \n(1) Plano A\n(2) Plano B\n(3) Plano C\nEscolha: "))
if planoDeContratacao == 1:
    planoDeContratacao = "Plano A"
elif planoDeContratacao == 2:
    planoDeContratacao = "Plano B"
elif planoDeContratacao == 3:
    planoDeContratacao = "Plano C"

carro.append(input("Placa do veículo: "))
carro.append(input("Ano do veículo: "))
carro.append(input("Modelo do veículo: "))
carro.append(input("Cor do veículo: "))

print("\n****** Cadastro realizado com sucesso! ******\n")

# Loop principal do programa
while True:
    mostrar_menu()
    escolha = input("Escolha uma opção: ")

    # Verifica se a opção é válida
    if escolha not in ['1', '2', '3', '4', '5', '6']:
        print("\nOpção inválida. Digite apenas uma das opções do menu.")

    # Opção 1: Iniciar Chat
    if escolha == "1":
        print("\n*** Iniciando Chat... ***")
        print("Olá, eu sou a inteligência artificial da Porto Seguro :)")
        print("\nEscolha uma das opções abaixo para darmos continuidade:)")
        print("\n(1) Descrever o meu Problema")
        print("(2) Descobrir Possível Problema")

        while True:
            op = input("\nEscolha: ")
            if op == "1":
                descricao_problema = input(
                    "Descreva brevemente o seu problema: ")
                while True:
                    alterar = input(
                        "\nDeseja alterar o texto? (1) Sim (2) Não: ")
                    if alterar == "1":
                        print(descricao_problema)
                        descricao_problema = input("\nAlterar: ")
                    elif alterar == "2":
                        print("\nProblema descrito com sucesso!")
                        break
                    else:
                        print("Opção inválida. Por favor, escolha novamente.")
                break  # Sair do loop após a descrição do problema
            elif op == "2":
                print(
                    "\nRedirecionando para nosso chatbot para descobrir possível problema...")
                break  # Sair do loop se a escolha for válida
            else:
                print("Opção inválida. Por favor, escolha novamente.")
                print("(1) Descrever Problema")
                print("(2) Descobrir Possível Problema")

    # Opção 2: Mecânicas perto da minha casa
    elif escolha == "2":
        print("\n*** Mecânicas próximas ***")
        print("Mecânica (1) ☆☆☆ a 1km")
        print("Mecânica (2) ☆☆☆☆ a 2km")
        print("Mecânica (3) ☆☆☆☆☆ a 5km")

        mec = int(input("\nEscolha a mecânica: "))
        descricao_problema = input(
            "\n>Agora Descreva brevemente o seu problema: ")

        while True:
            alterar = input("Deseja alterar o texto? (1) Sim (2) Não: ")
            if alterar == "1":
                descricao_problema = input(
                    ">Descreva brevemente o seu problema: ")
            elif alterar == "2":
                break
            else:
                print("Opção inválida. Por favor, escolha novamente.")

        if mec == 1:
            print("\n>>>>Mecânica 1 escolhida.")
            print("\nVocê receberá mais informações no email cadastrado: ", email)
        elif mec == 2:
            print("\n>>>>Mecânica 2 escolhida.")
            print("\nVocê receberá mais informações no email cadastrado: ", email)
        elif mec == 3:
            print("\n>>>>Mecânica 3 escolhida.")
            print("\nVocê receberá mais informações no email cadastrado: ", email)

    # Opção 3: Mudar Dados
    elif escolha == "3":
        print("\n*** Alterar Dados ***")
        opcao_dados = input(
            "O que você deseja alterar?\n(1) Nome\n(2) Email\n(3) CPF\n(4) CEP\n(5) Senha\n(6) Dados do Veículo\nEscolha: ")
        if opcao_dados == "1":
            nome = input("Novo Nome: ")
        elif opcao_dados == "2":
            email = input("Novo E-mail: ")
        elif opcao_dados == "3":
            while True:
                novo_cpf = input("Novo CPF (apenas números): ")
                if len(novo_cpf) != 11:
                    print("CPF inválido. Digite apenas 11 números.")
                else:
                    cpf = novo_cpf
                    # Atualiza a formatação do CPF
                    cpf_formatado = '{}.{}.{}-{}'.format(
                        cpf[:3], cpf[3:6], cpf[6:9], cpf[9:])
                    print("\nCPF atual:", cpf_formatado)
                    break
        elif opcao_dados == "4":
            while True:
                novo_cep = input("Novo CEP (apenas números): ")
                if len(novo_cep) != 8:
                    print("CEP inválido. Digite apenas números (8 números).")
                else:
                    cep = novo_cep
                    cep_formatado = '{}-{}'.format(cep[:5], cep[5:])
                    print("\nCEP atual:", cep_formatado)
                    break
        elif opcao_dados == "5":
            senha = input("Nova Senha: ")
        elif opcao_dados == "6":
            carro[0] = input("Nova Placa do veículo: ")
            carro[1] = input("Novo Ano do veículo: ")
            carro[2] = input("Novo Modelo do veículo: ")
            carro[3] = input("Nova Cor do veículo: ")

        print("\n****Dados alterados com sucesso!****")

    # Opção 4: Alterar Plano
    elif escolha == "4":
        print("\n*** Alterar Plano ***")
        print("Atualmente você se encontra no", planoDeContratacao)
        print("Você pode mudar para o (1) Plano A, (2) Plano B, (3) Plano C")

        escolha_Assinatura = input("\nPara qual você deseja mudar?: ")
        while escolha_Assinatura not in ['1', '2', '3']:
            print("\nOpção inválida. Digite apenas uma das opções do menu.")
            escolha_Assinatura = input(
                "\nNível de Plano: \n(1) Plano A\n(2) Plano B\n(3) Plano C\nEscolha: ")
        if escolha_Assinatura == "1":
            planoDeContratacao = "Plano A"
        elif escolha_Assinatura == "2":
            planoDeContratacao = "Plano B"
        elif escolha_Assinatura == "3":
            planoDeContratacao = "Plano C"

        print("\n****Plano alterado com sucesso!****")

    # Opção 5: Ver Dados
    elif escolha == "5":
        print("\n*** Ver Dados ***")
        if nome and email and senha and cpf and cep and planoDeContratacao and carro[0] and carro[1] and carro[2] and carro[3]:
            print("\nNome:", nome)
            print("Email:", email)
            print("CPF:", cpf_formatado)
            print("CEP:", cep_formatado)
            print("Plano Porto:", planoDeContratacao)
            print("Placa do veículo:", carro[0])
            print("Ano do veículo:", carro[1])
            print("Modelo do veículo:", carro[2])
            print("Cor do veículo:", carro[3])
        else:
            print("Por favor, preencha seus dados antes de visualizar.")

    # Opção 6: Encerrar Sessão
    elif escolha == "6":
        print("\n*** Encerrando Sessão ***")
        print("Obrigado! Foi um prazer te atender!")
        break

    # Pergunta se deseja voltar ao menu inicial
    voltar_menu = input("\nDeseja voltar ao menu inicial? (1) Sim (2) Não: ")
    if voltar_menu == "2":
        print("\nObrigado! Foi um prazer te atender!")
        break
