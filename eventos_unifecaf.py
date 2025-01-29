#Importando o módulo colorama para melhorar a visibilidade dos menus e das mensagens de erro
from colorama import init, Fore, Back
init(autoreset=True)

import os

def limpar_tela():
    os.system ("cls" if os.name == "nt" else "clear")

def pause():
    #Função destinada a pausar o sistema em determinados pontos.
    input ("Pressione a tecla ENTER para retornar...")

#------------------------------------------------REFERENTE AO ACESSO PERMITIDO À ALUNOS DA INSTITUIÇÃO------------------------------------------
aluno = {
    #Dentro desse dicionário o número identificador equivale ao número do RA do aluno, 
    #a partir dele temos acesso ao restante das informações.
    "001":{ "Nome": "Ednaldo Pereira", "Nascimento": "15/01/1967", "Curso": "ADS", "Senha": "0123"},
    "002":{ "Nome": "Fernanda Rodrigues", "Nascimento": "28/11/1992", "Curso": "GTI", "Senha": "456"},
    "003":{ "Nome": "Rodrigo Amadeu", "Nascimento": "25/04/2001", "Curso": "ADM", "Senha": "789"}
}

def acesso_aluno():
    #Com a opção '1' selecionada no menu inicial, essa função é chamada para realizar o login do usuário como aluno da Unifecaf.
    # O Código ira buscar dentro do sistema se as credenciais inseridas condizem com os dados de alunos que possuímos armazenados.
    limpar_tela()
    print(f"{Fore.BLUE}---------------------------------------------")
    print(f"{Fore.YELLOW}--------- ACESSO ALUNO CADASTRADO -----------")
    print(f"{Fore.BLUE}---------------------------------------------","\n")

    for i in range(3,0,-1):
        #Dentro desse FOR construímos a possibilidade de tentar logar-se 3 vezes, uma vez atingido o limite, retorna ao menu inicial.
        #Também temos validações de inserção de dados, retornando mensagens de erros de acordo.
        ra_aluno_acesso = str(input(f"{Fore.YELLOW}Ensira seu RA (3 dígitos): "))
        if len(ra_aluno_acesso) != 3  or not ra_aluno_acesso.isdigit():
            print(f"{Fore.RED}Erro: O número do RA é composto por 3 dígitos. Tentativas de login restantes: {i-1}")
            continue
        senha_aluno_acesso = str(input(f"{Fore.YELLOW}Insira sua senha: "))

        if ra_aluno_acesso in aluno:
            aluno_logado = aluno[ra_aluno_acesso]
            if senha_aluno_acesso == aluno_logado["Senha"]:
                print("\n")
                print(f"{Fore.GREEN}Logado com sucesso. Bem vindo, {aluno_logado["Nome"]}.")
                print("\n")
                menu_aluno()
            else:
                print(f"{Fore.RED}Senha incorreta. Tentativas de login restantes: {i-1}")
        else:
            print(f"{Fore.RED}RA não encontrado. Tentativas de login restantes: {i-1}")
    pause()

def inscricao_aluno_evento():
    print(f"{Fore.BLUE}------------------------------------------------------")
    ra_aluno_confirma = str(input("1 - Confirme a numeração do seu RA: "))
    if ra_aluno_confirma in aluno:
        dados_aluno = aluno[ra_aluno_confirma]
        print(f"RA: {ra_aluno_confirma}")
        for chave, valor  in dados_aluno.items():
            if chave == "Senha":
                continue
            print (f"{chave}: {valor}")

        id_evento_escolhido = str(input("Ensira o Código do Evento que deseja se inscrever: "))
        if id_evento_escolhido in eventos:
            evento_confirmado = eventos[id_evento_escolhido]
            vagas = evento_confirmado["Vagas Disponíveis"]
            if vagas > 0:
                evento_confirmado["Alunos Cadastrados"].append(ra_aluno_confirma)
                evento_confirmado["Vagas Disponíveis"] = vagas - 1
                print(f"{Fore.GREEN}Inscrição realizada com sucesso! \n")
        else:
            print(f"{Fore.RED} Código de Evento não encontrado. Tente novamente. \n")
            menu_aluno()

    else:
        print(f"{Fore.RED}RA não encontrado. Por segurança, encerraremos seu acesso. \n")
        menu_inicial()
    
        
