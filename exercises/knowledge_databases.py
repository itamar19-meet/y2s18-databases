from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_article(article_name , topic , rating):
	article = Knowledge(
		article_name = article_name,
		topic = topic,
		rating = int(rating))
	print(repr(article))
	session.add(article)
	session.commit()


def query_all_articles():
	articles = session.query(Knowledge).all()
	return articles



def query_article_by_topic(ar_name):
	articles = session.query(Knowledge).filter_by(article_name=ar_name).first()
	return articles


def delete_article_by_topic():
	pass

def delete_all_articles():
	pass

def edit_article_rating():
	pass
name_of = input("what is the name of the article?")
topic_of = input(" what is the topic of the article?")
rating_of = int(input("what is the rating that you give to the artice"))
add_article(name_of,topic_of,rating_of)

print(query_all_articles())
print(query_article_by_topic("dd"))
