# Treinando a lógica de programação com o app GymRats. Finalizei o Mundo 1 do Curso de Python do professor Gustavo Guanabara e quero práticar o que foi aprendido até agora. 
# O objetivo do app é simular um treino de academia, onde o usuário pode escolher diferentes exercícios e registrar suas séries e repetições. 
# Após a evolução das aulas, o app será aprimorado com adição de outras funcionalidades. 

amarelo = '\033[1;33m'
laranja = '\033[1;38;5;208m'
limpa = '\033[m'

from time import sleep
print('-'*35)
print(f'{amarelo}----- GymRats -----{limpa}'.center(43))
print('-'*35)

nome = str(input('Olá, digite seu nome: ')).strip().title()
print(f'\n{laranja}=== Bem-vindo ao GymRats, {nome}! ==={limpa} \nAqui você poderá registrar seus treinos e acompanhar \nsua evolução. Vamos começar!')
sleep(1.3)

peso = 0
registro = ' '
while True:
    print(f'\n {laranja}=== MENU GYMRATS ==={limpa}'
    '\n[ 1 ] Fazer Check-in de Treino '
    '\n[ 2 ] Recalcular IMC/ Dados Biométricos '
    '\n[ 3 ] Ver meta de Água ' \
    '\n[ 4 ] Ver último Relato'
    '\n[ 5 ] Sair do programa')
    opcao = int(input('Escolha sua opção: '))
        
    if opcao == 5:
        print(f'{amarelo}Treino Finalizado! Volte Amanhã e registre seu desempenho!{limpa}')
        break

    if opcao == 1: 
        print(f'\n{laranja}=== Check-in do dia ==={limpa}'
        '\n---------------------------------'
        '\n|      TABELA DE TREINOS        |'
        '\n---------------------------------'
        '\n| [A] Glúteo - Inferiores       |'\
        '\n| [B] Quadríceps - Inferiores   |'
        '\n| [C] Costas/Bíceps - Superiores|'\
        '\n| [D] Ombro/Tríceps - Superiores|'
        '\n---------------------------------')

        treino = str(input('Escolha seu treino: ')).upper().strip()

        while treino not in 'ABCD' or treino == '':
            treino = str(input('Opção Inválida! Digite A, B, C, ou D: ')).upper()
        
        if treino == 'A':
            print(f'\n{amarelo}Check-in realizado!{limpa} ✅ Treino: Glúteo - Inferiores.' )
            print('Seu treino de hoje é: \n- Elevação Pelvica \n- Búlgaro \n- Cadeira Abdutora \n- Agachamento Sumô')

            carga = float(input('Qual foi sua carga máxima (kg) na Elevação Pélvica hoje? '))
            if carga >= 60:
                print(f'\nUAU! Tá forte em? {amarelo}{carga}kg é carga de atleta!{limpa} ')
            else:
                print(f'\nMuito bem! {carga}kg registrado. {amarelo}Foco na execução e na progressão!{limpa}')

        elif treino == 'B':
            print(f'\n{amarelo}Check-in realizado!{limpa} ✅ Treino: Quadríceps - Inferiores.')
            print('Seu treino de hoje é: \n- Leg Press \n- Agachamento Smith \n- Cadeira extensora \n- Afundo')

            carga = float(input('Qual foi sua carga máxima (kg) no Leg Press hoje? '))
            if carga >= 50:
                print(f'\nUAU! Tá forte em? {amarelo}{carga}kg é carga de atleta!{limpa} ')
            else:
                print(f'\nMuito bem! {carga}kg registrado. {amarelo}Foco na execução e na progressão!{limpa}')

        elif treino == 'C':
            print(f'\n{amarelo}Check-in realizado!{limpa} ✅ Treino: Costas/Bíceps - Superiores.')
            print('Seu treino de hoje é: \n- Puxada aberta \n- Remada Baixa \n- Pulldown \n- Bíceps Martelo \n- Biceps na polia ')

            carga = float(input('Qual foi sua carga máxima (kg) na Puxada aberta hoje? '))
            if carga >= 30:
                print(f'\nUAU! Tá forte em? {amarelo}{carga}kg é carga de atleta!{limpa} ')
            else:
                print(f'\nMuito bem! {carga}kg registrado. {amarelo}Foco na execução e na progressão!{limpa}')

        elif treino == 'D':
            print(f'\n{amarelo}Check-in realizado!{limpa} ✅ Treino: Ombro/Tríceps - Superiores.')
            print('Seu treino de hoje é: \n- Desenvolvimento \n- Elevação Lateral \n- Elevação frontal \n- Tríceps francês \n- Tríceps corda \n- Tríceps no banco')

            carga = float(input('Qual foi sua carga máxima (kg) no Desenvolvimento hoje? '))
            if carga >= 12:
                print(f'\nUAU! Tá forte em? {amarelo}{carga}kg é carga de atleta!{limpa} ')
            else:
                print(f'\nMuito bem! {carga}kg registrado. {amarelo}Foco na execução e na progressão!{limpa}')

        print(f'\n{laranja}=== Diário do Atleta ==={limpa}')
        sleep(1)
        registro = str(input('Escreva como foi o treino e suas observações: ')).strip()
        print('-'*45)
        print(f'{amarelo}Registro realizado com sucesso!{limpa}')
        print(f'"{registro}"')
        print('Continue acompanhando sua evolução diária!')
        print('-' * 45)
            
                
    elif opcao == 2:
        print(f'\n{laranja}=== Registro Biométrico ==={limpa} ')
        sleep(1)
        print(f'Vamos avaliar primeiro como está o seu IMC {amarelo}(Índice de Massa Corporal){limpa}')
        peso = float(input('Informe seu peso (kg): '))
        altura = float(input('Informe sua altura (m): '))
        imc = peso / (altura ** 2)

        print(f'\n {laranja}=== Calculando IMC... ==={limpa}')
        sleep(1.5)

        print(f'Seu IMC atual é: {amarelo}{imc:.2f}{limpa}')

        if imc < 18.5:
            print(f'IMC abaixo do ideal - O objetivo agora é {amarelo}focar na dieta{limpa} e no {amarelo}ganho de massa{limpa}')
        elif imc < 24.9:
            print(f'IMC está ideal - Excelente! Vamos continuar {amarelo}mantendo assim{limpa}.')
        elif imc < 29.9:
            print(f'IMC indica sobrepeso - Focar no {amarelo}cardio{limpa} e {amarelo}défit calórico{limpa}.')
        else:
            print(f'IMC indica obesidade - {amarelo}ATENÇÃO!{limpa} Precisamos de foco total na {amarelo}dieta{limpa}, {amarelo}treino{limpa} e principalmente no {amarelo}cardio{limpa}.')

    elif opcao == 3:
        if peso == 0:
            print('-'* 65 )
            print(f'{amarelo}Por favor, registre seus dados biométricos na opção [2] primeiro!{limpa}')
            print('-'* 65)
        else:
            print(f'\n{laranja}=== Meta de Água Diária ==={limpa}')
            agua = peso * (35/1000)
            print(f'{amarelo}Dica do GymRats:{limpa} Para o seu peso de {peso}kg, sua meta \nde água diária é de {amarelo}{agua:.2f} Litros{limpa}. Não se esqueça de hidratar!')
            print('-'*60)

    elif opcao == 4:
        if registro == ' ':
            print('-'* 60)
            print(f'{amarelo}Você ainda não fez check-in de nehum treino!{limpa}')
            print('-' * 60)
        else:
            print(f'\n{laranja}=== Último Registro do Diário ==={limpa}')
            print('-'*60)
            sleep(1)
            print('Seu último registro foi:')
            print(f'{amarelo}{registro}{limpa}')
            print('-' * 60)
    else:
        print(f'\n{amarelo}Opção Inválida no menu!{limpa} Por favor, escolha um aopção entre 1 e 5.')
               

    

