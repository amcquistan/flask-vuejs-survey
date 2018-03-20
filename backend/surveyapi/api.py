"""
api.py
- provides the API endpoints for consuming and producing 
  REST requests and responses
"""

from flask import Blueprint, jsonify, request
from .models import db, Survey, Question, Choice

api = Blueprint('api', __name__)

@api.route('/surveys/', methods=('GET', 'POST'))
def fetch_surveys():
    if request.method == 'GET':
        surveys = Survey.query.all()
        return jsonify([s.to_dict() for s in surveys])
    elif request.method == 'POST':
        data = request.get_json()
        import pdb; pdb.set_trace()
        survey = Survey(name=data['name'])
        questions = []
        for q in data['questions']:
            question = Question(text=q['question'])
            question.choices = [Choice(text=c) for c in q['choices']]
            questions.append(question)
        survey.questions = questions
        db.session.add(survey)
        db.session.commit()
        return jsonify(survey.to_dict()), 201


@api.route('/surveys/<int:id>/', methods=('GET', 'PUT'))
def survey(id):
    if request.method == 'GET':
        survey = Survey.query.get(id)
        return jsonify(survey.to_dict())
    elif request.method == 'PUT':
        data = request.get_json()
        for q in data['questions']:
            choice = Choice.query.get(q['choice'])
            choice.selected = choice.selected + 1
        db.session.commit()
        survey = Survey.query.get(data['id'])
        return jsonify(survey.to_dict()), 201
