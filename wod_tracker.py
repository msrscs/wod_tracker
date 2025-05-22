######################################################## 
# Faculdade: Cesar School                              #
# Curso: Segurança da Informação                       #
# Período: 2025.1                                      #
# Disciplina: Fundamentos de Programação               #
# Professora: Carol Melo                               #
# Projeto: WOD Tracker                                 #
# Equipe:                                              #
#           Carlos Vinicius                            #
#           Eduardo Henrique Ferreira Fonseca Barbosa  #
#           Gabriel de Medeiros Almeida                #
#           Hugo Rafael de Souza                       #
#           Mauro Sérgio Rezende da Silva              #
#           Silvio Barros Tenório                      #
# Versão: 1.2                                          #
# Data: 22/05/2025                                     #
######################################################## 

# Importa biblioteca os
import os

# Nome do Banco de Dados
banco_dados = "wod_tracker.csv"

# Função Limpa Tela do Terminal
def limpa_tela():
    os.system('cls')

# Função verificar se o arquivo do banco de dados existe
def verifica_arquivo(banco_dados):
    try:
        with open(banco_dados, mode="r", encoding="UTF-8") as arquivo:
            arquivo.readlines()
        return True
    except FileNotFoundError:
        return False

# Função Criar Cabeçalho no Banco de Dados
def bd_cabecalho():
    # Verifica se o arquivo do banco de dados existe.
    if not verifica_arquivo(banco_dados):
       # O with garante que o arquivo será fechado automaticamente após o bloco de código, mesmo que ocorra um erro.
       with open(banco_dados, mode='w', encoding="UTF-8") as arquivo:
            arquivo.write("ID|DATA|TIPO|DURACAO|MOVIMENTOS|RESULTADO|RECORD_PESSOAL|OBSERVACAO|\n")

# Funcão Insere Treino no Banco de Dados
def bd_insere_treino(data_treino, tipo_treino, duracao_treino, movimentos_treino, resultado_treino, record_pessoal_treino, observacao_treino):
    try:
        id_treino = bd_gera_id_treino()
        with open(banco_dados, mode="a", encoding="UTF-8") as arquivo:
              arquivo.write(f"{id_treino}|{data_treino}|{tipo_treino}|{duracao_treino}|{movimentos_treino}|{resultado_treino}|{record_pessoal_treino}|{observacao_treino}|\n")
        return True
    except Exception:
        return False

# Funcão Ler Treino do Banco de Dados
def bd_ler_treino():
    try:
        with open(banco_dados, mode="r", encoding="UTF-8") as arquivo:
              return arquivo.readlines()
    except Exception:
        return []

# Funcão Gera Id do Treino do Banco de Dados
def bd_gera_id_treino():
    try:
        with open(banco_dados, mode="r", encoding="UTF-8") as arquivo:
              treinos = arquivo.readlines()
              if len(treinos) > 1:
                id_treino = int(treinos[-1].split('|')[0]) + 1
                return f"{id_treino}"
              else:
                return "1"      
    except Exception:
        return "1"

# Funcão Grava Treinos no Banco de Dados
def bd_grava_treinos(treinos):
    try:
        with open(banco_dados, mode="w", encoding="UTF-8") as arquivo:
              arquivo.writelines(treinos)
        return True
    except Exception:
        return False

# Função Verifica Data do Treino
def verifica_data(data):
    try:
        partes = data.split("/") 
        dia = int(partes[0])
        mes = int(partes[1])
        ano = int(partes[2])
        
        # Verifica se o ano é menor que 2000 e maior 2100.
        if ano < 2000 or ano > 2100:
            return "?"
        
        # Verifica se o mês está entre 1 e 12.
        if mes < 1 or mes > 12:
            return "?"
        
        # Verifica os dias de cada mês (incluindo anos bissextos)
        dias_por_mes = [
            31,  # Janeiro
            29 if (ano % 400 == 0) or (ano % 100 != 0 and ano % 4 == 0) else 28,  # Fevereiro (bissexto)
            31,  # Março
            30,  # Abril
            31,  # Maio
            30,  # Junho
            31,  # Julho
            31,  # Agosto
            30,  # Setembro
            31,  # Outubro
            30,  # Novembro
            31   # Dezembro
        ]
        
        if dia < 1 or dia > dias_por_mes[mes - 1]:
            return "?"

        return data  # Data válida
    
    except Exception:  # Se não for possível dividir em dia/mês/ano ou converter para int
        return "?"

