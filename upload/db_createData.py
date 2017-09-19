from upload import db
import datetime
from models import Users, Companies

db.session.add(Users("mparm920@gmail.com", "mark"))

db.session.add(Companies("Hirata"))
db.session.add(Companies("Hanwha"))
db.session.add(Companies("MCM"))
db.session.add(Companies("Cinetics/Fives"))

db.session.commit()