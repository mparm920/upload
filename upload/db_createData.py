from upload import db
import datetime
from models import Users

db.session.add(Users("mparm920@gmail.com", "mark", datetime.datetime.today(), datetime.datetime.today()))

db.session.commit()