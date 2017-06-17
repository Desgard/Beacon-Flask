#!/usr/bin/env python

import os
from app import create_app, db
from app.models import Types, Videos, Users, UserVideoRelation, Histories
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app = app, db = db, Types = Types, Videos = Videos, Users = Users,
                UserVideoRelation = UserVideoRelation, Histories = Histories)

manager.add_command("shell", Shell(make_context = make_shell_context))
manager.add_command("db", MigrateCommand)

@manager.command
def clearAlembic():
    from flask_migrate import upgrade
    from app.models import Alembic
    Alembic.clear_A()

if __name__ == '__main__':
    manager.run()