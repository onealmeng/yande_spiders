# -*- coding: utf-8 -*-
from sqlalchemy import Column, String, Integer

from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()


# 定义UserNew对象:
class SP(Base):
    # 表的名字:
    __tablename__ = 'sp'

    # 表的结构:
    id = Column(Integer(), primary_key=True, nullable=False, autoincrement=True)
    fileName = Column(String(20))
    fineNameHash = Column(String(20))
    tags = Column(String(20))
    addTime = Column(String(20))


