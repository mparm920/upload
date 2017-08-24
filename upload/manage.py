from upload import db, app
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app.secret_key = 'eflex upload page'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///upload.db' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()