import sys
from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop
from data.dao.UserMods import GetUser
from data.models.User import User

class UserAPI(RequestHandler):#API é um conjunto de rotinas e padrões de programação para acesso a um aplicativo de software ou plataforma baseado na Web.
    #  A sigla API refere-se ao termo em inglês "Application Programming Interface" que significa em tradução para o português "Interface de Programação de Aplicativos"

    def get(self, id):
        print(id)
        user = GetUser(id)
        self.write({'usuario': user.to_json()})

# def make_app():
#     urls = [('/api/user/([0-9]*)', UserAPI)]
#     return Application(urls)
    
# # usado para acessar um id do banco de dados via browser
# def StartServiceUser():
#     app = make_app()
#     app.listen(8001)
#     IOLoop.instance().start()

# if __name__ == "__main__":
#     StartServiceUser

def GetUrlUser():
    urls = [
        ('/api/user/([0-9]*)', UserAPI)
    ]
    return urls
