from sqlalchemy import Column, Integer, String, Text, DateTime
from models.database import Base
from datetime import datetime


class Video_items(Base):
    __tablename__ = 'video_items'
    id = Column(Integer, primary_key=True)
    video_id = Column(Text)
    item_image_1 = Column(Text)
    item_name_1 = Column(Text)
    item_url_1 = Column(Text)
    item_price_1 = Column(Text)
    item_image_2 = Column(Text)
    item_name_2 = Column(Text)
    item_url_2 = Column(Text)
    item_price_2 = Column(Text)
    item_image_3 = Column(Text)
    item_name_3 = Column(Text)
    item_url_3 = Column(Text)
    item_price_3 = Column(Text)
    item_image_4 = Column(Text)
    item_name_4 = Column(Text)
    item_url_4 = Column(Text)
    item_price_4 = Column(Text)
    item_image_5 = Column(Text)
    item_name_5 = Column(Text)
    item_url_5 = Column(Text)
    item_price_5 = Column(Text)

    def __init__(self, video_id=None, item_image_1=None, item_name_1=None, item_url_1=None, item_price_1=None,
                                    item_image_2=None, item_name_2=None, item_url_2=None, item_price_2=None,
                                    item_image_3=None, item_name_3=None, item_url_3=None, item_price_3=None,
                                    item_image_4=None, item_name_4=None, item_url_4=None, item_price_4=None,
                                    item_image_5=None, item_name_5=None, item_url_5=None, item_price_5=None):
        self.video_id = video_id
        self.item_image_1 = item_image_1
        self.item_name_1 = item_name_1
        self.item_url_1 = item_url_1
        self.item_price_1 = item_price_1
        self.item_image_2 = item_image_2
        self.item_name_2 = item_name_2
        self.item_url_2 = item_url_2
        self.item_price_2 = item_price_2
        self.item_image_3 = item_image_3
        self.item_name_3 = item_name_3
        self.item_url_3 = item_url_3
        self.item_price_3 = item_price_3
        self.item_image_4 = item_image_4
        self.item_name_4 = item_name_4
        self.item_url_4 = item_url_4
        self.item_price_4 = item_price_4
        self.item_image_5 = item_image_5
        self.item_name_5 = item_name_5
        self.item_url_5 = item_url_5
        self.item_price_5 = item_price_5
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
