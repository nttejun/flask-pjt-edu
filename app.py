from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from eduBoard import *

@app.route('/board', methods=['GET'])
def board():
    return render_template('board.html')
 
@app.route('/board/lists', method=['GET'])
def readBoardLists():
    return render_template('board.html')

@app.route('/board/lists', method=['POST'])
def createBoard():
    return ''

@app.route('/board/lists/<int:no>', method=['PUT'])
def updateBoard():
    return ''

@app.route('/board/lists/<int:no>', method=['DELETE'])
def deleteBoard():
    return ''

if __name__ == '__main__':
    app.run(debug = True)