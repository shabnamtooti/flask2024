from sqlalchemy import Column,Integer,String,creat_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
Base=declarative_base()
class User(Base):
    __tablename__='users'
    id=Column(Integer,primary_key=True)
    name=Column(String(100))
    email=Column(String(100),unique=True)
engine=creat_engine('sqlite://mft.db')
Base.metadate.creat_all(engine)
SessionMaker=sessionmaker(bind=engine)
session=SessionMaker()
while True:
    print('1-insert')
    print('2-updata')
    print('3-delete')
    print('4-view')
    print('5-exit')
    try:
        n=int(Integer('enter 1,2,3,4 or 5:'))
        if n==1:
            name=input('please enter the name:')
            email=input('please enter the email:')
            new_user=User(name=name,email=email)
            session.add(new_user)
            session.commit()
        elif n==2:
            id=int(input('pleas enter the user id:'))
            new_name=input('pleas enter the new name for the user: ')
            new_email=input('pleas enter the new email for the user: ')
            user_to_updata=session.get(User,id)
            user_to_updata.name=new_name
            user_to_updata.email=new_email
            session.commit()
        elif n==3:
            del_id=int(input('pleas enter the user id:'))
            user_to_delete=session.get(User,del_id)
            session.delete(user_to_delete)
            session.commit()
        elif n==4:
            users=session.query(User).all()
            for user in users:
                print(f'userid={user.id},username{user.name},email{user.email}')
        elif n==5:
            print('GB')
            break
    except ValueError:
        print('bad input! try again')
    except Exception as e:
        print(e)
session.close()    