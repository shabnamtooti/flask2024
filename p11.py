class singleton:
    _instance=None
    def __new__(cls):
        if cls._instance is None:
            cls._instance=super(singleton,cls).__new__(cls)
s1=singleton()
s2=singleton()
print(s1 is s2)