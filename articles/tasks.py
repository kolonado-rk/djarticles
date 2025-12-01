import feedparser
from celery import shared_task
from .models import NewSource, Article


def fetch_articles_sync() -> int:
    """
    Synchronná verzia – vykoná načítanie hneď v tomto procese.
    Vráti počet nových uložených článkov.
    Túto funkciu vieš volať aj z management commandu pri --sync režime.
    """
    created_count = 0
    sources = NewSource.objects.all()

    for src in sources:
        print(f"Spracúvam zdroj: {src.name} ({src.rss_url})")

        feed = feedparser.parse(src.rss_url)

        for item in feed.entries:
            # zoberieme link, podľa neho budeme kontrolovať duplicitu
            link = getattr(item, "link", "")
            if not link:
                continue  # ak RSS položka nemá link, preskočíme

            # ak článok s daným zdrojom a linkom už existuje, preskočíme
            if Article.objects.filter(source=src, link=link).exists():
                continue

            title = getattr(item, "title", "")[:100]
            summary = getattr(item, "summary", "")  # začni jednoducho

            article = Article(
                source=src,
                title=title,
                link=link[:200],
                summary=summary,
                # published neriešime – máš auto_now_add=True
            )
            article.save()
            created_count += 1

            print(f"  + {article.title}")

    print(f"Hotovo, vytvorených {created_count} nových článkov.")
    return created_count


@shared_task
def fetch_articles_from_rss() -> int:
    """
    Celery task – spustí fetch_articles_sync v Celery workerovi.
    """
    return fetch_articles_sync()