from django.core.management.base import BaseCommand
import feedparser

from articles.models import NewSource, Article


class Command(BaseCommand):
    help = "Načíta články z RSS feedov a uloží ich do Article"

    def handle(self, *args, **options):
        sources = NewSource.objects.all()

        for src in sources:
            self.stdout.write(f"Spracúvam zdroj: {src.name} ({src.rss_url})")

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

                self.stdout.write(f"  + {article.title}")