def menu_aluno():
    #Uma vez logado, o aluno tem acesso a essa tela que lista os eventos disponíveis e dá a opção de se inscrever em um deles.
    limpar_tela()
    print(f"{Fore.BLUE}------------------------------------------------------")
    print(f"{Fore.YELLOW}--------- PORTAL DO ALUNO - GRANDES EVENTOS ----------")
    print(f"{Fore.BLUE}------------------------------------------------------","\n")
    lista_eventos()
    print(f"{Fore.YELLOW}---------------------------------------------")
    resposta = input(f"{Fore.BLUE}Deseja se cadastrar em um evento? [s/n]: ")
    resposta = resposta.lower()
    if resposta == "s" and len(resposta) == 1:
        inscricao_aluno_evento()
    elif resposta == "n" and len(resposta) == 1:
        pause()
        menu_inicial()
    else:
        print("Operação inválida! Revise as opções disponíveis e tente novamente.")
        
    pause()
    menu_aluno()

#--------------------------------- REFERENTE AO ACESSO PERMITIDO À STAFFS DA INSTITUIÇÃO ----------------------------
staff = {
    #Dentro desse dicionário o número identificador equivale à um código nomeado como "Registro de STAFF" para membros docentes da faculdade,
    # o código é composto por uma letra e dois numerais para diferenciação dos RAs dos alunos que possuem 3 digitos numerais.
    "S01":{ "Nome": "Fabrício José", "Nascimento": "09/11/1968", "Cargo": "Professor", "Disciplina":"Matemática Financeira", "Senha": "123"},
    "S02":{ "Nome": "Elizeu Pereira", "Nascimento": "25/08/1977", "Cargo": "Professor", "Disciplina":"Lógica Computacional", "Senha": "456"},
    "S03":{ "Nome": "Júlia Vasconcelos", "Nascimento": "01/01/2002", "Cargo": "Professor", "Disciplina":"Agile Methods", "Senha": "789"}}

def acesso_staff():
    #Com a opção '2' selecionada no menu inicial, essa função é chamada para realizar o login do usuário como staff da Unifecaf.
    # O Código ira buscar dentro do sistema se as credenciais condizem com os dados que possuímos armazenados.
    limpar_tela()
    print(f"{Fore.BLUE}---------------------------------------------")
    print(f"{Fore.MAGENTA}-------- ACESSO STAFF CADASTRADO ----------")
    print(f"{Fore.BLUE}---------------------------------------------","\n")

    #Dentro desse FOR construímos a possibilidade de tentar logar-se 3 vezes, uma vez atingido o limite, retorna ao menu inicial.
    #Também temos validações de inserção de dados, retornando mensagens de erros de acordo.
    for i in range(3,0,-1):
        re_staff_acesso = str(input(f"{Fore.MAGENTA}Insira seu Registro de STAFF (Ex: S00): "))
        re_staff_acesso = re_staff_acesso.upper()
        if len(re_staff_acesso) != 3 and not re_staff_acesso.startswith("S"):
            print(f"{Fore.RED}Erro: O código do Registro de Staff exige 3 caracteres. Tentativas de login restantes: {i-1}")
            continue
        re_staff_senha = str(input(f"{Fore.MAGENTA}Insira sua senha: "))

        if re_staff_acesso in staff:
            staff_logado = staff[re_staff_acesso]
            if re_staff_senha == staff_logado["Senha"]:
                print("\n")
                print(f"{Fore.GREEN}Logado com sucesso. Bem vindo, {staff_logado["Nome"]}.")
                print("\n")
                menu_staff()
            else:
                print(f"{Fore.RED}Senha incorreta. Tentativas de login restantes: {i-1}")
        else:
            print(f"{Fore.RED}RA não encontrado. Tentativas de login restantes: {i-1}")
    pause()

def alternativas_staff(opcao_staff):
    #A opção selecionada no menu_staff() é tratada nessa função.
    match opcao_staff:
        case "1":
            limpar_tela()
            lista_eventos(exibir_alunos_cadastrados=True)
            print("\n")
            pause()
            menu_staff()
        case "2":
            limpar_tela()
            adicionar_evento()
            pause()
            menu_staff()
        case "3":
            limpar_tela()
            atualizar_evento(exibir_alunos_cadastrados = True)
            pause()
            menu_staff()
        case "4":
            limpar_tela()
            excluir_evento()
            pause()
            menu_staff()
        case "0":
            limpar_tela()
            menu_inicial()
        case _:
            limpar_tela()
            print(f"{Fore.RED}---------------------------------------------------------------")
            print(f"{Fore.RED}Opção inválida. Reveja as opções disponíveis e tente novamente.")
            pause()
            menu_staff()
    
