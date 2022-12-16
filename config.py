import os

basedir = os.path.abspath(os.path.dirname(__file__))

# create environment variables that Flask will need access to later on
class Config():
    """
    We will set Config variables for the Flask App here.
    Using Environment variables where available, otherwise
    we will create the confir variable(s) if not already done
    """

    # SECRET_KEY allows us to use forms inside of flask
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'You will never guess...'
    
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEPLOY_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')

    SQLALCHEMY_TRACK_MODIFICATIONS = False #Turn off update messages from the database