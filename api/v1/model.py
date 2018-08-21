
questions = []
answers = []

class Questions(object):

    def __init__(self, qnId,title, question, answer):

        self.qnId = qnId
        self.title = title
        self.question = question
        self.answer = []

    def to_json(self):
        json_data = {
            'qnId': self.qnId,
            'title': self.title,
            'question': self.question,
            'answer': self.answer
        }

        return json_data

class Answer(object):
    def__init__(self,ansId,body)
        self.ansId=ansId
        self.body=body

question1 = Question (1, "Github", "What is GitHub?")
questions.append(question1)

answer1 = Answer (1, "GitHub is a Git repository hosting service, but it adds many of its own features. While Git is a command line tool, GitHub provides a Web-based graphical interface. It also provides access control and several collaboration features, such as a wikis and basic task management tools for every project.")
question1.answers.append(answer1)

question2 = Question (2, "Repos", "What is a repository?")
questions.append(question2)

answer2 = Answer (2, "A repository, or repo for short, a digital directory or storage space where you can access your project, its files, and all the versions of its files that Git saves.")
question2.answers.append(answer2)