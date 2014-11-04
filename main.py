from twisted.web.static import File
from klein import run, route

@route('/static/', branch=True)
def static(request):
    return File("./staticfile.txt")

run('localhost', 8080)
