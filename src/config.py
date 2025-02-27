import os
class Config:
    SECRET_KEY=os.getenv('SECRET_KEY')



class ProduConfig(Config):
    DEBUG=False
    MYSQL_HOST=os.getenv('MYSQL_HOST')
    MYSQL_USER=os.getenv('MYSQL_USER')
    MYSQL_PASSWORD=os.getenv('MYSQL_PASSWORD')
    MYSQL_DB=os.getenv('MYSQL_DB')


class Development(Config):
    DEBUG=True
    MYSQL_HOST=os.getenv('MYSQL_HOST')
    MYSQL_USER=os.getenv('MYSQL_USER')
    MYSQL_PASSWORD=os.getenv('MYSQL_PASSWORD')
    MYSQL_DB=os.getenv('MYSQL_DB')




config = {
    "Develop" : Development,
    "produc" : ProduConfig
}
