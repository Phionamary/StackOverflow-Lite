import unittest
from flask import Flask,jsonify,make_response,request
import sys
import json

from APIs.questions import app, questions 



test_entry= {
                'id': 1,
                'title': 'Question One',
                'body': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Commodi reiciendis reprehenderit repellat tenetur ipsum beatae corrupti corporis natus a fuga illum harum accusantium laborum aspernatur, sequi, ut tempora nesciunt itaque.',
                'author': 'Phii',
                'create_date': '10-09-2017'
            }
test_entry2= {
                 'id': 2,
                'title': 'Question Two',
                'body': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Commodi reiciendis reprehenderit repellat tenetur ipsum beatae corrupti corporis natus a fuga illum harum accusantium laborum aspernatur, sequi, ut tempora nesciunt itaque.',
                'author': 'Winy',
                'create_date': '30-09-2017'
            }
class all_questions_test(unittest.TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app
    

    def tearDown(self):
        questions[:] = []


    #test if all questions are displayed
    def test_get_all_questions(self):
        test_user = app.test_client(self)
        response = test_user.get("/api/v1/questions", content_type="application/json")
        self.assertEqual(response.status_code,200)

    def test_API_can_create_new_questions(self):
        test_user=app.test_client(self)
        response=test_user.post('/api/v1/questions',data=json.dumps(test_entry),content_type="application/json")
        self.assertIn('Test Content',str(response.data),msg="all questions valid")
        self.assertEqual(response.status_code,201)

    def test_API_get_particular_question(self):
    
        test_user = app.test_client(self)
        test_user.post('/api/v1/questions',data=json.dumps(test_entry),content_type="application/json")
        response = test_user.get('/api/v1/question/1',data=json.dumps(test_entry),content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Test Content', str(response.data))

    
    def test_for_wrong_single_question(self):
        test_user = app.test_client(self)
        test_user.post('/api/v1/questions',data=json.dumps(test_entry),content_type="application/json")
        response = test_user.get('/api/v1/questions/2',data=json.dumps(test_entry),content_type='application/json')
        self.assertEqual(response.status_code, 404)
        self.assertIn('not found', str(response.data))
        
if __name__ == '__main__':
    unittest.main()