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
                'qnId':'3',
                'question':'What is a repo?',
                'answer': 'a repository, or “repo” for short, a digital directory or storage space where you can access your project, its files, and all the versions of its files that Git saves.'
            }


class QuestionsTestCase(unittest.TestCase):

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = app(config_name="testing")
        self.client = self.app.test_client
        self.question = {'question': 'What is GitHub?'}


    def test_question_creation(self):
        """Test API can create a new question (POST request)"""
        res = self.client().post('/questions/', data=self.question)
        self.assertEqual(res.status_code, 201)
        self.assertIn('What is GitHub?', str(res.data))

    def test_api_can_get_all_questions(self):
        """Test API can get a question (GET request)."""
        res = self.client().post('/questions/', data=self.question)
        self.assertEqual(res.status_code, 201)
        res = self.client().get('/questions/')
        self.assertEqual(res.status_code, 200)
        self.assertIn('What is GitHub?', str(res.data))

    def test_api_can_get_question_by_id(self):
        """Test API can get a single single by using it's id."""
        rv = self.client().post('/questions/', data=self.question)
        self.assertEqual(rv.status_code, 201)
        result_in_json = json.loads(rv.data.decode('utf-8').replace("'", "\""))
        result = self.client().get(
            '/questions/{}'.format(result_in_json['qnId']))
        self.assertEqual(result.status_code, 200)
        self.assertIn('What is GitHub?', str(result.data))


    def test_question_can_be_deleted(self):
        """Test API can delete an existing question. (DELETE request)."""
        rv = self.client().post(
            '/questions/',
            data={'question': 'What is a repo?'})
        self.assertEqual(rv.status_code, 201)
        res = self.client().delete('/questions/1')
        self.assertEqual(res.status_code, 200)
        # Test to see if it exists, should return a 404
        result = self.client().get('/questions/1')
        self.assertEqual(result.status_code, 404)

    def tearDown(self):
        questions[:] = []

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()