import random
biology_questions_answers = {'The separation of a leaf, fruit, or other part from the body of a plant': 'abscission',
    'A compound,molecule, ion, etc.to which electrons are donated in the formation of a coordinate bond.': 'acceptor',
    'Any chromosome that is additional to the regular karyotype of a species': 'accessory',
    'A membrane-bound sac (organelle) found in animal cells and in single-celled eukaryotes.': 'Lysosome',
    'A large phagocytic cell  that can ingest pathogenic microorganisms ': 'macrophage',
    ' What is The second period of the Cenozoic era': 'Quatenary' }

num_of_students = int(input('Enter a Number: '))
for quiz_number in range(num_of_students):
    quiz_question_file = open(f'biologypaper{quiz_number + 1}.txt', 'w')
    quiz_answer_file = open(f'biologyanswer{quiz_number + 1}.txt', 'w')

    quiz_question_file.write(f'Name: \n \n Dept: \n\n Matric No: \n')
    quiz_question_file.write(f" { ' ' * 20} BIOLOGY TEST{quiz_number+1}")
    quiz_question_file.write('\n\n')

    questions=list(biology_questions_answers.keys())
    random.shuffle(questions)


    for question_number in range(6):
            correct_answer=biology_questions_answers[questions[question_number]]
            wrong_answer=list(biology_questions_answers.values())
            del wrong_answer[wrong_answer.index(correct_answer)]
            wrong_answer=random.sample(wrong_answer,2)
            answerOptions=wrong_answer + [correct_answer]
            random.shuffle(answerOptions)


            quiz_question_file.write(f'{question_number+1}.{questions[question_number]}\n')

            for i in range(3):
                options='ABC'
                quiz_question_file.write(f' {options[i]}. {answerOptions[i]} \n')
            quiz_question_file.write('\n\n')

            quiz_answer_file.write(f'{question_number+1}. {options[answerOptions.index(correct_answer)]} \n')


quiz_answer_file.close()
quiz_question_file.close()



