"""
Сущность из БД - таблица всех дисков
"""

import sqlalchemy as sa

from .base import Base
from sqlalchemy.orm import relationship


class Disks(Base):
    __tablename__ = 'Disks'
    ID = sa.Column(sa.String(), primary_key=True, autoincrement=False)
    TypeID = sa.Column(sa.String, sa.ForeignKey('DiskTypes.ID'), nullable=False)
    ProjectID = sa.Column(sa.String, sa.ForeignKey('Projects.ID'), nullable=False)

    def __repr__(self):
        # для печати строки и отладки
        return '<Disks[ID="{}", TypeID="{}", ProjectID="{}"]>'.format(
            self.ID, self.TypeID, self.ProjectID)