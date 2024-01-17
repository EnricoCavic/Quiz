def generate_question(question : str, options : list[str], correct : str):
    
    # validation
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

def load_from_file():
    PATH = 'questions.txt'
    ENCODING = 'utf-8'
    TO_REMOVE = set(['', '\n'])

    with open(PATH, 'r', encoding=ENCODING) as file:
        raw_lines = set(file.read().split('\n\n'))
    
    inline_questions = [item for item in raw_lines if item not in TO_REMOVE]
    questions = []
    for element in inline_questions: 
        if element.startswith('#'): continue
        question_value, answers_values, correct_value = element.split('\n')
        generated = generate_question(
            question_value,
            answers_values.split(', '),
            correct_value
        )

        if(generated is None) : continue
        questions.append(generated)

    return questions

