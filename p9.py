class myclass:
    def __new__(cls):
        print('creating the object')
        return super(myclass,cls).__new__(cls)
    def __init__(self):
        print('initializing the object')
    def __enter__(self):
        print('entering the context')
        return self
    def __exit__(self,*args,**kwargs):
        print('exiting the context')
with myclass()as obj:
    print('inside the context')