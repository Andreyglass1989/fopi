from fopi.tele_bot.models import Client


class DatabaseRouter(object):
    def db_for_read(self, model, **hints):
        if issubclass(model, Client):
            return 'default'

        return 'local'

    def db_for_write(self, model, **hints):
        if issubclass(model, Client):
            return None

        return 'local'

    def allow_relation(self, obj1, obj2, **hints):
        return (isinstance(obj1, Client) == isinstance(obj2, Client))

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'default':
            return False
        return (db == 'local')