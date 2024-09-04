import pytest

from src.article import Article


@pytest.fixture
def one_article():
    Article.articles = dict()
    return Article.insert('test', 'test')


@pytest.fixture
def two_articles():
    Article.articles = dict()
    Article.insert('test1', 'test1')
    return Article.insert('test2', 'test2')


def test_insert(one_article):
    """ Тест для проверки, что количество статей равно единице """
    assert len(Article.articles) == 1


def test_article_id(one_article):
    """ Тест на проверку установки ID статьи """
    assert one_article.article_id == 1


def test_increase_id(two_articles):
    """ Тест на проверку увеличения ID статьи """
    assert two_articles.article_id == 2


def test_increase_article_count(two_articles):
    assert len(Article.articles) == 2
