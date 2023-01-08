from sqlalchemy import Column, Integer, Float, Table, ForeignKey
from sqlalchemy.orm import relationship

from classes.abc_classes.PointABC import PointABC
from utils.create_database import Base

points_scans_table = Table("points_scans", Base.metadata,
                           Column("point_id", Integer, ForeignKey("points.id"), primary_key=True),
                           Column("scan_id", Integer, ForeignKey("scans.id"), primary_key=True)
                           )


class PointDB(Base, PointABC):
    __tablename__ = "points"

    id = Column(Integer, primary_key=True)
    X = Column(Float)
    Y = Column(Float)
    Z = Column(Float)
    R = Column(Integer)
    G = Column(Integer)
    B = Column(Integer)
    scans = relationship("ScanDB", secondary=points_scans_table, backref="points_scans")
