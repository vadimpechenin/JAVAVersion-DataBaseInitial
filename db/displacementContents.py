"""
Сущность из БД - таблица про перестановки
"""

import sqlalchemy as sa

from .base import Base
from sqlalchemy.orm import relationship


class DisplacementContents(Base):
    __tablename__ = 'DisplacementContents'
    ID = sa.Column(sa.String(), primary_key=True, autoincrement=False)
    DisplacementID = sa.Column(sa.String, sa.ForeignKey('Displacements.ID'), nullable=False)
    BladeID = sa.Column(sa.String, sa.ForeignKey('Blades.ID'), nullable=False)
    #Position = sa.Column(sa.Integer)
    SlotID = sa.Column(sa.String, sa.ForeignKey('Slots.ID'), nullable=False)

    def __repr__(self):
        # для печати строки и отладки
        return '<DisplacementContents[ID="{}", DisplacementID="{}", BladeID="{}", SlotID="{}"]>'.format(
            self.ID, self.DisplacementID, self.BladeID, self.SlotID)