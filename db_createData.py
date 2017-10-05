from project import db
import datetime
from project.models import Users, Companies

db.session.add(Companies("Hirata"))
db.session.add(Companies("Hanwha"))
db.session.add(Companies("MCM"))
db.session.add(Companies("Cinetics/Fives"))

db.session.commit()

db.session.add(Users("mparm920@gmail.com", "mark", "Hirata"))

db.session.commit()