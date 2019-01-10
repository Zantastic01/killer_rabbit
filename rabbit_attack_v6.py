# Rabbit Attack!

def start():
    print("Welcome to RABBIT ATTACK!")
    print('         ,')
    print('        /|      __')
    print('       / |   ,-~ /')
    print('       Y :|  //  /')
    print('       | jj /( .^')
    print('       >-"~"-v"')
    print('      /       Y')
    print('     jo  o    |')
    print('    ( ~T~     j')
    print("     >._-' _./      ")
    print('    /   "~"  |      ')
    print('   Y     _,  |      ')
    print('  /| ;-"- _  |      ')
    print(' / l/ ,-"~    \     ')
    print(' \//\/      .- \    ')
    print('  Y        /    Y   ')
    print('  l       I     !   ')
    print('  ]\      _\    /"\ ')
    print('  ~----( ~   Y.  )  ')

def end():
    print("Goodbye. Thanks for playing!")
    
def confirm(question):
    while True:
        answer = input(question + " (y/n)")

        if answer in ['y', 'Y', 'yes', 'Yes', 'YEs', 'YES', 'yEs', 'yES', 'yeS', 'YeS']:
            return True
        elif answer in ['n', 'N', 'no', 'No', 'NO', 'nO']:
            return False

def play():
    num_knights = 5
    rabbit_is_alive = True

    print("Look, a cute little bunny rabbit.")

    while rabbit_is_alive and num_knights > 0:
        use_grenade = confirm("Shall we use the Holy Hand Grenade?")
            
        if use_grenade:
            print('       ,--.!,')
            print('    __/   -*-')
            print("  ,d08b.  '|`")
            print('  0088MM     ')
            print("  `9MMP'   ")
            print("1... 2... 5... No, 3!")
            print('     _.-^^---....,,--     ')  
            print(' _--                  --_  ')
            print('<                        >)')
            print('|                         | ')
            print(' \._                   _./  ')
            print("    ```--. . , ; .--'''      " )
            print('          | |   |            ') 
            print('       .-=||  | |=-.   ')
            print("       `-=#$%&%$#=-'   ")
            print('          | ;  :|     ')
            print(' _____.,-#%&$@%#&#~,._____ ')
            print("Boom!")
            rabbit_is_alive = False
        else:
            num_knights -= 1
            print("Oh, no! The rabbit just killed one of the knights!")
            print("Only " + str(num_knights) + " remain.")
        
    if num_knights > 0:
        print("The killer rabbit has been defeated. You win!")
    else:
        print("All of the knights are dead. You lose.")


start()

playing = True

while playing:
    play()
    playing = confirm("Would you like to play again?")

end()