# Função Verifica Tipo do Treino
def verifica_tipo(tipon):
    tipo = "?"
    if tipon == '1':
        tipo = "AMRAP"
    if tipon == '2':
        tipo = "EMON"
    if tipon == '3':
        tipo = "FOR TIME"
    return tipo
 
# Função Verifica se é Número e positivo
def verifica_numero(numero):
    try:
        num = int(numero)
        if num < 0:
            return "0"
        
        return numero
    
    except Exception:
        return "0"

# Função Verifica Record Pessoal do Treino
def verifica_record_pessoal(record):
    if record == "S":
        return "S"
    else:
        return "N"

# Função Verifica Movimentos
def verifica_movimentos(movimentos):
    lista_movimentos = (movimentos.replace(";", ",")).split(",")
    novo_movimentos = ""
    for movimento in lista_movimentos:
        if not movimento.strip() == "":
            if not novo_movimentos == "":
                novo_movimentos += ","
            novo_movimentos += movimento.strip()

    return novo_movimentos

# Função Adicionar Treino
def adicionar_treino():
    # Limpa tela
    limpa_tela()

    print("**************************************************")
    print("*        WOD Tracker -  Adicionar Treino         *")
    print("**************************************************")

    # Entrada de dados do Treino 
    print("\nDigite os dados do Treino")
    data_treino = input("\tData (DD/MM/AAAA): ")
    tipon_treino = input("\tTipo ([1] AMRAP, [2] EMON, [3] FOR TIME): ")
    duracao_treino = input("\tDuração (min): ")
    movimentos_treino = input("\tMovimentos (separados por ,): ").upper()
    resultado_treino = input("\tResultado: ")
    record_pessoal_treino = input("\tRecord Pessoal ([S] Sim / [N] Não): ").upper()
    observacao_treino = input("\tObservação: ")
    
    # Verifica dados do Treino 
    data_treino = verifica_data(data_treino) 
    tipo_treino = verifica_tipo(tipon_treino)
    duracao_treino = verifica_numero(duracao_treino)
    movimentos_treino = verifica_movimentos(movimentos_treino)
    record_pessoal_treino = verifica_record_pessoal(record_pessoal_treino)

    # Adiciona Treino no Banco de Dados
    if bd_insere_treino(data_treino, tipo_treino, duracao_treino, movimentos_treino, resultado_treino, record_pessoal_treino, observacao_treino):
        input("\nTreino Adicionado OK! Tecle <ENTER> para continuar.")
    else:
        input("\nErro Adicionando Treino! Tecle <ENTER> para continuar.")
        
# Função Visualiza Treino
def visualizar_treino():
    # Limpa tela
    limpa_tela()

    print("**************************************************")
    print("*        WOD Tracker -  Visualizar Treino        *")
    print("**************************************************")

    treinos = bd_ler_treino()
    if len(treinos) > 1:
        try:
            id_treino = 0
            for treino in treinos:
                if id_treino != 0:
                    dados_treino = treino.split("|")
                    print(f"Treino N°: {dados_treino[0]}")
                    print(f"Data: {dados_treino[1]}")
                    print(f"Tipo: {dados_treino[2]}")
                    print(f"Duração (min): {dados_treino[3]}")
                    print(f"Movimentos: {dados_treino[4]}")
                    print(f"Resultado: {dados_treino[5]}")
                    if dados_treino[6] == 'S':
                        print("Record Pessoal: Sim")
                    else:
                        print("Record Pessoal: Não")
                    print(f"Observação: {dados_treino[7]}")
                    print("**************************************************")
                id_treino += 1
            input("\nTecle <ENTER> para continuar.")
        except Exception as e:
            input(f"\nErro {e}. Tecle <ENTER> para continuar.")
       
    else:
        input("\nNão exitem Treinos cadastrados! Tecle <ENTER> para continuar.")

