sair=False
extrato="##### EXTATO #####"
saque_limite_quantidade=0
SAQUE_VALOR_MAXIMO= 500.00
SAQUE_QUANTIDADE_MAXIMA=3
saldo=1000.00




while sair==False:
    print("""
#################### MENU ####################
QUAL OPERAÇÃO DESEJA REALIZAR?
          [1] SACAR
          [2] DEPOSITAR
          [3] EXIBIR EXTRATO
          [99] SAIR               """)
    menu=int(input())

    if (menu!=1 and menu!=2 and menu!=3):
        print("SAINDO DO SISTEMA. OBRIGADO!")
        sair=True

    if(menu==1):
        valor=float(input("Digite o valor a ser sacado:"))
        if(valor>0):
            if(saque_limite_quantidade==3):
                print(f"Limite diário de quantidade de saques exceddo. O limited diário atual é de {SAQUE_QUANTIDADE_MAXIMA}")
                continue

            if(valor>500):
                print(f"Valor superior ao limite diário de R${SAQUE_VALOR_MAXIMO}")
                continue
            if(saldo>=valor):
                saldo-=valor
                extrato+=f"\n Saque: R${valor}"
                saque_limite_quantidade+=1
        else: 
            print("Digite um valor superior a zero")
            continue
    
    if(menu==2):
        valor=float(input("Digite o valor a ser depositado:"))
        if(valor>0):
            saldo+=valor
            extrato+=f"\n Depósito: R${valor}"
            
        else: 
            print("Digite um valor superior a zero")
    
    if(menu==3):
       print(extrato)
       print(f"Saldo atual: R${saldo}")
    




