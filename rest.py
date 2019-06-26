from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop
import json
import psycopg2

emails = '1702363@s2.com'
pwd = 'pw'

def make_app():
  urls = ([
    ("/", login),
    ("/api/item/", login)
  ])
  return Application(urls, debug=True)
  
def android():
    try:
        connection = psycopg2.connect(user = "postgres",
                                      password = "postgres",
                                      host = "172.17.0.3",
                                      port = "5432",
                                      database = "postgres")
        cursor = connection.cursor()
        # Print PostgreSQL Connection properties
        print ( connection.get_dsn_parameters(),"\n")
        # Print PostgreSQL version
        cursor.execute("SELECT version();")
        record = cursor.fetchone()
        print("You are connected to - ", record,"\n")
    except (Exception, psycopg2.Error) as error :
        print ("Error while connecting to PostgreSQL", error)
    finally:
        #closing database connection.
            if(connection):
                sqlStr = "SELECT email, pwd FROM login where email='%s'" % (emails)
                print(sqlStr)
                cursor.execute(sqlStr)
                result = cursor.fetchone()
                email,pw = result
                if pw == pwd:
                    print('Password Correct')
                    print('errorcode:0')
                    print('Auth Ok!')
                else:
                    print('Incorrect Email and Password')
                    print('errorcode:1')
                print(result)
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")

class login(RequestHandler):
  def get(self):
    self.write({'email': emails})
    self.write({'password': pwd})
    android()

  def post(self):
    emails.append(json.loads(self.request.body))
    pwd.append(json.loads(self.request.body))
    self.write({'login': json.loads(self.request.body)})


if __name__ == '__main__':
  app = make_app()
  app.listen(8888)
  IOLoop.instance().start()


