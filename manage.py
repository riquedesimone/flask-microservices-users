import unittest

from flask_script import Manager
from project import db, create_app
from project.api.models import User

app = create_app()
manager = Manager(app)


@manager.command
def recreate_db():
    """Recreates a database."""
    db.drop_all()
    db.create_all()
    db.session.commit()


@manager.command
def seed_db():
    """Seeds the database."""
    db.session.add(User(username='henrique', email="eu@henriquedesimone.com.br"))
    db.session.add(User(username='henriquedesimone', email="henrique.desimone@hfocus.com.br"))
    db.session.commit()


@manager.command
def test():
    """Runs the tests without code coverage"""
    tests = unittest.TestLoader().discover('project/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)

    if result.wasSuccessful():
        return 0

    return 1


if __name__ == '__main__':
    manager.run()
