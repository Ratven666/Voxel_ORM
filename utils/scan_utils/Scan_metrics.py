from sqlalchemy import and_
from sqlalchemy import func

from db_models.PointDB import PointDB, points_scans_table
from db_models.Scan import Scan
from utils.create_database import Session


def calc_scan_metrics(scan: Scan):
    with Session() as session:
        scan_metrics = session.query(func.count(PointDB.id),
                                     func.min(PointDB.X), func.max(PointDB.X),
                                     func.min(PointDB.Y), func.max(PointDB.Y),
                                     func.min(PointDB.Z), func.max(PointDB.Z))\
            .filter(and_(
            points_scans_table.c.point_id == PointDB.id,
            points_scans_table.c.scan_id == Scan.id,
            Scan.id == scan.id)).first()
        # scan_data = {"id": scan.id,
        #                 "len": scan_metrics[0],
        #                 "min_X": scan_metrics[1], "max_X": scan_metrics[2],
        #                 "min_Y": scan_metrics[3], "max_Y": scan_metrics[4],
        #                 "min_Z": scan_metrics[5], "max_Z": scan_metrics[6],
        #                 }
        scan.len = scan_metrics[0]
        scan.min_X, scan.max_X = scan_metrics[1], scan_metrics[2]
        scan.min_Y, scan.max_Y = scan_metrics[3], scan_metrics[4]
        scan.min_Z, scan.max_Z = scan_metrics[5], scan_metrics[6]
        return scan


def update_scan_in_db(updated_scan: Scan):
    with Session() as session:
        scan = session.query(Scan).get(updated_scan.id)
        scan.len = updated_scan.len
        scan.min_X, scan.max_X = updated_scan.min_X, updated_scan.max_X
        scan.min_Y, scan.max_Y = updated_scan.min_Y, updated_scan.max_Y
        scan.min_Z, scan.max_Z = updated_scan.min_Z, updated_scan.max_Z
        session.commit()


# def check_scan_borders(scan: Scan, point_data: dict):
#     if scan.min_X is None:
#         scan.min_X, scan.max_X = point_data["X"], point_data["X"]
#         scan.min_Y, scan.max_Y = point_data["Y"], point_data["Y"]
#         scan.min_Z, scan.max_Z = point_data["Z"], point_data["Z"]
#     if point_data["X"] < scan.min_X:
#         scan.min_X = point_data["X"]
#     if point_data["X"] > scan.max_X:
#         scan.max_X = point_data["X"]
#     if point_data["Y"] < scan.min_Y:
#         scan.min_Y = point_data["Y"]
#     if point_data["Y"] > scan.max_Y:
#         scan.max_Y = point_data["Y"]
#     if point_data["Z"] < scan.min_Z:
#         scan.min_Z = point_data["Z"]
#     if point_data["Z"] > scan.max_Z:
#         scan.max_Z = point_data["Z"]

