import pymysql

db_host = 'instance-cym.cdyc0ucs6ghp.us-east-1.rds.amazonaws.com'
db_user = 'felaponte'
db_password = 'pandora0706'

def connectionSQL():
    try:
        connection_sql = pymysql.connect(
            host = db_host,
            user = db_user,
            password = db_password
        )
        print('succesfull connection to database')
    except:
        print('Error connecting to database')

connectionSQL
