import random
import string
from datetime import datetime

from flask import request
from flask_restful import Resource
from sqlalchemy.orm.attributes import flag_modified

from app import db
from controllers.CollaborationController import Collaborations
from models.model_collaboration import Collaboration_Model


class CollaborationAPI(Resource):

    def get(self):
        """ GET method for Collaboration API. """
        collaborate = Collaborations()
        result = collaborate.get_response_for_api()
        if result['response']:
            return result, 200
        elif result['status_code'] == 401:
            return result, 401
        return result, 202


class CommentWrite(Resource):

    def post(self):
        """ POST method for CommentWrite API. """
        if request.method == 'POST':
            if request.is_json:
                payload = request.get_json()
                data = Collaboration_Model.query.filter_by(supply_id=payload['supply_id']).first()
                results = {
                    "recruiter_name": 'H-Edge-Recruiter',
                    "comment_id": ''.join(random.choices(string.ascii_uppercase + string.digits, k=6)),
                    "comments": payload['comments'],
                    "commented_on": datetime.strftime(datetime.now(), "%d-%m-%Y %T")
                }
                if data:
                    if data.comments:
                        data.comments.append(results)
                    flag_modified(data, "comments")
                    db.session.add(data)
                    db.session.commit()
                    return {'response': 'success',
                            "message": f"Supply_id: {data.supply_id} has been updated successfully."
                            }, 201
                else:
                    data = Collaboration_Model(
                        supply_id=payload['supply_id'],
                        comments=[results],
                        demand_id=payload['demand_id'],
                        is_hide=payload['is_hide'],
                        add_members=payload['add_members']
                    )
                    db.session.add(data)
                    db.session.commit()
                    return {'response': 'success',
                            "message": f"Supply_id: {data.supply_id} has been created successfully."
                            }, 201
            else:
                return {"error": "The request payload is not in JSON format"}, 202


class CommentReadUpdateDelete(Resource):

    def get(self):
        """ GET method for CommentRead API. """
        supply_id = request.args.get('supply_id')
        data = db.session.query(Collaboration_Model).filter_by(supply_id=supply_id).first()
        if data:
            if request.method == 'GET':
                response = {
                    'supply_id': data.supply_id,
                    'comments': data.comments,
                    'demand_id': data.demand_id,
                    'is_hide': data.is_hide,
                    'add_members': data.add_members
                }
                return {'response': True, 'results': [response]}, 200
        return {'response': False, 'message': 'Supply_Id Not Found'}, 202

    def put(self):
        """ PUT method for Comment Modified API. """
        supply_id = request.args.get('supply_id')
        results = db.session.query(Collaboration_Model).filter_by(supply_id=supply_id).first()
        if results:
            if request.method == 'PUT':
                if request.is_json:
                    data = request.get_json()
                    results.supply_id = data['supply_id']
                    results.comments = data['comments']
                    results.demand_id = data['demand_id']
                    results.is_hide = data['is_hide']
                    results.add_members = data['add_members']
                    db.session.add(results)
                    db.session.commit()
                    return {'response': 'success',
                            "message": f"Supply_id: {results.supply_id} has been updated successfully."}, 201
                return {"error": "The request payload is not in JSON format"}, 400
        return {'response': False, 'message': 'Supply_id Not Found'}, 202

    def delete(self):
        """ DELETE method for Comment Delete API. """
        supply_id = request.args.get('supply_id')
        comment_id = request.args.get('comment_id')
        query = db.session.query(Collaboration_Model).filter_by(supply_id=supply_id).first()
        if query:
            if query.comments:
                for comments in query.comments:
                    if comments.get('comment_id') == comment_id:
                        query.comments.remove(comments)
            flag_modified(query, "comments")
            db.session.add(query)
            db.session.commit()
            return {'response': f"Comment_Id: {comment_id} deleted successfully"}, 201
        return {'response': False, 'message': 'Supply_Id for Comment Not Found.'}, 202


class FeedbackRead(Resource):

    def get(self):
        """ GET method for Feedback Read API. """
        supply_id = request.args.get('supply_id')
        data = db.session.query(Collaboration_Model).filter_by(supply_id=supply_id).first()
        if data:
            results = list()
            if data.feedback:
                results = data.feedback
            return {'response': True, 'results': results}, 200
        return {'response': False, 'message': 'Supply_Id for Feedback Not Found.'}, 202

    def delete(self):
        """ DELETE method for Feedback Delete API. """
        supply_id = request.args.get('supply_id')
        feedback_id = request.args.get('feedback_id')
        query = db.session.query(Collaboration_Model).filter_by(supply_id=supply_id).first()
        if query:
            if query.feedback:
                for feedback in query.feedback:
                    if feedback.get('feedback_id') == feedback_id:
                        query.feedback.remove(feedback)
            flag_modified(query, "feedback")
            db.session.add(query)
            db.session.commit()
            return {'response': "Feedback deleted successfully"}, 201
        return {'response': False, 'message': 'Supply_Id for Feedback Not Found.'}, 202


class FeedbackWrite(Resource):

    def post(self):
        """ POST method for Feedback Write API. """
        supply_id = request.args.get('supply_id')
        feedback = request.get_json("feedback")
        query = db.session.query(Collaboration_Model).filter_by(supply_id=supply_id).first()
        if query:
            results = {
                "feedback_id": ''.join(random.choices(string.ascii_uppercase + string.digits, k=6)),
                "feedback": feedback,
                "feedback_date": datetime.now().strftime("%d/%m/%Y %H:%m:%d")
            }
            if not query:
                query = Collaboration_Model(
                    feedback=[results],
                    comments=[],
                    supply_id=supply_id,
                )
            else:
                if query.feedback:
                    query.feedback.append(results)
                else:
                    query.feedback = [results]
                flag_modified(query, "feedback")
            query.supply_id = supply_id
            db.session.add(query)
            db.session.commit()
            return {'response': 'success', 'message': 'Feedback has been added successfully.'}, 201
        return {'response': False, 'message': 'Supply_Id for Feedback Not Found.'}, 202
