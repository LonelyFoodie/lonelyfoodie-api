from werkzeug.exceptions import NotFound
from lonelyfoodie.database import use_database
from lonelyfoodie.database.models import User

@use_database
def check_log(db,id,password):
    user = db.query(User).filter(User.username == id).one()
    if not user:
        raise NotFound()
    elif user.password != password:
        return False
    else:
        return True


        

    
