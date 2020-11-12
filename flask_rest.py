from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from tweepy_get import tweepy_get
from image2video import image_to_video
import multiprocessing, time, threading, queue, os

app = Flask(__name__)
api = Api(app)

twitter_names = list()


def abort_if_todo_doesnt_exist(t_id):
    if t_id not in twitter_names:
        abort(404, message="Keyword {} doesn't exist".format(t_id))


parser = reqparse.RequestParser()
parser.add_argument('twitter_name', type=str)


class Update_Delete_Keyword(Resource):
    def get(self, t_id):
        abort_if_todo_doesnt_exist(t_id)            
        tweepy_get(t_id)
        image_to_video(t_id)
        return 'Videos has Downloaded', 201

    def delete(self, t_id):            
        abort_if_todo_doesnt_exist(t_id)
        twitter_names.remove(t_id)
        return 'Delete success', 204

    def post(self, t_id):           
        abort_if_todo_doesnt_exist(t_id)
        return twitter_names, 201

    def put(self, t_id): 
        if t_id not in twitter_names:
            twitter_names.append(t_id)
        return 'Keyword add success', 201

api.add_resource(Update_Delete_Keyword, '/twitter/<t_id>')

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 8080)


