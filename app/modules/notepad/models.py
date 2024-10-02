from app import db


# Definición de la tabla NOTEPAD en la base de datos
class Notepad(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256), nullable=False)
    body = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    # backref (relación bidireccional)
    # Relación unidireccional: user = db.relationship('User')
    # lazy=True: solo cargará los datos relacionados cuando se acceda a ellos
    # lazy='joined': carga inmediata
    # lazy='subquery': los datos relacionados se cargan con una consulta separada
    # lazy='dynamic': no carga los datos relacionados inmediatamente, sino que devuelve una 
    # consulta que se puede filtrar o ejecutar más tarde
    user = db.relationship('User', backref='notepads', lazy=True)

    # Representación de una instancia NOTEPAD
    def __repr__(self):
        return f'Notepad<{self.id}, Title={self.title}, Author={self.user.username}>'
