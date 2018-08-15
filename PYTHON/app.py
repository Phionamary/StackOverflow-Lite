from flask import Flask, jsonify, render_template

from data import Questions


app = Flask(__name__)

Questions=Questions()

@app.route('/')

def index():
    return render_template ('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/questions')
def questions():
    return render_template('questions.html',questions = Questions)

@app.route('/question/<string:id>/')
def question(id):
    return render_template('question.html', id=id)


@app.route('/post_question/')
def post_question():
    pass

@app.route('/post_answer/')
def post_answer():
    pass


def validate_question(questionObject):
    if 'question_id' in questionObject and 'topic' in questionObject and 'body' in questionObject:
        return True
    else:
        return False


if __name__=='__main__':
    app.run(debug=True)