from flask import Flask, jsonify
import os

app = Flask(__name__)

courses = [{'name': "Python Programming Certification",
            'course_id': "0",
            'Description': "Python programming certification helps you learn"
                           "python in the structured learning path with innovative"
                           "out of the box projects matching the industry standards",
            'price': "visit online to get more details"},
           {'name': "Data Science with Python Certification",
            'course_id': "1",
            'Description': "Python programming certification helps you learn"
                           "python in the structured learning path with innovative"
                           "out of the box projects matching the industry standards",
            'price': "visit online to get more details"},

           {'name': "AI and Machine Learning Certification",
            'course_id': "2",
            'Description': "Python programming certification helps you learn"
                           "python in the structured learning path with innovative"
                           "out of the box projects matching the industry standards",
            'price': "visit online to get more details"},

           {'name': "DevOps Certification",
            'course_id': "3",
            'Description': "Python programming certification helps you learn"
                           "python in the structured learning path with innovative"
                           "out of the box projects matching the industry standards",
            'price': "visit online to get more details"},
           ]


@app.route('/')
def index():
    return "Welcome to the course API"


@app.route("/courses", methods=['GET'])
def get():
    return jsonify({'Courses': courses})

@app.route("/courses/<int:course_id>",methods=['GET'])
def get_course(course_id):
    return jsonify({'course': courses[course_id]})

@app.route("/courses", methods=['POST'])
def create():
    course = {'name': "Natural Language Processing with Python Certification",
            'course_id': "4",
            'Description': "Python programming certification helps you learn"
                           "python in the structured learning path with innovative"
                           "out of the box projects matching the industry standards",
            'price': "visit online to get more details"}
    courses.append(course)
    return jsonify({'Created': course})

@app.route("/courses/<int:course_id>",methods=['PUT'])
def course_update(course_id) :
    courses[course_id]['Description'] = "Natural language processing (NLP) refers to the branch of computer science—and more specifically, the branch of artificial intelligence  giving computers the ability to understand text and spoken words in much the same way human beings can."
    return jsonify({'course': courses[course_id]})

@app.route("/courses/<int:course_id>",methods=['DELETE'])
def delete(course_id):
    courses.remove(courses[course_id])
    return jsonify({'result': True})

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)