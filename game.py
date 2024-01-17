
def generate_question(question : str, options : list[str], correct : str):
    
    correct_flag = False
    for opt in options:
        if opt == correct:
            correct_flag = True
            
            
    if not correct_flag:
        print('There is no option matching the correct one!')
        return None
    
    return {
        'question' : question,
        'options' : options,
        'correct' : correct
    }

def questions_from_file():
    PATH = 'questions.txt'
    ENCODING = 'utf-8'
    TO_REMOVE = set(['', '\n'])

    with open(PATH, 'r', encoding=ENCODING) as file:
        raw_lines = file.read().split('\n\n')
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


questions = questions_from_file()

print(questions)



