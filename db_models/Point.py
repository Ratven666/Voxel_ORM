from sqlalchemy import Column, Integer, Float, Table, ForeignKey
from sqlalchemy.orm import relationship

from utils.create_database import Base

association_table = Table("points_scans", Base.metadata,
                          Column("point_id", Integer, ForeignKey("points.id"), primary_key=True),
                          Column("scan_id", Integer, ForeignKey("scans.id"), primary_key=True)
                          )


class Point(Base):
    __tablename__ = "points"

    id = Column(Integer, primary_key=True)
    X = Column(Float)
    Y = Column(Float)
    Z = Column(Float)
    R = Column(Integer)
    G = Column(Integer)
    B = Column(Integer)
    # nX = Column(Float)
    # nY = Column(Float)
    # nZ = Column(Float)
    scans = relationship("Scan", secondary=association_table, backref="points_scans")

    def __init__(self, coordinates: list[float], color: list[int], normals=None):
        self.X, self.Y, self.Z = coordinates
        self.R, self.G, self.B = color
        # self.nX, self.nY, self.nZ = normals

    def __str__(self):
        return f"Point [id: {self.id},\tx: {self.X} y: {self.Y} z: {self.Z},\tRGB: ({self.R},{self.G},{self.B})]"

    def __repr__(self):
        return f"Point [id: {self.id}]"
