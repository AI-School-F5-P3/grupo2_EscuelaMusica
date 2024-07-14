from app.models import Level
from app.schemas import level_schema, levels_schema
from app.__init__ import db

def add_level(data):
    new_level = Level(**data)
    db.session.add(new_level)
    db.session.commit()
    return level_schema.jsonify(new_level)

def get_all_levels():
    levels = Level.query.all()
    return levels_schema.dump(levels)

def get_level_by_id(level_id):
    level = Level.query.get_or_404(level_id)
    return level_schema.jsonify(level)

def update_level(level_id, data):
    level = Level.query.get_or_404(level_id)
    for key, value in data.items():
        setattr(level, key, value)
    db.session.commit()
    return level_schema.jsonify(level)

def delete_level(level_id):
    level = Level.query.get_or_404(level_id)
    db.session.delete(level)
    db.session.commit()
    return level_schema.jsonify(level)