def menu_staff():
    #O Menu de membros da Staff é mais complexo do que dos alunos, tendo diversas opções de gerenciamento de eventos disponíveis.
    limpar_tela()
    print(f"{Fore.BLUE}----------------------------------------------------------")
    print(f"{Fore.MAGENTA}--------- GERENCIAMENTO STAFF - GRANDES EVENTOS ----------")
    print(f"{Fore.BLUE}----------------------------------------------------------","\n")
    print("Opções de Gerenciamento: \n")
    print("1 - Visualizar Eventos")
    print("2 - Adicionar Evento")
    print("3 - Atualizar Evento Existente")
    print("4 - Excluir/Cancelar Evento")
    print("0 - Sair")
    opcao_staff = input("Digite o código númerico da opção desejada: ")
    alternativas_staff(opcao_staff)

#--------------------------------- REFERENTE AO ARMAZENAMENTO E GERENCIAMENTO DE EVENTOS ------------------------------

eventos = { "1":{"Descrição": "Workshop - Lógica Computacional com Python", "Data-inicio": "25/02/2025 às 08:00",
    "Data-fim": "25/02/2025 às 12h", "Professor":"Irineu da Silva Sauro","Local":"Campus Centro - Lab 1", "Vagas Disponíveis": 18,
    "Alunos Cadastrados": ["003","002"]},
    "2":{"Descrição": "Workshop - Banco de Dados Relacionais com MySQL Server", "Data-inicio": "24/03/2025 às 08:00",
    "Data-fim": "24/03/2025 às 12:00", "Professor":"Joel Santana","Local":"Campus Centro - Lab 2", "Vagas Disponíveis": 49,
    "Alunos Cadastrados": ["003"]},
    "3":{"Descrição": "Palestra - Desenvolvimento Pessoal e Empregabilidade", "Data-inicio": "27/04/2025 às 08:00",
    "Data-fim": "27/04/2025 às 10:00", "Professor":"Maria Gadu","Local":"Campus Taboão - Lab 11", "Vagas Disponíveis": 50,
    "Alunos Cadastrados": []},
}

cont_id_evento = len(eventos) + 1


def lista_eventos (exibir_alunos_cadastrados=False):
    #Essa função lista cada um dos eventos disponíveis com seus dados informativos.
    #Foi inserido uma validação de dados que permite imprimir mais ou menos informações dependendo de que função chamou a lista_eventos(),
    #se ela foi chamada a partir de um login de alunos, a chave "Alunos Cadastrados" não é impressa, apenas se for chamado por um login Staff
    print(f"{Fore.GREEN}--------- EVENTOS DISPONÍVEIS ----------")
    for id_evento, dados_evento  in eventos.items():
        print(f"{Fore.YELLOW}---------------------------------------------")
        print(f"Código do Evento: {id_evento}")
        for chave, valor in dados_evento.items():
            if chave == "Alunos Cadastrados":
                if exibir_alunos_cadastrados:
                    print(f"{Fore.YELLOW}{chave}: ")
                    if valor:
                        for ra in valor:
                            print(f"- RA: {ra} ")
                    else:
                        print(f"{Fore.RED}Nenhum aluno cadastrado no evento")
                else:
                    continue
            else:
                print (f"{chave}: {valor}")

