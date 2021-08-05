import sys
from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop
from data.dao.UserTypeMods import GetUserTypeById, GetUserTypeByName
from data.models.UserType import UserType

class UserTypeAPI(RequestHandler):#API é um conjunto de rotinas e padrões de programação para acesso a um aplicativo de software ou plataforma baseado na Web.
    #  A sigla API refere-se ao termo em inglês "Application Programming Interface" que significa em tradução para o português "Interface de Programação de Aplicativos"

    def get(self, id):
        print(id)
        user = GetUserTypeByName(id)
        self.write({'tipo de usuario': user.to_json()})

# def make_app():
#     urls = [('/api/usertype/([0-9]*)', UserTypeAPI)]
#     return Application(urls)
    
# # usado para acessar um id do banco de dados via browser
# def StartServiceUserType():
#     app = make_app()
#     app.listen(8001)
#     IOLoop.instance().start()

# if __name__ == "__main__":
#     StartServiceUserType

def GetUrlUserType():
    urls = [
        ('/api/usertype/([0-9]*)', UserTypeAPI)
    ]
    return urls
