from tornado.web import Application, RequestHandler 
from tornado.ioloop import IOLoop
from data.dao.RoomMods import GetRoom

class RoomAPI(RequestHandler):#API é um conjunto de rotinas e padrões de programação para acesso a um aplicativo de software ou plataforma baseado na Web.
    #  A sigla API refere-se ao termo em inglês "Application Programming Interface" que significa em tradução para o português "Interface de Programação de Aplicativos"
    
    def set_default_headers(self):
        # print("setting headers!!!")
        origin = self.request.headers.get('Origin')
        if origin:
            self.set_header('Access-Control-Allow-Origin', origin)
        
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header("Access-Control-Allow-Headers",
                        "access-control-allow-origin,authorization,content-type, grant_type, client_id, client_secret")
        self.set_header('Access-Control-Allow-Credentials', 'true')
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    def get(self, id=None):
        print(id)
        room = GetRoom(id)
        if id is not None:
            self.write({'room': room.to_json()})
        else: 
            self.write({'room': room})


def GetUrlRoom():
    urls = [
        ('/api/room/([0-9]*)', RoomAPI),
        ('/api/room', RoomAPI)
    ]
    return urls
