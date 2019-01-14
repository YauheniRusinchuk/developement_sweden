from apps.article.models import Article


def result_article(profile):
    ''' Function return subscriptions articles '''
    authors = [a.user for a in profile.subscriptions.all()]
    authors.append(profile.user)
    articles = Article.objects.filter(author__in = authors)
    return articles
