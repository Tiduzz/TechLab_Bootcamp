from data.database import session_factory
from data.models.Report import Report
from datetime import datetime

def CreateReports(people_quantity,distance_quantity,no_mask_quantity, id_cameras):
    session = session_factory()
    today = datetime.now()
    report = Report('name',today,people_quantity,distance_quantity,no_mask_quantity, id_cameras)
    session.add(report)
    session.commit()
    session.close()

def GetReports(id=None):
    session = session_factory()
    if id is not None:
        report = session.query(Report).filter(Report.id == id).first()
    else:
        reports = list()
        report = session.query(Report).all()
        for r in report:
            reports.append(r.to_json())
        report = reports
    
    session.close()
    return report

def UpdateReports(id, name,datetime,people_quantity,distance_quantity,no_mask_quantity,id_cameras):
    session = session_factory()
    report = session.query(Report).filter(Report.id == id).first()
    report.set_valor(name)
    report.set_valor(datetime)
    report.set_valor(people_quantity)
    report.set_valor(distance_quantity)
    report.set_valor(no_mask_quantity)
    report.set_valor(id_cameras)
    session.add(report)
    session.commit()
    session.close()
    return report

def DeleteReports(id):
    session = session_factory()
    reports = session.query(Report).filter(Report.id == id).first()
    session.delete(reports)
    session.commit()
    session.close()
