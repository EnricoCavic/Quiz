def generate_question(question : str, options : list[str], correct : str):
    
    correct_flag = False
    for opt in options:
        if opt == correct:
            correct_flag = True
            
            
    if not correct_flag:
        print('There is no option matching the correct one!')
        return None
    
    return {
        'Question' : question,
        'Options' : options,
        'Correct' : correct
    }

def load_questions():
    PATH = 'questions.txt'
    ENCODING = 'utf-8'
    TO_REMOVE = set(['', '\n'])

    with open(PATH, 'r', encoding=ENCODING) as file:
        raw_lines = set(file.read().split('\n\n'))
    
    inline_questions = [item for item in raw_lines if item not in TO_REMOVE]
    questions = []
    for element in inline_questions: 
        if element.startswith('#'): continue
        question, answers, correct = element.split('\n')

        questions.append(generate_question(
            question,
            answers.split(', '),
            correct
        ))

    return questions


available_questions = load_questions()
while len(available_questions) > 0:
    current_question = available_questions.pop()
    key1, key2, key3 = current_question
    print(key1, current_question[key1], sep=': ', end='\n\n')

    options = current_question[key2]
    for i in range(0, len(options)):
        print(f'{i}) {options[i]}')
    
    user_answer = input('Choose an option:')
    if current_question[key3] == options[int(user_answer)]:
        print('Correct answer!', end='\n\n')
    else:
        print('Wrong answer!', end='\n\n')


