from flask import Flask, render_template, request

app = Flask(__name__)

# medical questions and answers
# questions = {
#     'question1': 'Do you have a fever?',
#     'question2': 'Are you experiencing cough and/or shortness of breath?',
#     'question3': 'Are you experiencing headache and/or body aches?',
#     'question4': 'Are you experiencing nausea and/or diarrhea?',
# }
questions = {
'question1': 'Did the employee effectively communicate with team members and management?',
'question2': 'Did the employee collaborate well with colleagues and contribute to team projects?',
'question3': 'Did the employee effectively meet deadlines and complete assigned tasks?',
'question4': 'Did the employee handle feedback and constructive criticism well?',
}

answers = {
    'answer1_yes': 'Yes, the employee effectively communicated with team members and management by actively listening, expressing themselves clearly and concisely, and providing feedback in a professional manner',
    'answer1_yes_cure': '',

    'answer1_no': 'No, the employee did not effectively communicate with team members and management by interrupting, talking over others, and failing to express themselves clearly.',
    'answer1_no_cure':  '',

    'answer2_yes': 'Yes, the employee collaborated well with colleagues and contributed to team projects by sharing knowledge, ideas, and resources, and resolving conflicts effectively.',
    'answer2_yes_cure': '',

    'answer2_no': 'No, the employee did not collaborate well with colleagues and failed to contribute to team projects by not sharing knowledge, ideas, and resources, and not resolving conflicts effectively.',
    'answer2_no_cure': '',

    'answer3_yes': 'Yes, the employee effectively met deadlines and completed assigned tasks by prioritizing tasks, managing time effectively, and producing high-quality work within the given timeframe.',
    'answer3_yes_cure': '',

    'answer3_no': 'No, the employee did not effectively meet deadlines and complete assigned tasks by failing to prioritize tasks, not managing time effectively, and producing low-quality work.',
    'answer3_no_cure': '',

    'answer4_yes': 'Yes, the employee handled feedback and constructive criticism well by receiving and acting on feedback, addressing areas for improvement, and learning from mistakes.',
    'answer4_yes_cure':'',

    'answer4_no': 'No, the employee did not handle feedback and constructive criticism well by being defensive, dismissive, or not taking action on feedback',
    'answer4_no_cure': ''
}

# home page
@app.route('/')
def index():
    return render_template('index.html')

# medical questionnaire
@app.route('/questionnaire')
def questionnaire():
    return render_template('questionnaire.html', questions=questions)

# results page
@app.route('/results', methods=['POST'])
def results():
    result = ''
    for key in request.form:
        result += request.form[key]

    if result == '1100':
        return render_template('results.html', result=answers['answer1_yes'], cure = answers['answer1_no_cure'])
    elif result == '1110':
        return render_template('results.html', result=answers['answer2_yes'],cure = answers['answer2_yes_cure'])
    elif result == '1001':
        return render_template('results.html', result=answers['answer3_yes'], cure = answers['answer3_yes_cure'])
    elif result == '1011':
        return render_template('results.html', result=answers['answer4_yes'], cure = answers['answer4_yes_cure'])
    elif result == '0010':
        return render_template('results.html', result=answers['answer1_no'],cure = answers['answer1_no_cure'])
    elif result == '0110':
        return render_template('results.html', result=answers['answer2_no'],cure = answers['answer2_no_cure'])
    elif result == '0001':
        return render_template('results.html', result=answers['answer3_no'], cure = answers['answer3_no_cure'])
    elif result == '0101':
        return render_template('results.html', result=answers['answer4_no'], cure = answers['answer4_no_cure'])
    else:
        return 'Invalid input'

if __name__ == '__main__':
    app.run(debug=True)
