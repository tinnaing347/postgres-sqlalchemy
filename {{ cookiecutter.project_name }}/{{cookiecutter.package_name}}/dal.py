from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.exc import IntegrityError

from contextlib import contextmanager

import logging
l = logging.getLogger(__name__)


class DataAccessLayer(object):
    '''
    Base class for Database API objects - manages transactions, sessions and holds a reference to the engine.
    Acts as a simple session context manager and creates a uniform API for querying using the ORM


    This class could be thought of as a singleton factory. 
    Applications should only ever use one instance per database.

    Example:
        dal = DataAccessLayer()
        dal.connect(engine_url=..., engine_echo=False)
    '''

    def __init__(self, BaseModel):

        self.engine = None
        self.Session = None
        self.Base = BaseModel


    def connect(self, engine_url, engine_echo=True, with_create=True):
        ''' Builds engine and Session class for app layer
        if_drop==True then drop existing tables and rebuild schema
        '''
        self.engine = create_engine(engine_url, echo=engine_echo)
        self.Session = scoped_session(sessionmaker(bind=self.engine)) #NOTE extra config can be implemented in this call to sessionmaker factory


    @contextmanager
    def transaction(self):
        """this method safely wraps a session object in a transactional scope
        used for basic create, select, update and delete procedures
        """
        session = self.Session()

        try:
            yield session
            session.commit()

        except Exception as e:
            l.error(e)
            session.rollback()
            l.warn('session rolled back')
            raise

        finally:
            session.close()
            l.info('session closed')

    def bulk_insert(self, records):
        """ performs a bulk insert on a list of records 
        
        Arguments:
            records {list} -- obj records in list of dicts format 
        """
        with self.transaction() as session:
            session.bulk_save_objects(records)
    

    def safe_append(self, records, keep_errors=True):
        '''Performs a 'safe append' of an object where integrity errors are 
        caught and the db rolled back. 
        
        Arguments:
            records {list} -- obj records in list of dict format 
        
        Keyword Arguments:
            keep_errors {bool} -- will keep any error records for the user (default: {True})
        
        Returns:
            error_records, error_messages -- a tuple of lists with errors from the append  
        '''

        error_messages = []
        error_records = []
        for rec in records:
            try:
                with self.transaction() as session:
                    l.info('inserting record: {}'.format(rec))
                    session.add(rec)
            
            except IntegrityError as err:
                l.error('An integrity error was reported for facility')
                error_messages.append(err.args)  # append message and errors
                error_records += [rec]
                continue 
        
        return error_records, error_messages


    def get_session(self):
        '''returns a session to the caller
        '''
        return self.Session()
    
    def set_base_model(self, BaseModel):
        self.Base = BaseModel


    def reset_db(self):
        """ destroys the database
        """
        self.Base.metadata.drop_all(self.engine)


    def create_all(self):
        """ creates the database 
        """
        self.Base.metadata.create_all(self.engine)


    def drop_table(self, Model):
        """ Attempts to drop the specified table from db 
        """
        Model.__table__.drop(self.engine)


