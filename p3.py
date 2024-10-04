class myclass:
    def __enter__(self):
        print('enter class manager')
    def __exit__(self,exc_type,exc_val,exc_traceback):
        print(exc_type,exc_val,exc_traceback)
        print('ending class manager')
        return True
def f1():
    print('hello dad')
with myclass()as f:
    f1qwe()