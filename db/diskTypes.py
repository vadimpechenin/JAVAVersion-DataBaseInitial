"""
Сущность из БД - таблица данных о типе диска
"""

import sqlalchemy as sa

from .base import Base
from sqlalchemy.orm import relationship


class DiskTypes(Base):
    __tablename__ = 'DiskTypes'
    ID = sa.Column(sa.String, primary_key=True, autoincrement=False)
    Name = sa.Column(sa.String)
    NumberBladesDisk = sa.Column(sa.Integer)

    def __repr__(self):
        # для печати строки и отладки
        return '<DiskTypes[ID="{}", Name="{}", NumberBladesDisk="{}"]>'.format(
            self.ID, self.Name, self.NumberBladesDisk)