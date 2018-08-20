from flask import Flask, jsonify, make_response, request, json

from questions import questions

app = Flask(__name__)

answers = [
    {'id': 1, 'answer': [{'ans_id':1,'answer': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Commodi reiciendis reprehenderit repellat tenetur ipsum beatae corrupti corporis natus a fuga illum harum accusantium laborum aspernatur, sequi, ut tempora nesciunt itaque.'},
    {'id': 2, 'answer': [{'ans_id':2,'answer':'Lorem ipsum dolor sit amet consectetur adipisicing elit. Commodi reiciendis reprehenderit repellat tenetur ipsum beatae corrupti corporis natus a fuga illum harum accusantium laborum aspernatur, sequi, ut tempora nesciunt itaque.'},
    {'id': 3, 'answer': [{'ans_id':3,'answer':'Lorem ipsum dolor sit amet consectetur adipisicing elit. Commodi reiciendis reprehenderit repellat tenetur ipsum beatae corrupti corporis natus a fuga illum harum accusantium laborum aspernatur, sequi, ut tempora nesciunt itaque.'}
]


@app.route("/api/v1/questions/2/answers", methods=["POST"])

def answer():
    """Adds answer to question."""
    answers = {
        "id": request.json["id"],
        "answer": request.json["answer"]
    }
    QUESTION["id" == 2]["answer"].update(answers)
    return jsonify(answers)

if __name__ == '__main__':
    app.run(debug=True)

