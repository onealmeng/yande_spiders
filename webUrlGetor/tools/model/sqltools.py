# -*- coding: utf-8 -*-
import hashlib
import os
import time
from webUrlGetor.settings import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from webUrlGetor.tools.model.sp import *


class SQLTools(object):

    def __init__(self):
        self.sqlite_file_path = os.path.join(DB_path, 'test.db')

    def stringtomd5(self, originstr):
        signaturemd5 = hashlib.md5()
        signaturemd5.update(originstr.encode('utf-8'))
        return signaturemd5.hexdigest()

    def insert_into_new_db(self, fileName, tags_name=None):
        """
        增 向数据库插入用户数据
        :return:
        """
        # 初始化数据库连接:
        engine = create_engine('sqlite:///' + str(self.sqlite_file_path))
        current_date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        # 创建DBSession类型:
        DBSession = sessionmaker(bind=engine)
        # 创建session对象:
        session = DBSession()
        fineNameHash = self.stringtomd5(fileName)
        try:
            if tags_name is not None:
                new_user = SP(fileName=fileName, fineNameHash=fineNameHash, tags=tags_name, addTime=current_date)
            else:
                new_user = SP(fileName=fileName, fineNameHash=fineNameHash, addTime=current_date)
            session.add(new_user)
            session.commit()
        except Exception as e:
            print("db error", e)
            session.rollback()
        finally:
            session.close()

    def query_from_UserNew_more_info(self, fileName):
        """
        查
        :return:
        """
        # 初始化数据库连接:
        engine = create_engine('sqlite:///' + str(self.sqlite_file_path))

        # 创建DBSession类型:
        DBSession = sessionmaker(bind=engine)
        # 创建session对象:
        session = DBSession()
        fineNameHash = self.stringtomd5(fileName)
        try:
            has_got = session.query(SP).filter(SP.fineNameHash == fineNameHash).all()
            return has_got
        except Exception as e:
            print("db error", e)
        finally:
            session.close()

    def query_from_UserNew_more_info_by_tag(self, tag):
        """
        查
        :return:
        """
        # 初始化数据库连接:
        engine = create_engine('sqlite:///' + str(self.sqlite_file_path))

        # 创建DBSession类型:
        DBSession = sessionmaker(bind=engine)
        # 创建session对象:
        session = DBSession()
        try:
            has_got = session.query(SP).filter(SP.tags == tag).all()
            return has_got
        except Exception as e:
            print("db error", e)
        finally:
            session.close()


if __name__ == '__main__':
    x = SQLTools()
    a=x.stringtomd5("68682a2817c805c1ed50b13484c8ff38.png")
    print(a)
