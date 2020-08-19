from db import data
import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import uuid


Base = declarative_base()


class Todos(Base):
    __tablename__ = "Todos"

    description = sa.Column(sa.TEXT)
    is_completed = sa.Column(sa.Boolean)
    id = sa.Column(sa.UUID, primary_key=True)
    uid = sa.Column(sa.TEXT)

    def to_dict(self):
        return {
            "description": self.description,
            "is_completed": self.is_completed,
            "uid": self.uid
        }


engine = sa.create_engine(data)
Session = sessionmaker(engine)
session = Session()

def add_task_to_db(json):
    """
    Функция добавляет POST запрос из фронтенда в базу данных
    :param json:
    :return:
    """
    add = Todos(description=json['description'], is_completed=json['is_completed'])
    session.add(add)
    session.commit()
    session.close()

def form_list():
    """
    Функция отвечает на GET запрос, фрормирует данные в список
    """
    base_list = session.query(Todos).all()
    session.close()
    return base_list

def delete_task(uid):
    """
    удаляет задачу из базы по DELETE запросу
    :param uid:
    :return:
    """
    task = session.query(Todos).filter(Todos.uid == uid).one()

    session.delete(task)
    session.commit()
    session.close()

def change_task(uid, task_changes):
    """
    Изменяет значение в базе данных по uid задачи.
    :param uid:
    :param task_changes:
    :return:
    """
    task = session.query(Todos).filter(Todos.uid == uid).one()
    task.description = task_changes['description']
    task.is_completed = task_changes['is_completed']

    session.commit()
    session.close()
