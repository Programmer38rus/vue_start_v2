import sqlalchemy as sa

metadata = sa.MetaData()

Todos = sa.Table('Todos', metadata,
                 sa.Column('id', sa.Integer, primary_key=True),
                 sa.Column('description', sa.Text),
                 sa.Column('is_complite', sa.Boolean),
                )

print('Loading db file...')