def adicionar_evento():
    #Essa função solicita novas inserções de dados para cada chave do dicionário de eventos.
    #Após isso, combina com um número de identificador gerado a partir da quantidade de itens no dicionário de eventos e então registra o evento novo.
    #Valida se o novo evento está de fato registrado no dicionário e se o tiver, visualiza a lista de eventos para consulta.
    global cont_id_evento
    print(f"{Fore.GREEN}---------------------------------------------")
    print(f"{Fore.GREEN}--------------- CRIAR EVENTO ---------------")
    print(f"{Fore.GREEN}--------------------------------------------- \n")
    print(f"{Fore.YELLOW}Vamos agendar seu novo evento. Adicione as informações a seguir:")

    descricao_novo = str(input("1 - Adicione a descrição de seu evento (Tipo do evento) - (Título do Evento): "))
    data_inicio_novo = input("2 - Ensira a data de início do evento (DIA/MÊS/ANO HR:MIN): ")
    data_fim_novo = input("3 -Ensira a data do final do evento(DIA/MÊS/ANO HR:MIN):")
    professor_novo = str(input("4 - Ensira o nome do responsável pelo evento (Professor ou Palestrante): "))
    local_novo = str(input("5 - Ensira o local onde será realizado o evento: "))
    vagas_novo = int(input("6 - Ensira a quantidade de vagas disponíveis para participar do evento: "))

    novo_evento = {
        "Descrição": descricao_novo,
        "Data-inicio": data_inicio_novo,
        "Data-fim": data_fim_novo,
        "Professor": professor_novo,
        "Local": local_novo,
        "Vagas Disponíveis": vagas_novo,
        "Alunos Cadastrados": []
    }

    eventos [str(cont_id_evento)] = novo_evento
    if eventos [str(cont_id_evento)] == novo_evento:
        lista_eventos(exibir_alunos_cadastrados=True)
        print(f"{Fore.YELLOW}---------------------------------------------")
        print(f"{Fore.GREEN}Novo evento agendado com sucesso!")
    else:
        print(f"{Fore.RED}---------------------------------------------")
        print(f"{Fore.RED} Ocorreu um erro ao agendar o evento. Tente novamente.")


def atualizar_evento(exibir_alunos_cadastrados = False):
    #Essa função lista as opções de eventos disponíveis para que o usuário tenha acesso aos dados necessários para iniciar as alterações.
    #Em seguida, solicita o código identificador do evento que deseja modificar.
    #Após isso, mostra o número de opções disponíveis para serem alteradas e solicita ao usuário qual será trabalhada.
    #Uma vez alterada, mostra o evento na tela novamente com as novas informações.
    lista_eventos(exibir_alunos_cadastrados=True)
    print(f"{Fore.YELLOW}---------------------------------------------")
    print(f"{Fore.YELLOW}------------- MODIFICAR EVENTOS -------------")
    print(f"{Fore.YELLOW}---------------------------------------------")
    id_para_alterar = input(f"{Fore.MAGENTA} Digite o Código do Evento que deseja alterar: ")
    if id_para_alterar in eventos:
        evento_para_alterar = eventos[id_para_alterar]
        print(f"{Fore.YELLOW}---------------------------------------------")
        print(f"{Fore.YELLOW}Evento selecionado:")
        print(f"Código do Evento: {id_para_alterar}")
        for chave, valor in evento_para_alterar.items():
            if chave != "Alunos Cadastrados":
                print(f"{chave}: {valor}")
            if chave == "Alunos Cadastrados":
                if exibir_alunos_cadastrados:
                    print(f"{Fore.YELLOW}{chave}: ")
                    if valor:
                        for ra in valor:
                            print(f"- RA: {ra} ")
                    else:
                        print(f"{Fore.RED}Nenhum aluno cadastrado no evento")
                else:
                    continue        
        print(f"{Fore.YELLOW}---------------------------------------------")
        print("O que deseja alterar?")
        print("1 - Descrição")
        print("2 - Data-inicio")
        print("3 - Data-fim")
        print("4 - Professor (Responsável)")
        print("5 - Local")
        print("6 - Vagas Disponíveis")
        print("0 - Sair")
        opcao_alterar = input("Insira a opção desejada: ")

        match opcao_alterar:
            case "1":
                valor_novo = str(input("Ensira a nova descrição do evento: (Tipo do evento) - (Título do Evento)"))
                eventos[id_para_alterar]["Descrição"] = valor_novo
            case "2":
                valor_novo = str(input("Ensira a nova data de início do evento: (DIA/MÊS/ANO HR:MIN) "))
                eventos[id_para_alterar]["Data-inicio"] = valor_novo
            case "3":
                valor_novo = str(input("Ensira a nova data de encerramento do evento: (DIA/MÊS/ANO HR:MIN) "))
                eventos[id_para_alterar]["Data-fim"] = valor_novo
            case "4":
                valor_novo = str(input("Ensira o nome e sobrenome do novo responsável pelo evento: "))
                eventos[id_para_alterar]["Professor"] = valor_novo
            case "5":
                valor_novo = str(input("Ensira o novo local do evento: "))
                eventos[id_para_alterar]["Local"] = valor_novo
            case "6":
                valor_novo = int(input("Ensira a nova quantidade de vagas disponíveis: "))
                eventos[id_para_alterar]["Vagas Disponíveis"] = valor_novo
            case "0":
                return

    if id_para_alterar in eventos:
        evento_para_alterar = eventos[id_para_alterar]
        print(f"{Fore.YELLOW}---------------------------------------------")
        print(f"{Fore.GREEN}Evento Atualizado:")
        print(f"{Fore.GREEN}Código do Evento: {id_para_alterar}")
        for chave, valor in evento_para_alterar.items():
            if chave != "Alunos Cadastrados":
                print(f"{Fore.GREEN}{chave}: {valor}")
            if chave == "Alunos Cadastrados":
                if exibir_alunos_cadastrados:
                    print(f"{Fore.YELLOW}{chave}: ")
                    if valor:
                        for ra in valor:
                            print(f"- RA: {ra} ")
                    else:
                        print(f"{Fore.RED}Nenhum aluno cadastrado no evento")
                else:
                    continue

