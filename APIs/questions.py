from flask import Flask, jsonify, make_response, request

app = Flask(__name__)

questions=[
        {
            'id': 1,
            'title': 'Question One',
            'body': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Commodi reiciendis reprehenderit repellat tenetur ipsum beatae corrupti corporis natus a fuga illum harum accusantium laborum aspernatur, sequi, ut tempora nesciunt itaque.',
            'author': 'Phii',
            'create_date': '10-09-2017'
        },

        {
            'id': 2,
            'title': 'Question Two',
            'body': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Commodi reiciendis reprehenderit repellat tenetur ipsum beatae corrupti corporis natus a fuga illum harum accusantium laborum aspernatur, sequi, ut tempora nesciunt itaque.',
            'author': 'Winy',
            'create_date': '30-09-2017'
        },

        {
            'id': 3,
            'title': 'Question Three',
            'body': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Commodi reiciendis reprehenderit repellat tenetur ipsum beatae corrupti corporis natus a fuga illum harum accusantium laborum aspernatur, sequi, ut tempora nesciunt itaque.',
            'author': 'Jackie',
            'create_date': '16-11-2017'
        },

    ]

def _get_question(id):
    return [question for question in questions if question['id'] == id]

@app.route('/api/v1/questions', methods=['GET'])
def get_questions():
    return jsonify({'questions': questions})


@app.route('/api/v1/question/<int:id>', methods=['GET'])
def get_question(id):
    question = _get_question(id)
    return jsonify({'questions': question})


@app.route('/api/v1/questions', methods=['POST'])
def post_question():
    question_id = questions[-1].get("id") + 1
    title = request.json.get('title')
    body = request.json.get('body')
    author= request.json.get('author')
    create_date= request.json.get('create_date')
    question = {"id": question_id, "title": title,"body": body, "author": author, "create_date": create_date}
    questions.append(question)
    return jsonify({'question': question}), 201


@app.route('/api/v1/questions/<int:id>', methods=['DELETE'])
def delete_question(id):
    question = _get_question(id)
    questions.remove(question[0])
    return jsonify({}), 204


if __name__ == '__main__':
    app.run(debug=True)

