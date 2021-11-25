"""
Сущность из БД - таблица всех пазов для диска
"""

import sqlalchemy as sa

from .base import Base
from sqlalchemy.orm import relationship


class Slots(Base):
    __tablename__ = 'Slots'
    ID = sa.Column(sa.String(), primary_key=True, autoincrement=False)
    DiskID = sa.Column(sa.String, sa.ForeignKey('Disks.ID'), nullable=False)
    measThicknessSlot= sa.Column(sa.Float)
    measAngleAxisSlot= sa.Column(sa.Float)
    measAngleSlot = sa.Column(sa.Float)
    ExternalID = sa.Column(sa.String)

    def __repr__(self):
        # для печати строки и отладки
        return '<Slots[ID="{}", DiskID="{}", measThicknessSlot="{}", measAngleAxisSlot="{}", measAngleSlot="{}", ExternalID="{}"]>'.format(
            self.ID, self.DiskID, self.measThicknessSlot, self.measAngleAxisSlot, self.measAngleSlot, self.ExternalID)