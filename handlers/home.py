from tornado.websocket import WebSocketHandler
from handlers.base import BaseHandler
from models import User, session


class HomeHandler(BaseHandler):
    def get(self):
        self.render('home/index.html')


class AuthHandler(BaseHandler):
    def get(self):
        self.render('auth.html')

    def post(self):
        this_username = self.get_body_argument('username', '')

        try:
            assert session.query(User).filter_by(username=this_username).first() != None
        except Exception as e:
            user = User(username=this_username)
            session.add(user)
            self.write(f'Username <b>{this_username}</b> added to database')
        else:
           # print(result)
           self.write(f'Username <b>{this_username}</b> already exist')
        finally:
            session.commit()

