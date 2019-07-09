from bottle import route, run
import Dice-Roller

@route('/hello')
def hello():
    return "Hello World!"

@route('/roll')
def roll():
    return

run(host='localhost', port=8080, debug=True)