class singletonmeta(type):
    _instance={}
    def __call__(cls,*args,**kwargs):
        if cls not in cls._instance:
            cls._instance[cls]=super(singletonmeta,cls).__call__(*args,**kwargs)
            return cls._instance[cls]
class singleton(metaclass=singletonmeta):
    pass
s1=singleton()
s2=singleton()
print(s1 is s2)