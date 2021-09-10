"""
Сущность из БД - таблица пояснений для параметров
"""

import sqlalchemy as sa

from .base import Base
from sqlalchemy.orm import relationship


class ParameterDescriptions(Base):
    __tablename__ = 'ParameterDescriptions'
    ID = sa.Column(sa.String(), primary_key=True, autoincrement=False)
    SystemName = sa.Column(sa.String)
    DisplayName = sa.Column(sa.String)

    def __repr__(self):
        # для печати строки и отладки
        return '<ParameterDescriptions[ID="{}", SystemName="{}", DisplayName="{}"]>'.format(
            self.ID, self.SystemName, self.DisplayName)