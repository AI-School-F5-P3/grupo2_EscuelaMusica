from config import Session
from models import Level

db_session = Session()

def create_level(name_level):
    new_level = Level(name_level=name_level)
    db_session.add(new_level)
    db_session.commit()
    return new_level

def get_level_by_id(level_id):
    return db_session.query(Level).filter_by(id_level=level_id).first()

def update_level(level_id, new_data):
    level = db_session.query(Level).filter_by(id_level=level_id).first()
    if level:
        setattr(level, 'name_level', new_data['name_level'])
        db_session.commit()
    return level

def delete_level(level_id):
    level = db_session.query(Level).filter_by(id_level=level_id).first()
    if level:
        db_session.delete(level)
        db_session.commit()
    return level

def get_all_levels():
    return db_session.query(Level).all()