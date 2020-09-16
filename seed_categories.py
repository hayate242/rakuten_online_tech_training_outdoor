from models.database import db_session

"""[categories seeder]
"""
from models.models import Categories
# categories
db_session.add(
    Categories(
        '',
        'Healty Food'
    )
)
db_session.add(
    Categories(
        '',
        'Exercise Equipment'
    )
)
db_session.add(
    Categories(
        '',
        'Hygiene Products'
    )
)
db_session.add(
    Categories(
        '',
        'Daily Goods'
    )
)
db_session.add(
    Categories(
        '',
        'Books'
    )
)
db_session.commit()
