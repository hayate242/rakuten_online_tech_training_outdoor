from models.database import db_session

"""[categories seeder]
"""
from models.models import Categories
# categories
db_session.add(
    Categories(
        '健康',
        'Healty Food'
    )
)
db_session.add(
    Categories(
        '健康器具',
        'Exercise Equipment'
    )
)
db_session.add(
    Categories(
        '日用品',
        'Hygiene Products'
    )
)
db_session.add(
    Categories(
        '生活用品',
        'Daily Goods'
    )
)
db_session.add(
    Categories(
        'ヘルスケア本',
        'Books'
    )
)
db_session.commit()
