import datetime
import pymysql

class db_util:
    def __init__(self, host='localhost', port=3306, user='root', psw='', db='tesla_giga_ga_pt000', charset='utf8'):
        self.host = host
        self.port = port
        self.user = user
        self.psw = psw
        self.db = db
        self.charset = charset

    def connect(self):
        self.conn = pymysql.Connect(host=self.host, port=self.port, user=self.user, passwd=self.psw, db=self.db,
                                    charset=self.charset)
        self.cur = self.conn.cursor()

    def close(self):
        self.cur.close()
        self.conn.close()

    def select_by_predict_result_null(self):
        self.connect()
        sql = "select `id`,`path` from `image` where `predict_result` is null"
        self.cur.execute(sql)
        self.data = self.cur.fetchall()
        self.close()
        return self.data
    
    def update_predict_result(self,id,update_value):
        self.connect()
        sql="update `image` set `predict_result`=%s,`updateat`=%s where `id`=%s"
        self.cur.execute(sql,(update_value,datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),id))
        self.conn.commit()
        self.close()
        return
    
    def delete(self):
        pass

    def insert(self,name,path):
        self.connect()
        dt=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sql="insert into `image`(`name`,`path`,`isactive`,`created`,`updateat`) values(%s,%s,1,%s,%s)"
        self.cur.execute(sql,(name,path,dt,dt))
        self.conn.commit()
        self.close()
        return