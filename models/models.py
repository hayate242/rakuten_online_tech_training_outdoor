from sqlalchemy import Column, Integer, String, Text, DateTime
from models.database import Base
from datetime import datetime


class Video_items(Base):
    __tablename__ = 'video_items'
    id = Column(Integer, primary_key=True)
    video_id = Column(Integer)
    item_id = Column(Integer)
    item_title = Column(Text)
    item_url = Column(Text)

    def __init__(self, video_id=None, item_id=None, item_title=None, item_url=None):
        self.item_id = item_id
        self.item_title = item_title
        self.item_url = item_url
    # def __repr__(self):
    #    return '<Title %r>' % (self.title)


class Videos(Base):
    __tablename__ = 'videos'
    video_id = Column(Integer, primary_key=True)
    video_title = Column(Text)
    uploaded_at = Column(Text)
    explain_text = Column(Text)
    serch_tag = Column(Text)
    Youtube_link = Column(Text)
    Type = Column(Text)

    def __init__(self, video_title=None, uploaded_at=None, explain_text=None, serch_tag=None, Youtube_link=None, Type=None):
        self.video_title = video_title
        self.uploaded_at = uploaded_at
        self.explain_text = explain_text
        self.serch_tag = serch_tag
        self.Youtube_link = Youtube_link
        self.Type = Type


class Categories(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    category_api_name = Column(Text)
    category_display_name = Column(Text)

    def __init__(self,  category_api_name=None, category_display_name=None):
        self.category_api_name = category_api_name
        self.category_display_name = category_display_name


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    user_name = Column(Text)
    email = Column(Text)
    password = Column(Text)

    def __init__(self, user_name=None, email=None, password=None):
        self.user_name = user_name
        self.email = email
        self.password = password
