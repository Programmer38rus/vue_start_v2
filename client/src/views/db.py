import sqlalchemy as sa
import os
# import uuid

metadata = sa.MetaData()

Todos = sa.Table('Todos', metadata,
                 sa.Column('uid', sa.Integer, primary_key=True),
                 sa.Column('description', sa.Text),
                 sa.Column('is_completed', sa.Boolean),
                )


file_name = '../views/base.sqlite'

data = "sqlite:///" + file_name

if os.path.exists(file_name):
    print('File is ready...')
else:
    engine = sa.create_engine(data)
    metadata.create_all(engine)

    print('*** Data is created ***')

