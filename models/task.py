"""
Modelo Task - Representa una tarea en la base de datos

Este archivo contiene la definición del modelo Task usando SQLAlchemy ORM.
"""

from datetime import datetime
from app import db


class Task(db.Model):
    """
    Modelo para representar una tarea en la aplicación To-Do
    """
    
    # Nombre de la tabla en la base de datos
    __tablename__ = 'tasks'
    
    # Definición de columnas
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=True)
    completed = db.Column(db.Boolean, default=False, nullable=False)
    due_date = db.Column(db.DateTime, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    
    def __init__(self, title, description=None, due_date=None):
        """
        Constructor del modelo Task
        
        Args:
            title (str): Título de la tarea
            description (str, optional): Descripción de la tarea
            due_date (datetime, optional): Fecha de vencimiento
        """
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = False
    
    def __repr__(self):
        """Representación en string del objeto Task"""
        return f'<Task {self.id}: {self.title}>'
    
    def to_dict(self):
        """
        Convierte el objeto Task a un diccionario

        Returns:
            dict: Diccionario con los datos de la tarea
        """
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'completed': self.completed,
            'due_date': self.due_date.isoformat() if self.due_date else None,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

    def is_overdue(self):
        """
        Verifica si la tarea está vencida
        
        Returns:
            bool: True si la tarea está vencida, False en caso contrario
        """
         # TODO: implementar el método
        return self.due_date is not None and self.due_date < datetime.utcnow() and not self.completed
    
    def mark_completed(self):
        """Marca la tarea como completada"""
        # TODO: implementar el método
        self.completed = True
        self.updated_at = datetime.utcnow()
    
    def mark_pending(self):
        """Marca la tarea como pendiente"""
     # TODO: implementar el método
        self.completed = False
        self.updated_at = datetime.utcnow()
    
    @staticmethod
    def get_all_tasks():
        """
        Obtiene todas las tareas de la base de datos
        
        Returns:
            list: Lista de objetos Task
        """
        return Task.query.all()
    
    @staticmethod
    def get_pending_tasks():
        """
        Obtiene todas las tareas pendientes
        
        Returns:
            list: Lista de tareas pendientes
        """
        # TODO: implementar el método
        return Task.query.filter_by(completed=False).order_by(Task.due_date.asc()).all()
    
    @staticmethod
    def get_completed_tasks():
        """
        Obtiene todas las tareas completadas
        
        Returns:
            list: Lista de tareas completadas
        """
     # TODO: implementar el método
        return Task.query.filter_by(completed=True).order_by(Task.completed_at.desc()).all()
    
    @staticmethod
    def get_overdue_tasks():
        """
        Obtiene todas las tareas vencidas
        
        Returns:
            list: Lista de tareas vencidas
        """
     # TODO: implementar el método
        return Task.query.filter(Task.due_date < datetime.utcnow(),Task.completed == False.order_by(Task.due_date.asc()).all())
    
    def save(self):
        """Guarda la tarea en la base de datos"""
     # TODO: implementar el método
        db.session.add(self)
        db.session.commit()
     
    
    def delete(self):
        """Elimina la tarea de la base de datos"""
    # TODO: implementar el método
        db.session.delete(self)
        db.session.commit()

