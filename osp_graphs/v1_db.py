

import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.automap import automap_base


# TODO: Config-ify.
url = URL(drivername='postgresql', database='osp_graphs')

engine = create_engine(url)

factory = sessionmaker(bind=engine)

session = scoped_session(factory)

Base = automap_base()

Base.prepare(engine, reflect=True)

Text = Base.classes.text
Citation = Base.classes.citation
Field = Base.classes.field
Subfield = Base.classes.subfield
SubfieldDocument = Base.classes.subfield_document
Document = Base.classes.document
