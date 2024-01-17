import question

available_questions = question.load_from_file()

while len(available_questions) > 0:
    current_question = available_questions.pop()
    question_key, answers_key, correct_key = current_question
    print(question_key, current_question[question_key], sep=': ', end='\n\n')

    options = current_question[answers_key]
    for i, opt in enumerate(options):
        print(f'{i})', opt)
    
    try:
        user_answer = input('Choose an option:')
    except:
        break

    if current_question[correct_key] == options[int(user_answer)]:
        print('Correct answer!', end='\n\n')
    else:
        print('Wrong answer!', end='\n\n')


