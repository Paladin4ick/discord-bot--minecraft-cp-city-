class Extensions:
    __list__ = [
        {'package': 'database_operation', 'name': 'add_all_users_db'},
        {'package': 'database_operation', 'name': 'set_ava'},
    ]

    @staticmethod
    def all():
        return Extensions.__list__
    
    @staticmethod
    def get(name):
        for extension in Extensions.__list__:
            if extension['name'] == name:
                return extension
            else:
                return None
    

    def __repr__(self):
        return self.__list__.__repr__()