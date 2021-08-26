import configparser

config=configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class Readconfig():
    @staticmethod
    def getApplicationURL(self):
        url=config.get('common info','baseURL')


    @staticmethod
    def getUsermail(self):
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def getPassword(self):
        password = config.get('common info', 'passsword')
        return password





