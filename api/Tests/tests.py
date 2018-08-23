import unittest
from flask import Flask,jsonify,make_response,request
from copy import deepcopy
import sys
import json

from v1.views import app
from v1.model import questions

test_question1= {
                'qnId':'1',
                'question': 'What is GitHub?',
                'answer': 'GitHub is a Git repository hosting service, but it adds many of its own features. While Git is a command line tool, GitHub provides a Web-based graphical interface. It also provides access control and several collaboration features, such as a wikis and basic task management tools for every project.'
            }
test_question2= {
                'qnId':'2',
                'question':'What is a repo?',
                'answer': 'a repository, or “repo” for short, a digital directory or storage space where you can access your project, its files, and all the versions of its files that Git saves.'
            }


class all_questions_test(unittest.TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def tearDown(self):
        questions[:] = []

    #test if all questions are displayed
    def test_get_all_questions(self):
        # Tests that all questions can be retrieved
        test_user = app.test_client(self)
        response = test_user.get("/api/v1/get_questions", content_type="application/json")
        self.assertEqual(response.status_code,200)

    def test_API_can_create_new_questions(self):
        test_user=app.test_client(self)
        response=test_user.post('/api/v1/post_questions',data=json.dumps(test_question1),content_type="application/json")
        self.assertIn('question', str(response.data), msg="Question added successfully")
        self.assertEqual(response.status_code, 201)

    def test_API_get_one_question(self):
        # Tests to show one  questions
        test_user = app.test_client(self)
        test_user.post('/api/v1/post_questions',data=json.dumps(test_question1),content_type="application/json")
        response = test_user.get('/api/v1/get_question/1',content_type='application/json')
        self.assertIn('question', str(response.data))
        self.assertEqual(response.status_code, 200)

    def test_delete_question(self):
        test_user = app.test_client(self)
        test_user.delete('/api/v1/delete_questions/<int:qnId>', data=json.dumps(test_question1), content_type="application/json")
        response = test_user.delete('/api/v1/delete_questions/1')
        ids = [question['qnId'] for question in questions]
        if 1 in ids:
            self.assertEqual(response.status_code, 200)

    #def test_add_answer_to_question(self):
        #test_user = app.test_client(self)
        #test_user.post('/api/v1/post_questions',data=json.dumps(test_question1),content_type="application/json")
        #response = test_user.post("/api/v1/add_answer/1",content_type = 'application/json')
        #self.assertEquals(response.status_code, 201)
        #self.assertIn('question', str(response.data), msg='Answer added successfully')
        

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()