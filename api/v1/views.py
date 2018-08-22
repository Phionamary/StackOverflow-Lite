from flask import Flask,jsonify,abort, make_response,request 

from v1.model import questions


NOT_FOUND = 'Not found'
BAD_REQUEST = 'Bad request'

app = Flask(__name__)

def get_single_question(qnId):

    for question in questions:
        if question["qnId"] == qnId:
            return question 

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': NOT_FOUND}), 404)


@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': BAD_REQUEST}), 400)


@app.route('/api/v1/get_questions', methods=['GET'])
def get_all_question():
    return jsonify({'questions': questions})
    #return questions

@app.route('/api/v1/get_question/<int:qnId>', methods=['GET'])
def get_question(qnId):
    question = get_single_question(qnId)
    if not question:
        abort(404)
    return jsonify({'question': question})


@app.route('/api/v1/post_questions', methods=['POST'])
def post_question():
    if not request.json or 'question' not in request.json:
        abort(400)
    question_id = len(questions) + 1
    new_question = request.json.get('question')
    question = {"qnId": question_id, "question": new_question}
    questions.append(question)
    return jsonify({'question': question}), 201

@app.route('/api/v1/edit_questions/<int:qnId>', methods=['PUT'])
def edit_question(qnId):
    question = get_question(qnId)
    if len(question) == 0:
        abort(404)
    if not request.json:
        abort(400)
    title = request.json.get('title', question[0]['title'])
    question = request.json.get('question', question[0]['question'])
    question[0]['title'] = title
    question[0]['question'] = question
    return jsonify({'question': question[0]}), 200

@app.route('/api/v1/delete_questions/<int:qnId>', methods=['DELETE'])
def delete_question(qnId):
    question = get_question(qnId)
    if len(question) == 0:
        abort(404)
    questions.remove(question[0])
    return jsonify({}), 204

if __name__ == '__main__':
    app.run(debug=True)

