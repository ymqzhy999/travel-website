# coding:utf-8
import random
from datetime import datetime
from sqlalchemy import text,TIMESTAMP

from api.models.models import Base_model
from api.exts import db
from sqlalchemy.dialects.mysql import DOUBLE,LONGTEXT
# 个人信息
class yonghu(Base_model):
    __doc__ = u'''yonghu'''
    __tablename__ = 'yonghu'

    __loginUser__='yonghuzhanghao'


    __authTables__={}
    __authPeople__='是'
    __authSeparate__='否'
    __thumbsUp__='否'
    __intelRecom__='否'
    __browseClick__='否'
    __foreEndListAuth__='否'
    __foreEndList__='否'
    __isAdmin__='否'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    yonghuzhanghao=db.Column( db.VARCHAR(255), nullable=False,unique=True,comment='用户账号' )
    xingming=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='姓名' )
    mima=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='密码' )
    xingbie=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='性别' )
    shouji=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='手机' )
    touxiang=db.Column( db.Text,  nullable=True, unique=False,comment='头像' )


class jingdianxinxi(Base_model):
    __doc__ = u'''jingdianxinxi'''
    __tablename__ = 'jingdianxinxi'



    __authTables__={}
    __authPeople__='否'
    __authSeparate__='否'
    __thumbsUp__='否'
    __intelRecom__='是'
    __browseClick__='是'
    __foreEndListAuth__='否'
    __foreEndList__='是'
    __isAdmin__='否'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    jingdianmingcheng=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='景点名称' )
    jingdianleixing=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='景点类型' )
    jingdiandengji=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='景点等级' )
    tupian=db.Column( db.Text,  nullable=True, unique=False,comment='图片' )
    piaojia=db.Column( db.Float,default=0, nullable=False, unique=False,comment='票价' )
    piaoshu=db.Column( db.Integer,default=0, nullable=False, unique=False,comment='票数' )
    kaifangshijian=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='开放时间' )
    fuwudianhua=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='服务电话' )
    xiangxidizhi=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='详细地址' )
    jingdianxiangqing=db.Column( db.Text,  nullable=True, unique=False,comment='景点详情' )
    clicktime=db.Column( db.DateTime,  nullable=True, unique=False,comment='最近点击时间' )
    clicknum=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='点击次数' )


class jingdianleixing(Base_model):
    __doc__ = u'''jingdianleixing'''
    __tablename__ = 'jingdianleixing'



    __authTables__={}
    __authPeople__='否'
    __authSeparate__='否'
    __thumbsUp__='否'
    __intelRecom__='否'
    __browseClick__='否'
    __foreEndListAuth__='否'
    __foreEndList__='否'
    __isAdmin__='否'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    jingdianleixing=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='景点类型' )


class jingdianmenpiao(Base_model):
    __doc__ = u'''jingdianmenpiao'''
    __tablename__ = 'jingdianmenpiao'



    __authTables__={}
    __authPeople__='否'
    __authSeparate__='否'
    __thumbsUp__='否'
    __intelRecom__='是'
    __browseClick__='是'
    __foreEndListAuth__='否'
    __foreEndList__='否'
    __isAdmin__='否'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    laiyuan=db.Column( db.Text,  nullable=True, unique=False,comment='来源' )
    biaoti=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='标题' )
    fengmian=db.Column( db.Text,  nullable=True, unique=False,comment='封面' )
    miaoshu=db.Column( db.Text,  nullable=True, unique=False,comment='描述' )
    weizhi=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='位置' )
    dianping=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='点评' )
    pinglun=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='评论' )
    jiage=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='价格' )
    tese=db.Column( db.Text,  nullable=True, unique=False,comment='特色' )
    kaifangshijian=db.Column( db.Text,  nullable=True, unique=False,comment='开放时间' )
    clicktime=db.Column( db.DateTime,  nullable=True, unique=False,comment='最近点击时间' )
    clicknum=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='点击次数' )


class storeup(Base_model):
    __doc__ = u'''storeup'''
    __tablename__ = 'storeup'



    __authTables__={}
    __authSeparate__='是'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    userid=db.Column( db.BigInteger, nullable=False, unique=False,comment='用户id' )
    refid=db.Column( db.BigInteger,  nullable=True, unique=False,comment='商品id' )
    tablename=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='表名' )
    name=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='名称' )
    picture=db.Column( db.Text, nullable=False, unique=False,comment='图片' )
    type=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='类型(1:收藏,21:赞,22:踩,31:竞拍参与,41:关注)' )
    inteltype=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='推荐类型' )
    remark=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='备注' )


class news(Base_model):
    __doc__ = u'''news'''
    __tablename__ = 'news'



    __authTables__={}
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    title=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='标题' )
    introduction=db.Column( db.Text,  nullable=True, unique=False,comment='简介' )
    picture=db.Column( db.Text, nullable=False, unique=False,comment='图片' )
    content=db.Column( db.Text, nullable=False, unique=False,comment='内容' )


class messages(Base_model):
    __doc__ = u'''messages'''
    __tablename__ = 'messages'



    __authTables__={}
    __hasMessage__='是'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    userid=db.Column( db.BigInteger, nullable=False, unique=False,comment='留言人id' )
    username=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='用户名' )
    avatarurl=db.Column( db.Text,  nullable=True, unique=False,comment='头像' )
    content=db.Column( db.Text, nullable=False, unique=False,comment='留言内容' )
    cpicture=db.Column( db.Text,  nullable=True, unique=False,comment='留言图片' )
    reply=db.Column( db.Text,  nullable=True, unique=False,comment='回复内容' )
    rpicture=db.Column( db.Text,  nullable=True, unique=False,comment='回复图片' )


class discussjingdianxinxi(Base_model):
    __doc__ = u'''discussjingdianxinxi'''
    __tablename__ = 'discussjingdianxinxi'



    __authTables__={}
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    refid=db.Column( db.BigInteger, nullable=False, unique=False,comment='关联表id' )
    userid=db.Column( db.BigInteger, nullable=False, unique=False,comment='用户id' )
    avatarurl=db.Column( db.Text,  nullable=True, unique=False,comment='头像' )
    nickname=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='用户名' )
    content=db.Column( db.Text, nullable=False, unique=False,comment='评论内容' )
    reply=db.Column( db.Text,  nullable=True, unique=False,comment='回复内容' )


class discussjingdianmenpiao(Base_model):
    __doc__ = u'''discussjingdianmenpiao'''
    __tablename__ = 'discussjingdianmenpiao'



    __authTables__={}
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    refid=db.Column( db.BigInteger, nullable=False, unique=False,comment='关联表id' )
    userid=db.Column( db.BigInteger, nullable=False, unique=False,comment='用户id' )
    avatarurl=db.Column( db.Text,  nullable=True, unique=False,comment='头像' )
    nickname=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='用户名' )
    content=db.Column( db.Text, nullable=False, unique=False,comment='评论内容' )
    reply=db.Column( db.Text,  nullable=True, unique=False,comment='回复内容' )


