from flask import Flask, jsonify, make_response, request

from questions import questions

app = Flask(__name__)

answers = [
    {'id': 1, 'answer': [{'ans_id':1,'answer': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Commodi reiciendis reprehenderit repellat tenetur ipsum beatae corrupti corporis natus a fuga illum harum accusantium laborum aspernatur, sequi, ut tempora nesciunt itaque.'},
    {'id': 2, 'answer': [{'ans_id':2,'answer':'Lorem ipsum dolor sit amet consectetur adipisicing elit. Commodi reiciendis reprehenderit repellat tenetur ipsum beatae corrupti corporis natus a fuga illum harum accusantium laborum aspernatur, sequi, ut tempora nesciunt itaque.'},
    {'id': 3, 'answer': [{'ans_id':3,'answer':'Lorem ipsum dolor sit amet consectetur adipisicing elit. Commodi reiciendis reprehenderit repellat tenetur ipsum beatae corrupti corporis natus a fuga illum harum accusantium laborum aspernatur, sequi, ut tempora nesciunt itaque.'}
]

@app.route('/api/v1/questions/<int:qn_id>/answer', methods={'POST'})

def add_answer(id):
    particular_question = answers[id - 1]
    all_answers = particular_question['answer']

    given_answer = request.get_json()
    if valid_answer(given_answer):
        new_answer={'ans_id':(len(all_answers)+1),'answer':given_answer["answer"]}
        all_answers.append(new_answer)
        return jsonify({'answers': answers})

if __name__ == '__main__':
    app.run(debug=True)

