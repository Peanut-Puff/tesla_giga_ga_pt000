import pymysql
import config

class db_util:
    def __init__(self):
        self.cfg=config.DATABASE_CONFIG

    def connect(self):
        self.conn = pymysql.Connect(**self.cfg)
        self.cur = self.conn.cursor()

    def close(self):
        self.cur.close()
        self.conn.close()
    
    def select_by_predict_result_null(self,limit,max=0):
        self.connect()
        sql = "select `id`,`path` from `image` where `predict_result` is null and `id` > %s LIMIT %s"
        self.cur.execute(sql,(max,limit))
        self.data = self.cur.fetchall()
        self.close()
        return self.data
    
    def update_key_valaue(self,id,update_key,update_value):
        self.connect()
        sql="update `image` set `"+update_key+"`=%s,`updateat`=NOW() where `id`=%s"
        self.cur.execute(sql,(update_value,id))
        self.conn.commit()
        self.close()
        return
    
    def delete(self):
        pass

    def insert(self,name,path):
        self.connect()
        sql="insert into `image`(`name`,`path`) values(%s,%s)"
        self.cur.execute(sql,(name,path))
        self.conn.commit()
        self.close()
        return