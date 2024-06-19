import pymysql

db_host = 'instance-cym.cdyc0ucs6ghp.us-east-1.rds.amazonaws.com'
db_user = 'felaponte'
db_password = 'pandora0706'
db_database = 'db_cym'
db_table = 'users'

def connectionSQL():
    try:
        connection_sql = pymysql.connect(
            host = db_host,
            user = db_user,
            password = db_password,
            database = db_database
        )
        print('succesfull connection to database')
        return connection_sql
    except Exception as err:
        print('Error connecting to database')
        print (err)
        return None 

def add_user(id, name, lastname, birthday):
    instruction_sql =  "INSERT INTO " + db_table + " (id, name, lastname, birthday) Values ("+id+", '"+name+"', '"+lastname+"', '"+birthday+"')" 
    connection_sql = connectionSQL()
    try:
        if connection_sql != None:
           cursor = connection_sql.cursor()
           cursor.execute(instruction_sql)
           connection_sql.commit()
           print("user added")
           return True
        else:
            print('Error connecting to database')
            return False
    except Exception as err:
        print("Error creating the user")
        print(err)
        return False