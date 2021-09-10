"""
Сущность из БД - таблица пояснений к перестановкам
"""

import sqlalchemy as sa

from .base import Base
from sqlalchemy.orm import relationship


class Displacements(Base):
    __tablename__ = 'Displacements'
    ID = sa.Column(sa.String(), primary_key=True, autoincrement=False)
    ProjectID = sa.Column(sa.String, sa.ForeignKey('Projects.ID'), nullable=False)
    DisplacementType = sa.Column(sa.Integer)

    def __repr__(self):
        # для печати строки и отладки
        return '<Displacements[ID="{}", ProjectID="{}", DisplacementType="{}"]>'.format(
            self.ID, self.ProjectID, self.DisplacementType)