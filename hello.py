from bottle import route, run, template
from misc import add

@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)



@route('/add/<n>/<m>')
@route('/add/<n>/<m>/')
def route_add(n, m):
    return {'result': add(n, m)}



run(host='localhost', port=8080)