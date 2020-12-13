from utils.app_exceptions import AppException

print([e for e in dir(AppException) if "__" not in e])
# ['FooCreateItem', 'FooGetItem', 'FooItemRequiresAuth']
