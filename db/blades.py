"""
Сущность из БД - таблица всех измеренных значений для лопаток
"""

import sqlalchemy as sa

from .base import Base
from sqlalchemy.orm import relationship


class Blades(Base):
    __tablename__ = 'Blades'
    ID = sa.Column(sa.String(), primary_key=True, autoincrement=False)
    TypeID = sa.Column(sa.String, sa.ForeignKey('BladeTypes.ID'), nullable=False)
    MeasThickness = sa.Column(sa.Float)
    MeasAngle= sa.Column(sa.Float)
    ExternalID = sa.Column(sa.String)
    ProjectID = sa.Column(sa.String, sa.ForeignKey('Projects.ID'), nullable=False)

    def __repr__(self):
        # для печати строки и отладки
        return '<Blades[ID="{}", TypeID="{}", MeasThickness="{}", MeasAngle="{}", ExternalID="{}", ProjectID="{}"]>'.format(
            self.ID, self.TypeID, self.MeasThickness, self.MeasAngle, self.ProjectID)