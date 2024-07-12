import logging
from db import Session
from models import Level

# Configuración básica del logger
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

db_session = Session()

def create_level(name_level):
    logging.info(f'Creando nivel: {name_level}')
    new_level = Level(name_level=name_level)
    db_session.add(new_level)
    db_session.commit()
    logging.info(f'Nivel creado exitosamente: {name_level}')
    return new_level

def get_level_by_id(level_id):
    logging.info(f'Recuperando nivel con ID: {level_id}')
    level = db_session.query(Level).filter_by(id_level=level_id).first()
    if level:
        logging.info(f'Nivel recuperado: {level.name_level}')
    else:
        logging.warning(f'Nivel con ID {level_id} no encontrado')
    return level

def update_level(level_id, new_data):
    logging.info(f'Actualizando nivel con ID: {level_id}')
    level = db_session.query(Level).filter_by(id_level=level_id).first()
    if level:
        logging.debug(f'Actualizando detalles del nivel: {level.name_level} -> {new_data["name_level"]}')
        setattr(level, 'name_level', new_data['name_level'])
        db_session.commit()
        logging.info(f'Nivel actualizado exitosamente: {level.name_level}')
    else:
        logging.warning(f'Nivel con ID {level_id} no encontrado')
    return level

def delete_level(level_id):
    logging.info(f'Borrando nivel con ID: {level_id}')
    level = db_session.query(Level).filter_by(id_level=level_id).first()
    if level:
        logging.info(f'Borrando nivel: {level.name_level}')
        db_session.delete(level)
        db_session.commit()
        logging.info(f'Nivel borrado exitosamente: {level.name_level}')
    else:
        logging.warning(f'Nivel con ID {level_id} no encontrado')
    return level

def get_all_levels():
    logging.info('Recuperando todos los niveles')
    levels = db_session.query(Level).all()
    logging.info(f'Se han recuperado {len(levels)} niveles')
    return levels

