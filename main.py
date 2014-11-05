from twisted.web.static import File
from klein import run, route

@route('/static/', branch=True)
def static(request):
    file = File("./staticfile.txt")
    file.isLeaf = True
    return file

run('localhost', 8080)
