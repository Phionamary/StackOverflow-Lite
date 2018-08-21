class Questions(object):

    def __init__(self, qnId,question, answer):

        self.qnId = qnId
        self.question = question
        self.answer = answer

    def to_json(self):
        json_data = {
            'qnId': self.qnId,
            'question': self.question,
            'answer': self.answer
        }

        return json_data