from .entities.User import User

class ModelUser():

    @classmethod
    def register(cls,db, user):
        
        try:
            hashed_password = User.generate_hash(user.password)
            cur = db.connection.cursor()
            cur.execute("INSERT INTO users VALUES(NULL,%s,%s,%s)", (user.email,hashed_password,user.fullname))
            db.connection.commit()

        except Exception as e:
            print(e)

    @classmethod
    def login(cls,db,user):
        
        try:
            cur = db.connection.cursor()
            cur.execute("SELECT * FROM users WHERE email=%s",(user.email,))
            datos = cur.fetchone()

            if datos:
                
                id = datos[0]
                email = datos[1]
                password = User.check_password(datos[2],user.password)
                fullname = datos[3]
                
                if password:
                    user = User(id,email,password,fullname)
                    return user
                
                return "password no validad"
            return "Correo no valido"
        
        except Exception as e:
            print(e)
    
    @classmethod
    def get_by_id(cls,db,id):
        try:
            cur = db.connection.cursor()
            cur.execute("SELECT id, fullname, email FROM users WHERE id = %s", (id,))
            datos = cur.fetchone()
            if datos:
                id = datos[0]
                fullname = datos[1]
                email = datos[2]
            
                logged_user = User(id,email,None,fullname)   

                return logged_user
            else:
                return None
        
        except Exception as e:
            print(e)

    @classmethod
    def addcontacts(cls,db,fullname,telefono,user_id):
        try:
            cur = db.connection.cursor()
            cur.execute("INSERT INTO contacts VALUES(NULL,%s,%s,%s)", (fullname,telefono,user_id))
            db.connection.commit()

        except Exception as e:
            print(e)

    @classmethod
    def getcontacts(cls,db,user_id):
        try:
            cur = db.connect.cursor()
            cur.execute("SELECT id,fullname,number FROM contacts WHERE user_id = %s",(user_id,))
            data = cur.fetchall()
            if data:
                return data
            return None
        
        except Exception as e:
            print(e)