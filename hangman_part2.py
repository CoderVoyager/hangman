import random
values=['class','socks','india','army','chorous','stumble','startup','engineer','thief','hang']
Game=1
lives=0
while Game==1:
    def final_list():
        global lives
        global Game
        if lives==0:
            print('\t         _____')
            print('\t|-------( X X )')
            print('\t|-------\     /')
            print('\t|        \+++/')
            print('\t|\t  \_/ ')

            print('\t|\t   |')
            print('\t|\t   |')
            print('\t|\t   |')
            print('\t|\t/  |  \ ')
            print('\t|\t   |')
            print('\t|\t   |')
            print('\t|\t   |')
            print('\t|\t /    \ ')
        print()
        print()
        lives=0
        Game=0
        
    def message_func():
        print('Wrong guess try again')
    def message_func_2(result_list,check_list):
        global Game
        if result_list==check_list:
            print('You win')
            Game=0
        else:
            print('You lose')
        print('\t\t\tTHANK YOU FOR PLAYING THE GAME. HOPE YOU LIKED IT  "-"')
    def Random_value_func(a):
        check_list=[]
        ran_value=random.choice(a)
        for c in ran_value:
            check_list.append(c)
        return check_list
    def lives_func():
        check_list=Random_value_func(values)
        l=len(check_list)
        global lives
        lives=l+2
        return lives
    def check_func():
        check_list=Random_value_func(values)
        l=len(check_list)
        result_list=[]
        for i in range(l):
                result_list.append('__')
        global lives
        lives=lives_func()
        while lives>0:
            Input=input('Guess a letter')
            
            for j in range(l):
                if Input==check_list[j]:
                    result_list[j]=Input
            print(result_list)
            lives-=1
            if Input not in check_list:
                message_func()
                
            if result_list==check_list or lives==0:
                message_func_2(result_list,check_list)
                final_list()
                break
    check_func()
    def replay_func():
        global Game
        Game=int(input('Wanna play again(0,1)'))
    replay_func()
    
            
                
                
        
        
        
        
        
        

    
    
