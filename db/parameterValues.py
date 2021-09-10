"""
Сущность из БД - таблица номинальных значений параметров для лопаток
"""

import sqlalchemy as sa

from .base import Base
from sqlalchemy.orm import relationship


class ParameterValues(Base):
    __tablename__ = 'ParameterValues'
    ID = sa.Column(sa.String(), primary_key=True, autoincrement=False)
    BladeTypeID = sa.Column(sa.String, sa.ForeignKey('BladeTypes.ID'), nullable=False)
    ParameterDescriptionID = sa.Column(sa.Float, sa.ForeignKey('ParameterDescriprions.ID'), nullable=False)
    Value = sa.Column(sa.Float)

    def __repr__(self):
        # для печати строки и отладки
        return '<ParameterValues[ID="{}", BladeTypeID="{}", ParameterDescriptionID="{}", Value="{}"]>'.format(
            self.ID, self.BladeTypeID, self.ParameterDescriptionID, self.Value)