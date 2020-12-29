import json

import tornado.ioloop
import tornado.web
import tornado
from tornado import gen
import pymysql


client = pymysql.connect("huameidb.mysql.database.chinacloudapi.cn", "webuser@huameidb", "User@123", "hm_test")

class MainHandler(tornado.web.RequestHandler):
    @gen.coroutine
    def get(self):
        user_name = self.get_query_argument("user_name")
        pwd = self.get_query_argument("pwd")
        args = (user_name,pwd)
        global client
        cursor = client.cursor()
        try:
            cursor.execute("select user_id,real_name from identif where user_id=%s and real_name=%s'", args)
            res = cursor.fetchone()
        except Exception:
            return self.finish("wrong")
        if res:
            return self.finish(json.dumps({"user": res}))
        else:
            return self.finish("wrong")

def make_app():
    return tornado.web.Application([
        (r"/api/login", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(5000)
    tornado.ioloop.IOLoop.current().start()