import json, random, os, time

with open('Questions.json','r',encoding='utf-8') as f:
    json_preguntas = json.loads(f.read())

#----------------------------------------
def new_game():
    category = 0
    show_question(category)


#------------------------------------------------
def clear_screen(): 
    if os.name == "posix":
        time.sleep(3)
        os.system ("clear")
    else :
        time.sleep(3)
        os.system ("cls")


#----------------------------------------
def check_answer(option,cat,correct):
    if option == correct:
        cat+=1
        print()
        print("CORRECT!!!!! Your cumulative score is: "+ str(cat*5) + " Points" )
        if cat <= 4:
            show_question(cat)
        elif cat > 4:
            print()
            print('YOU WON !!!!!')
    elif option != correct:
        print()
        print('SORRY - YOU LOST!!')
        exit(1)


    #----------------------------------------
def display_score():
        pass

#----------------------------------------
def play_again():
    pass


def show_question(category):
    #os.system('cls')
    clear_screen()
    #print(category)
    category_questions = json_preguntas['Preguntas'][category]
    ramdom_question=random.randint(0,4)
    print(80 * "-")
    print (category_questions[ramdom_question]['question'])
    print()
    for options in category_questions[ramdom_question]['options']:
        print (options)
    print()
    selected_option=input('Select one Option (A, B, C, or D) type E to exit the game : ')
    selected_option=selected_option.upper()
    correct_answer= category_questions[ramdom_question]['answer']
    #print(correct_answer)
    check_answer(selected_option,category,correct_answer)
    print(80 * "-")



new_game()


















'''print(json_preguntas['Preguntas'][0][0]['pregunta'])
print(json_preguntas['Preguntas'][0][1]['pregunta'])
print(json_preguntas['Preguntas'][0][2]['pregunta'])
print(json_preguntas['Preguntas'][0][3]['pregunta'])
print(json_preguntas['Preguntas'][0][4]['pregunta'])
#print(json_preguntas['Preguntas'][0])
pre = json_preguntas['Preguntas'][2]
pregunta_mostrar=random.randint(0,4)

#print(type(pre))
print(80 * "-")
print (pre[pregunta_mostrar]['question'])
print()
#print (pre[pregunta_mostrar]['options'])
for op in pre[pregunta_mostrar]['options']:
    print (op)
print()
print('Select one Option : ')
print(80 * "-")

#print(json_preguntas['Preguntas'][0][0]['opciones'][3]['flag'])
#bandera= json_preguntas['Preguntas'][0][0]['opciones'][3]['flag']
#print(bandera)'''