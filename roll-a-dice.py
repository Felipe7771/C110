import random
response = "y"
total_value_dice = 0

while response == "y":
    no = random.randint(1,6)

    if no == 1:
        print("[-----]")
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
        print("[-----]")
    elif no == 2:
        print("[-----]")
        print("[ 0   ]")
        print("[     ]")
        print("[   0 ]")
        print("[-----]")
    elif no == 3:
        print("[-----]")
        print("[ 0   ]")
        print("[  0  ]")
        print("[   0 ]")
        print("[-----]")
    elif no == 4:
        print("[-----]")
        print("[0   0]")
        print("[     ]")
        print("[0   0]")
        print("[-----]")
    elif no == 5:
        print("[-----]")
        print("[0   0]")
        print("[  0  ]")
        print("[0   0]")
        print("[-----]")
    elif no == 6:
        print("[-----]")
        print("[0   0]")
        print("[0   0]")
        print("[0   0]")
        print("[-----]")
    
    total_value_dice = total_value_dice + no
    
    response = input("Pressione y para jogar novamente e n para sair >")
    print("\n\n")
print(f"Obrigado por jogar, [Soma dos Dados => {total_value_dice}]")