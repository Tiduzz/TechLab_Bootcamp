import sys
from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop
from data.dao.NotificationSettingMods import GetNotificationsSetting
from data.models.NotificationSetting import NotificationSetting

class NotificationSettingAPI(RequestHandler):#API é um conjunto de rotinas e padrões de programação para acesso a um aplicativo de software ou plataforma baseado na Web.
    #  A sigla API refere-se ao termo em inglês "Application Programming Interface" que significa em tradução para o português "Interface de Programação de Aplicativos"

    def get(self, id):
        print(id)
        user = NotificationSetting(id)
        self.write({'configuracao de usuario': user.to_json()})


def GetUrlNotificationSetting():
    urls = [
        ('/api/notificationsetting/([0-9]*)', NotificationSettingAPI)
    ]
    return urls
