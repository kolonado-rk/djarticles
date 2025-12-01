from django.core.management.base import BaseCommand
from articles.tasks import fetch_articles_from_rss, fetch_articles_sync


class Command(BaseCommand):
    help = "Načíta články z RSS feedov a uloží ich do Article (cez Celery alebo synchronne)."

    def add_arguments(self, parser):
        parser.add_argument(
            "--sync",
            action="store_true",
            help="Spustí načítanie synchronne (bez Celery, rovno v manage.py procese).",
        )

    def handle(self, *args, **options):
        if options["sync"]:
            # SYNCHRÓNNE – volá priamo Python funkciu (už žiadne Celery)
            self.stdout.write(self.style.WARNING("Spúšťam synchronne (bez Celery)..."))
            created = fetch_articles_sync()
            self.stdout.write(
                self.style.SUCCESS(
                    f"Hotovo, vytvorených {created} nových článkov (sync)."
                )
            )
        else:
            # ASYNCHRÓNNE – odošle task do Celery
            self.stdout.write("Odosielam Celery task na načítanie článkov...")
            result = fetch_articles_from_rss.delay()
            self.stdout.write(
                self.style.SUCCESS(
                    f"Celery task spustený. task_id = {result.id}"
                )
            )
