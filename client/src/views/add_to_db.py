from db import data
import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Todos(Base):
    __tablename__ = "Todos"

    description = sa.Column(sa.TEXT)
    is_completed = sa.Column(sa.Boolean)
    uid = sa.Column(sa.INTEGER, primary_key=True)

    def to_dict(self):
        return {
            "description": self.description,
            "is_completed": self.is_completed,
            "uid": self.uid
        }


engine = sa.create_engine(data)
Session = sessionmaker(engine)
session = Session()

def db_add(json):
    add = Todos(description=json['description'], is_completed=json['is_completed'])
    session.add(add)
    session.commit()
    session.close()

def form_list():
    base_list = session.query(Todos).all()
    session.close()
    return base_list

def delete_task(uid):
    task = session.query(Todos).filter(Todos.uid == uid).one()

    session.delete(task)
    session.commit()
    session.close()

def change_task(uid, task_changes):
    task = session.query(Todos).filter(Todos.uid == uid).one()
    task.description = task_changes['description']
    task.is_completed = task_changes['is_completed']

    session.commit()
    session.close()