# Função Edita Treino
def editar_treino():
    # Limpa tela
    limpa_tela()

    print("**************************************************")
    print("*         WOD Tracker -  Editar Treino           *")
    print("**************************************************")

    # Escolhe o Número do Treino a Editar
    id_treino = input("\tEntre com o N° do Treino a editar: ")
    if verifica_numero(id_treino) != "0":
        treinos = bd_ler_treino()
        if len(treinos) > 1:
            edita_treinos = []
            flg = False
            try:
                for treino in treinos:
                    dados_treino = treino.split("|")
                    if dados_treino[0] == id_treino:
                        # Editar os dados do Treino
                        print(f"\nEditar os dados do Treino N° {dados_treino[0]} (Deixar em branco para não alterar o valor)")
                        data_treino = input(f"\tData [{dados_treino[1]}] (DD/MM/AAAA): ")
                        tipon_treino = input(f"\tTipo [{dados_treino[2]}] ([1] AMRAP, [2] EMON, [3] FOR TIME): ")
                        duracao_treino = input(f"\tDuração [{dados_treino[3]}] (min): ")
                        movimentos_treino = input(f"\tMovimentos [{dados_treino[4]}] (separados por ,): ").upper()
                        resultado_treino = input(f"\tResultado [{dados_treino[5]}]: ")
                        aux = "Não"
                        if dados_treino[6] == "S":
                            aux = "Sim"
                        record_pessoal_treino = input(f"\tRecord Pessoal [{aux}] ([S] Sim / [N] Não): ").upper()
                        observacao_treino = input(f"\tObservação [{dados_treino[7]}]: ")

                        #  Solicita confirmação de edição do Treino
                        editar = input(f"\nConfirma Editar o Treino N° {dados_treino[0]} ([S] Sim / [N] Não): ").upper()

                        #  Verifica a confirmação de edição
                        if editar != "S":
                            input("\nEdição do N° Treino cancelada! Tecle <ENTER> para continuar.")
                            break

                        # Verifica dados do Treino e valores em branco
                        if data_treino.strip() == "":
                            data_treino = dados_treino[1]
                        else:    
                            data_treino = verifica_data(data_treino) 
                        if tipon_treino.strip() == "":
                            tipo_treino = dados_treino[2]
                        else:
                            tipo_treino = verifica_tipo(tipon_treino)
                        if duracao_treino.strip() == "":
                            duracao_treino = dados_treino[3]
                        else:
                            duracao_treino = verifica_numero(duracao_treino)
                        if movimentos_treino.strip() == "":
                            movimentos_treino = dados_treino[4]
                        else:
                            movimentos_treino = verifica_movimentos(movimentos_treino)
                        if resultado_treino.strip() == "":
                            resultado_treino = dados_treino[5]
                        if record_pessoal_treino.strip() == "":
                            record_pessoal_treino = dados_treino[6]
                        else:
                            record_pessoal_treino = verifica_record_pessoal(record_pessoal_treino)
                        if observacao_treino.strip() == "":
                            observacao_treino = dados_treino[7]

                        #  Edita Treino
                        edita_treinos.append(f"{dados_treino[0]}|{data_treino}|{tipo_treino}|{duracao_treino}|{movimentos_treino}|{resultado_treino}|{record_pessoal_treino}|{observacao_treino}|\n")
                        #  Flag que Editou o Treino
                        flg =True
                    else:
                        edita_treinos.append(treino)
                # Editar Treino no Banco de Dados
                if flg:
                    if bd_grava_treinos(edita_treinos):
                       input("\nTreino Editado OK! Tecle <ENTER> para continuar.")
                    else:
                       input("\nErro Editando Treino! Tecle <ENTER> para continuar.")
            except Exception as e:
                input(f"\nErro {e}. Tecle <ENTER> para continuar.")
        else:
            input("\nNão exitem Treinos cadastrados! Tecle <ENTER> para continuar.")
    else:
        input("\nN° do Treino inválido! Tecle <ENTER> para continuar.")