def excluir_evento():
    lista_eventos(exibir_alunos_cadastrados = True)
    print(f"{Fore.RED}---------------------------------------------")
    print(f"{Fore.RED}---------- CANCELAR/EXCLUIR EVENTO ----------")
    print(f"{Fore.RED}---------------------------------------------")
    evento_excluir = input(f"{Fore.YELLOW}Ensira a ID do evento que deseja excluir: ")
    for i in range(3,0,-1):
        re_staff_acesso = str(input(f"{Fore.MAGENTA}Por segurança, confirme seu Registro de Staff:"))
        re_staff_acesso = re_staff_acesso.upper()
        if len(re_staff_acesso) != 3 and not re_staff_acesso.startswith("S"):
            print(f"{Fore.RED}Erro: O código do Registro de Staff exige 3 caracteres. Tentativas de confirmação restantes:{i-1}")
            continue
        re_staff_senha = str(input(f"{Fore.MAGENTA}Confirme sua senha: "))

        if re_staff_acesso in staff:
            staff_logado = staff[re_staff_acesso]
            if re_staff_senha == staff_logado["Senha"]:
                print("\n")
                print(f"{Fore.GREEN}{staff_logado["Nome"]}, suas crendenciais foram confirmadas com sucesso.")
                del eventos[evento_excluir]
                print("\n")
                evento_check = False

                for chave in eventos:
                    if chave == eventos:
                        evento_check = True
                    break
    
                if evento_check == True:
                    print(f"{Fore.RED}Ocorreu um erro ao tentar excluir o evento. Código do Evento: {evento_excluir}") 
                else:
                    limpar_tela()
                    print(f"{Fore.GREEN}Código do Evento: {evento_excluir}. Foi excluído/cancelado com sucesso.")
                    print(f"{Fore.GREEN}Lista de eventos atualizada:")
                    print("\n")
                    lista_eventos(exibir_alunos_cadastrados = True)
            else:
                print(f"{Fore.RED}Senha incorreta. Tentativas restantes: {i-1}")
        else:
            print(f"{Fore.RED}RA não encontrado. Tentativas restantes: {i-1}")
        if i == 1:
            print(f"{Fore.RED}-----------------------------------------------------------------")
            print(f"{Fore.RED}Muitos erros consecutivos. Por segurança encerraremos seu acesso.")
            pause()
            menu_inicial()
    

    

#------------------------------ REFERENTE AO MENU INICIAL ------------------------------------

def menu_inicial():
    #O Menu inicial é a primeira tela a ser mostrada quando o usuário abrir o sistema,
    #a partir dela ele terá duas opções de acesso disponíveis.
    limpar_tela()
    print(f"{Fore.BLUE}---------------------------------------------")
    print(f"{Fore.BLUE}--------- UNIFECAF GRANDES EVENTOS ----------")
    print(f"{Fore.BLUE}---------------------------------------------\n")
    print("Acesse nossa plataforma para estar por dentro de todas as novidades! \n"),
    print("Você é: ")
    print("1 - Acesso: Aluno")
    print("2 - Acesso: Staff")
    print("0 - Sair")
    opcao = int(input("Insira o número correspondente à ação desejada: "))
    if opcao == 1:
        acesso_aluno()
    elif opcao == 2:
        acesso_staff()
    elif opcao == 0:
        limpar_tela()
        print(f"{Fore.RED}----------------------------------------------")
        print(f"{Fore.RED}------ ACESSO ENCERRADO - VOLTE SEMPRE! ------")
        print(f"{Fore.RED}----------------------------------------------")
        exit(0)
    else:
        print(f"{Fore.RED}Opção inválida! Confira as opções disponíveis e tente novamente.")
        pause()
    menu_inicial()

menu_inicial()