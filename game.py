
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
    with open(PATH, 'r', encoding=ENCODING) as file:
        line_questions = file.read().split('\n\n')

    questions = {}
    for element in line_questions: 
        if element.startswith('#'): continue
        split_question = line_questions.split('\n')

    

    return line_questions

    
questions_from_file()

questions = questions_from_file()