# Função Exclui Treino
def excluir_treino():
    # Limpa tela
    limpa_tela()

    print("**************************************************")
    print("*         WOD Tracker -  Excluir Treino          *")
    print("**************************************************")

    # Escolhe o Número do Treino a Editar
    id_treino = input("\tEntre com o N° do Treino a excluir: ")
    if verifica_numero(id_treino) != "0":
        treinos = bd_ler_treino()
        if len(treinos) > 1:
            exclui_treinos = []
            flg = False
            try:
                for treino in treinos:
                    dados_treino = treino.split("|")
                    if dados_treino[0] == id_treino:
                        # Exibe os dados do Treino
                        print(f"\nTreino N°: {dados_treino[0]}")
                        print(f"Data: {dados_treino[1]}")
                        print(f"Tipo: {dados_treino[2]}")
                        print(f"Tempo (min): {dados_treino[3]}")
                        print(f"Duração (min): {dados_treino[4]}")
                        print(f"Movimentos: {dados_treino[5]}")
                        print(f"Resultado: {dados_treino[6]}")
                        if dados_treino[7] == 'S':
                            print("Record Pessoal: Sim")
                        else:
                            print("Record Pessoal: Não")
                        print(f"Observação: {dados_treino[7]}")

                        #  Solicita confirmação de exclusão do Treino
                        excluir = input(f"\nConfirma Excluir o Treino N° {dados_treino[0]} ([S] Sim / [N] Não): ").upper()

                        #  Verifica a confirmação de edição
                        if excluir != "S":
                            input("\nEdição do N° Treino cancelada! Tecle <ENTER> para continuar.")
                            break

                        #  Flag que Editou o Treino
                        flg =True
                    else:
                        exclui_treinos.append(treino)
                # Excluir Treino no Banco de Dados
                if flg:
                    if bd_grava_treinos(exclui_treinos):
                       input("\nTreino Excluído OK! Tecle <ENTER> para continuar.")
                    else:
                       input("\nErro Eexcluindo Treino! Tecle <ENTER> para continuar.")
            except Exception as e:
                input(f"\nErro {e}. Tecle <ENTER> para continuar.")
        else:
            input("\nNão exitem Treinos cadastrados! Tecle <ENTER> para continuar.")
    else:
        input("\nN° do Treino inválido! Tecle <ENTER> para continuar.")

# Função Filtrar Treino por Tipo WOD
def filtro_tipo_treino():
    # Limpa tela
    limpa_tela()

    print("**************************************************")
    print("*   WOD Tracker -  Filtrar Treino por Tipo WOD   *")
    print("**************************************************")

    tipon_treino = input("\n Escolher o Tipo ([1] AMRAP, [2] EMON, [3] FOR TIME): ")
    tipo_treino = verifica_tipo(tipon_treino)
    if tipo_treino == "?":
        input("\nTipo inválido! Tecle <ENTER> para continuar.")
        return
    print()

    treinos = bd_ler_treino()
    if len(treinos) > 1:
        try:
            id_treino = 0
            conta = 0
            for treino in treinos:
                if id_treino != 0:
                    dados_treino = treino.split("|")
                    if dados_treino[2] == tipo_treino:
                        conta += 1
                        print(f"Treino N°: {dados_treino[0]}")
                        print(f"Data: {dados_treino[1]}")
                        print(f"Tipo: {dados_treino[2]}")
                        print(f"Duração (min): {dados_treino[3]}")
                        print(f"Movimentos: {dados_treino[4]}")
                        print(f"Resultado: {dados_treino[5]}")
                        if dados_treino[6] == 'S':
                            print("Record Pessoal: Sim")
                        else:
                            print("Record Pessoal: Não")
                        print(f"Observação: {dados_treino[7]}")
                        print("**************************************************")
                id_treino += 1
            if conta > 0:
                input("\nTecle <ENTER> para continuar.")
            else:    
                input(f"\nNão existem Treinos do Tipo [{tipo_treino}]! Tecle <ENTER> para continuar.")
        except Exception as e:
            input(f"\nErro {e}. Tecle <ENTER> para continuar.")
    else:
        input("\nNão exitem Treinos cadastrados! Tecle <ENTER> para continuar.")
    return

# Função Filtrar Treino por Movimento
def filtro_movimento_treino():
    # Limpa tela
    limpa_tela()

    print("**************************************************")
    print("*   WOD Tracker -  Filtrar Treino por Movimento  *")
    print("**************************************************")

    movimento_treino = input("\n Digite o Movimento: ").upper()
    print()

    treinos = bd_ler_treino()
    if len(treinos) > 1:
        try:
            id_treino = 0
            conta = 0
            for treino in treinos:
                if id_treino != 0:
                    dados_treino = treino.split("|")
                    movimentos = dados_treino[4].split(",")
                    if movimento_treino in movimentos:
                        conta += 1
                        print(f"Treino N°: {dados_treino[0]}")
                        print(f"Data: {dados_treino[1]}")
                        print(f"Tipo: {dados_treino[2]}")
                        print(f"Duração (min): {dados_treino[3]}")
                        print(f"Movimentos: {dados_treino[4]}")
                        print(f"Resultado: {dados_treino[5]}")
                        if dados_treino[6] == 'S':
                            print("Record Pessoal: Sim")
                        else:
                            print("Record Pessoal: Não")
                        print(f"Observação: {dados_treino[7]}")
                        print("**************************************************")
                id_treino += 1
            if conta > 0:
                input("\nTecle <ENTER> para continuar.")
            else:    
                input(f"\nNão existem Treinos com Movimento [{movimento_treino}]! Tecle <ENTER> para continuar.")
        except Exception as e:
            input(f"\nErro {e}. Tecle <ENTER> para continuar.")
    else:
        input("\nNão exitem Treinos cadastrados! Tecle <ENTER> para continuar.")

