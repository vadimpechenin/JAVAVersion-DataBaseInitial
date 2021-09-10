"""
Сущность из БД - таблица проектов
"""

import sqlalchemy as sa

from .base import Base
from sqlalchemy.orm import relationship

class Projects(Base):
    __tablename__ = 'Projects'
    ID = sa.Column(sa.String, primary_key=True, autoincrement=False)
    Description = sa.Column(sa.String)

    def __repr__(self):
        # для печати строки и отладки
        return '<Projects[ID="{}", Description="{}"]>'.format(
            self.ID, self.Description)