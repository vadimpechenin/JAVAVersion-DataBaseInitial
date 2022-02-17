"""
Сущность из БД - таблица номинальных значений параметров для дисков
"""

import sqlalchemy as sa

from .base import Base
from sqlalchemy.orm import relationship


class ParameterDiskValues(Base):
    __tablename__ = 'ParameterDiskValues'
    ID = sa.Column(sa.String(), primary_key=True, autoincrement=False)
    DiskTypeID = sa.Column(sa.String, sa.ForeignKey('DiskTypes.ID'), nullable=False)
    ParameterDescriptionID = sa.Column(sa.String, sa.ForeignKey('ParameterDescriptions.ID'), nullable=False)
    Value = sa.Column(sa.Float)

    def __repr__(self):
        # для печати строки и отладки
        return '<ParameterValues[ID="{}", DiskTypeID="{}", ParameterDescriptionID="{}", Value="{}"]>'.format(
            self.ID, self.BladeTypeID, self.ParameterDescriptionID, self.Value)