from os.path import abspath, dirname, join


_cwd = dirname(abspath(__file__))


class BaseConfiguration(object):
    """This is the applications base configuration object.
    It will contain all of the DEFAULT constant values for
    our applications.  Every configuration object will inherit
    this.

    {{ params }}
    DEBUG = BOOL
    TESTING = BOOL
    HOST = STRING
    PORT = INTEGER"""
    DEBUG = False
    TESTING = False
    HOST = '0.0.0.0'
    PORT = 5000


class DevConfiguration(BaseConfiguration):
    """This configuration should be used and tailored to help
    limit the frustrations of debugging

    {{ params }}
    DEBUG = False"""
    DEBUG = True


class TestingConfiguration(BaseConfiguration):
    """This configuration should be used and tailored for testing
    the application.

    {{ params }}
    TESTING = True"""
    TESTING = True
