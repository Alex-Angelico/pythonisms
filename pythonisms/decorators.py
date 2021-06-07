from functools import wraps

def entry_counter(function):
    @wraps(function)
    def added_info(*args, **kwargs):
        base = function(*args, **kwargs)
        number = base.count('\n')
        return f'{base}\n=========================\n{number} line entries\n=========================\n'
    return added_info