# Função Relatório Estatísico de Treino(Funcionalidade Extra)
def relatorio_treino():
    # Limpa tela
    limpa_tela()

    print("**************************************************")
    print("* WOD Tracker -  Relatório Estatístico de Treino *")
    print("**************************************************")

    treinos = bd_ler_treino()
    if len(treinos) > 1:
       try:
            total_treinos = 0
            total_record_pessoal = 0
            total_tipo_amrap = 0
            total_tipo_emon = 0
            total_tipo_for_time = 0
            total_movimentos = []
            movimentos = []
            cabecalho = False

            #  Totaliza dados do Treino
            for treino in treinos:
                if cabecalho:
                    dados_treino = treino.split("|")
                    total_treinos += 1
                    if dados_treino[6] == 'S':
                        total_record_pessoal += 1
                    if dados_treino[2] == "AMRAP":
                        total_tipo_amrap += 1    
                    elif dados_treino[2] == "EMON":
                        total_tipo_emon += 1    
                    elif dados_treino[2] == "FOR TIME":
                        total_tipo_for_time += 1    
                    aux_movimentos = dados_treino[4].split(",")
                    for movimento_treino in aux_movimentos:
                        if movimento_treino in movimentos:
                            indice = movimentos.index(movimento_treino)
                            total_movimentos[indice] = total_movimentos[indice] + 1
                        else:   
                            movimentos.append(movimento_treino)
                            total_movimentos.append(1)
                else:
                    cabecalho = True            

            # Exibe Relatório
            print(f"\nTotal de Treinos: {total_treinos}")
            print(f"\nTipo WOD\n\tTotal [AMRAP]: {total_tipo_amrap}")
            print(f"\tTotal [EMON]: {total_tipo_emon}")
            print(f"\tTotal [FOR TIME]: {total_tipo_for_time}")
            print("\nMovimentos")
            for i, mov in enumerate(movimentos):
                print(f"\tTotal [{mov}]: {total_movimentos[i]} ")
            print(f"\nTotal de Records Pessoal: {total_record_pessoal}")
            input("\nTecle <ENTER> para continuar.")
       except Exception as e:
            input(f"\nErro {e}. Tecle <ENTER> para continuar.")
    else:
        input("\nNão exitem Treinos cadastrados! Tecle <ENTER> para continuar.")


#######################
# Início da Aplicação #
#######################

# Cria Cabeçalho no Banco de Dados
bd_cabecalho()

#  Menu da Aplicação
while True:
    # Limpa tela
    limpa_tela()
    # Menu
    print("**************************************************")
    print("*                  WOD Tracker                   *")
    print("**************************************************")
    print("\nMENU PRINCIPAL")
    print("\t[1] Adicionar Treino")
    print("\t[2] Visualizar Treinos")
    print("\t[3] Editar Treino")
    print("\t[4] Excluir Treino")
    print("\t[5] Filtrar Treinos por Tipo WOD")
    print("\t[6] Filtrar Treinos por Movimento")
    print("\t[7] Relatório Estatístico de Treino")
    print("\t[0] Sair da aplicação")
    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        # Adicionar Treino
        adicionar_treino()
    elif opcao == "2":
        # Visualizar Treinos
        visualizar_treino()
    elif opcao == "3":
        # Editar Treino
        editar_treino()
    elif opcao == "4":
        # Excluir Treino
        excluir_treino()
    elif opcao == "5":
        # Filtrar Treinos por Tipo WOD
        filtro_tipo_treino()
    elif opcao == "6":
        # Filtrar Treinos por Movimento
        filtro_movimento_treino()
    elif opcao == "7":
        # Relatório de Estatístico de Treino - Funcionalidade Extra
        relatorio_treino()
    elif opcao == "0":
        # Sair da aplicação 
        break
    else:
        input("\nOpção inválida! Tecle <ENTER> para continuar.")
