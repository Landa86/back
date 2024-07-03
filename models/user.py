from extensions import db

class User(db.Model):
    __tablename__= "users"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80),nullable = False, unique = False)
    sex = db.Column(db.String(10))
    email = db.Column(db.String(200),nullable = False, unique = True)
    created_at =db.Coloumn(db.DateTime(),nullable = False, server_default=db.func.now())
    update_at =db.Coloumn(db.DateTime(),nullable = False, server_default=db.func.now(),onupdate=db.func.now())
    
    @property
    def data(self):
        return{
            "id":self.id,
            "name":self.name,
            "sex":self.sex,
            "email":self.email
        }
        
    def save(self):
        db.session.add(self)
        db.session.commit()
        
        
    @classmethod
    def get_all(cls):
        r = cls.query.all()
        result = []
        
        for i in r:
            result.append(i.data)
        return result
    
    @classmethod
    def get_by_id(cls,id):
        return cls.query.filter(cls.id == id).first()
