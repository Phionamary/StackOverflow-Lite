from flask import Flask,jsonify,abort, make_response,request

from .model import questions

NOT_FOUND = 'Not found'
BAD_REQUEST = 'Bad request'

app = Flask(__name__)

def get_single_question(qnId):

    for question in questions:
        if question.qnId == qnId:
            return question 

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': NOT_FOUND}), 404)


@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': BAD_REQUEST}), 400)


@app.route('/api/v1/questions', methods=['GET'])
def get_all_question():
    return jsonify({'questions': questions})

@app.route('/api/v1/questions/<int:id>', methods=['GET'])
def get_question(qnId):
    question = get_single_question(id)
    if not question:
        abort(404)
    return jsonify({'questions': questions})


@app.route('/api/v1.0/questions', methods=['POST'])
def post_question():
    if not request.json or 'question' not in request.json:
        abort(400)
    question_id = len(questions) + 1
    new_question = request.json.get('question')
    question = {"qnId": question_id, "question": new_question}
    questions.append(question)
    return jsonify({'question': question}), 201

@app.route('/api/v1.0/questions/<int:id>', methods=['DELETE'])
def delete_question(qnId):
    question = get_question(qnId)
    if len(question) == 0:
        abort(404)
    questions.remove(question[0])
    return jsonify({}), 204

if __name__ == '__main__':
    app.run(debug=True)

