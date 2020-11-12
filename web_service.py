import sys
from flask import Flask, render_template, request, send_file
import os
import zipfile

application = Flask(__name__)

@application.route('/') #creates the flask html route
def root():
    return render_template('main.html')

@application.route('/', methods=['POST']) #creates the flask html route
def post():
    text1 = request.form['user1'] #getting usernames
    text2 = request.form['user2'] 
    text3 = request.form['user3']
    text4 = request.form['user4'] 
    # os.system("rm -rf img/*.png")
    # os.system("rm -rf videos/*")
    args = "python queue_test.py "+ str(text1) + " " + str(text2) + " " + str(text3) + " " + str(text4)
    os.system(args)

    zipFolder = zipfile.ZipFile('videos.zip','w', zipfile.ZIP_DEFLATED) 
    for root, directs, files in os.walk('videos/'):
        for f in files:
            print(f)
            zipFolder.write('videos/' + str(f))
    zipFolder.close()

    # os.system("rm videos/*")
    return send_file('videos.zip', mimetype ='zip', attachment_filename = 'videos.zip', as_attachment=True)

if __name__ == '__main__':
    # application.run(debug=True)
    application.run(host = '0.0.0.0', port = 80)


