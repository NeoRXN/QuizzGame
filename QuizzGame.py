import json, random, os, time, datetime

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
    username=''
    if option == "E":
        points = cat * 5000
        print()
        username = input('Be part of our leaderboard, what is your name? :  ')
        save_score(points,username)
    
        
    if option == correct:
        cat+=1
        points = cat * 5000
        print()
        print("CORRECT!!!!! Your cumulative score is: "+ str(points) + " Points" )
        if cat <= 4:
            show_question(cat)
        elif cat > 4:
            print()
            print('YOU WON !!!!!')
            print()
            username = input('Be part of our leaderboard, what is your name? :  ')   
            save_score(points,username)
    elif option != correct and option != "E":
        print()
        print('SORRY - YOU LOST!!')
        end_game()

#----------------------------------------

def save_score(points,username):
    filename='scores.txt' 
    file_exists = os.path.exists(filename)
    current_date = datetime.datetime.now()    
    if file_exists:
        score_data =(username +',  '+ str(points)+' Points'+',  '+ str(current_date.strftime("%c")))
        with open(filename, 'a') as f:
            f.write(score_data)
            f.write('\n')
            end_game()
    else:
        score_data =(username +',  '+ str(points)+' Points'+',  '+ str(current_date.strftime("%c")))
        with open(filename, 'w') as f:
            f.write(score_data)
            f.write('\n')
            end_game()
    

#----------------------------------------

def show_question(category):
    clear_screen()
    category_questions = json_preguntas['Preguntas'][category]
    ramdom_question=random.randint(0,4)    
    print (category_questions[ramdom_question]['question'])    
    print(80 * "-")
    print()
    for options in category_questions[ramdom_question]['options']:
        print (options)
    print()
    print(80 * "-")
    selected_option=input('Select one Option (A, B, C, or D) type E to exit the game : ')
    selected_option=selected_option.upper()
    correct_answer= category_questions[ramdom_question]['answer']
    check_answer(selected_option,category,correct_answer)

#----------------------------------------   

def welcome_screen():
     clear_screen()
     print(80 * "-")
     print()
     print('          Welcome to QUIZZGAME !!!!!!')
     print('')
     print('We are going to put into test your General Knowledge')
     print('')
     print('Are you ready?, The game will start in a few seconds')
     print('')
     print('Our evil elfs are working on the questions ...... hehehe :) ')
     print('')
     print(80 * "-")
     time.sleep(3)

#----------------------------------------    

def end_game():
    clear_screen()
    print(80*"-")
    print()
    print('Thanks to participate in the Quizz Game')
    print()
    print('I hope you enjoyed it')
    print()
    print(80*"-")

#------     Game Start      -------------

welcome_screen()
new_game()
