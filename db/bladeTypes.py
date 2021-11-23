"""
Сущность из БД - таблица данных о типе лопатке
"""

import sqlalchemy as sa

from .base import Base
from sqlalchemy.orm import relationship


class BladeTypes(Base):
    __tablename__ = 'BladeTypes'
    ID = sa.Column(sa.String, primary_key=True, autoincrement=False)
    Name = sa.Column(sa.String)
    #NumberBladesDisk = sa.Column(sa.Integer)
    TypeDiskID = sa.Column(sa.String, sa.ForeignKey('DiskTypes.ID'), nullable=False)

    def __repr__(self):
        # для печати строки и отладки
        return '<BladeTypes[ID="{}", Name="{}", TypeDiskID="{}"]>'.format(
            self.ID, self.Name, self.TypeDiskID)