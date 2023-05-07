from database import Question
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker

def opendb():
    engine = create_engine("sqlite:///db.sqlite")
    Session = sessionmaker(bind=engine)
    return Session()

db = opendb()
q = Question(
    title='what is the formula of water',
    op1= 'h2h',
    op2 = 'h2n',
    op3 = 'h2s',
    op4 = 'h2o',
    ans = 'h2o',
    category ='gk'
)
db.add(q)
q = Question(
    title='what is the formula of oxygen',
    op1= 'h2h',
    op2 = 'h2n',
    op3 = 'o2',
    op4 = 'h2o',
    ans = 'o2',
    category ='gk'
)
db.add(q)



db.commit()
db.close()