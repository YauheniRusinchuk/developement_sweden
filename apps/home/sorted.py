from apps.article.models import Article


def result_article(profile):
    ''' Function return subscriptions articles '''
    # articlesresult = Article.objects.filter(author=[x.user for x in profile.subscriptions.all()])
    # result = []
    authors = [a.user for a in profile.subscriptions.all()]
    authors.append(profile.user)
    articles = Article.objects.filter(author__in = authors)
    # articles = Article.objects.all()
    # for sub in profile.subscriptions.all():
    #     for art in articles:
    #         if sub.user == art.author:
    #             result.append(art)
    # result+= profile.user.article_set.all()
    return articles
