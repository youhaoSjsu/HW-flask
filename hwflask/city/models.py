from city import db
class City(db.Model):
    id= db.Column(db.Integer,primary_key= True)
    names = db.Column(db.String(20), unique=True, nullable=False)
    ranks = db.Column(db.Integer, unique=True, nullable=False)
    visted = db.Column(db.Boolean, nullable=False, default=False)
    def __repr__(self):
             return f"City('{self.names}', {self.ranks}, {self.visited})"

