from sqlalchemy import Column, Integer, Float, Table, ForeignKey
from sqlalchemy.orm import relationship

from utils.create_database import Base

points_scans_table = Table("points_scans", Base.metadata,
                           Column("point_id", Integer, ForeignKey("points.id"), primary_key=True),
                           Column("scan_id", Integer, ForeignKey("scans.id"), primary_key=True)
                           )


class PointDB(Base):
    __tablename__ = "points"

    id = Column(Integer, primary_key=True)
    X = Column(Float)
    Y = Column(Float)
    Z = Column(Float)
    R = Column(Integer)
    G = Column(Integer)
    B = Column(Integer)
    scans = relationship("Scan", secondary=points_scans_table, backref="points_scans")

    # def __init__(self, X, Y, Z, R, G, B, id_=None):
    #     self.id = id_
    #     self.X, self.Y, self.Z = X, Y, Z
    #     self.R, self.G, self.B = R, G, B
    #
    def __str__(self):
        return f"{self.__class__.__name__} [id: {self.id},\tx: {self.X} y: {self.Y} z: {self.Z},\tRGB: ({self.R},{self.G},{self.B})]"

    def __repr__(self):
        return f"{self.__class__.__name__} [id: {self.id}]"
