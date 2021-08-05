#o que mudar com as recomendacoes do Huge e andenson aqui nesta parte do codigo
#adicionar um banco tipos para controlar o user types
#colocar os tipos de dados na tabela, mudar a tabalea adm para user
#usertype para small int
#tabela de relacionamento de camera para reports, pricipalmente com cameras
#mudar os caminhos na parte de Web

import asyncio
from data.database import session_factory
#implantados ate agora no cogigo
    #Camera
    #FaceRecogniton, precisa ser atualizado
    #Report
    #Room 
    #User
    #UserType
    #NotificationSetting
#composicao dos tipos de arquivos:
    #data.dao."Type"Mods, operacoes principais do CRUD:
        #Create: criacao de novos itens
        #Get:recuperacao de itens existentes utilizando Id //PARA USERTYPE USAR GetUserTypeById OU GetUserTypeByName
        #Update: modificaos do iten ja existente
        #Delet: apagar itens ja existentes
    #service."Type"Web, operacoes no tornado/navegador
        #GetUrl: inicia o tornado/navegador do tipo

from data.dao.CameraMods import CreateCamera, GetCamera, UpdateCamera, DeleteCamera
from service.CamerasWeb import GetUrlCameras 

from service.FaceRecognitionWeb import GetUrlFaceRecognition, GetUrlFaceRecognitionFrame

from data.dao.ReportMods import CreateReports, GetReports, UpdateReports, DeleteReports
from service.ReportsWeb import GetUrlReport

from data.dao.RoomMods import CreateRoom, GetRoom, UpdateRoom, DeleteRoom
from service.RoomWeb import GetUrlRoom

from data.dao.UserMods import CreateUser, GetUser, UpdateUser, DeleteUser
from service.UserWeb import GetUrlUser

from data.dao.UserTypeMods import CreateUserType, GetUserTypeByName, GetUserTypeById, UpdateUserType, DeleteUserType
from service.UserTypeWeb import GetUrlUserType

from data.dao.NotificationSettingMods import CreateNotificationsSetting, GetNotificationsSetting, UpdateNotificationsSetting, DeleteNotificationsSetting
from service.NotificationSettingWeb import GetUrlNotificationSetting

from tornado.web import Application
from tornado.ioloop import IOLoop

#usado para comunicacao e browser
def make_app():
    urls = list()
    urls.extend([*GetUrlCameras()])
    urls.extend([*GetUrlFaceRecognition()])
    urls.extend([*GetUrlFaceRecognitionFrame()])
    urls.append(*GetUrlNotificationSetting())
    urls.extend([*GetUrlReport()])
    urls.extend([*GetUrlRoom()])
    urls.append(*GetUrlUser())
    urls.append(*GetUrlUserType())
    return Application(urls)

#main, parte em loop e corpo do codigo    
if __name__ == "__main__":

    #ordem de chamada ideal
    # 
    #CreateRooms('')
    #CreateCamera('')
    #CreateReports('')
    # 
    #CreateUserType('')
    #CreateNotificationSetting('')
    #CreateUser('')

    #CreateRoom('sala 1', 10)
    #CreateCamera('camera 1',1)
    #CreateReports('relatorio 1',1,1)
    #CreateUserType('tipo 1', '0-0',0,0,0,0,0,0,0,0,0,0)
    #CreateNotificationsSetting(0,0,0,0,0,0,0,0,0,0)
    #CreateUser('joao','joao@jao',123456, 1,1)

    #CreateRoom('sala 2', 20)
    #CreateCamera('camera 2',2)
    #CreateReports('relatorio 2',2,2)
    #CreateUserType('tipo 2', '0-1',1,0,0,0,0,0,0,0,0,0)
    #CreateNotificationsSetting(0,0,0,0,0,0,0,0,0,1)
    #CreateUser('jose','jose@jse',123456, 2,2)

    #CreateRoom('sala 3', 30)
    #CreateCamera('camera 3',3)
    #CreateReports('relatorio 3',3,3)
    #CreateUserType('tipo 3', '0-3',1,1,0,0,0,0,0,0,0,0)
    #CreateNotificationsSetting(0,0,0,0,0,0,0,0,1,1)
    #CreateUser('jario','jario@jio',123456, 3,3)

    #CreateRoom('sala 4', 40)
    #CreateCamera('camera 4',4)
    #CreateReports('relatorio 4',4,4)
    #CreateUserType('tipo 4', '0-4',1,1,1,0,0,0,0,0,0,0)
    #CreateNotificationsSetting(0,0,0,0,0,0,0,1,1,1)
    #CreateUser('maria','maria@mar',123456, 4,4)

    # CreateRoom('sala 5', 50)
    # CreateCamera('camera 5',5)
    # CreatReports('relarorio 5',5,5)
    # CreateUserType('tipo 5', '0-5',1,1,1,1,0,0,0,0,0,0)
    # CreateNotificationsSetting(0,0,0,0,0,0,1,1,1,1)
    # CreateUser('jorge','jorge@jge',123456, 5,5)

    # StartServiceCamera()
    # StartServiceReport()
    # StartServiceRoom()
    # StartServiceUser()
    # StartServiceUserType()
    # StartServiceNotificationSetting()

    app = make_app()
    app.listen(8000)
    IOLoop.instance().start()


    
