from django.core.management.base import BaseCommand
from ...models import Person
import csv


class Command(BaseCommand):
    help = ""

    def add_arguments(self, parser):
        parser.add_argument('--csv', nargs='?', type=str, required=True)

    def handle(self, *args, **options):
        csv_file = open(options["csv"], "r",
                        encoding="utf_8", errors="", newline="")
        f = csv.DictReader(csv_file, delimiter=",", doublequote=True,
                           quotechar='"', skipinitialspace=True)

        create_list = []
        for row in f:
            print(row["tel_number"])
            create_list.append(Person(
                name=row["name"],
                furigana=row["furigana"],
                tel_number=row["tel_number"],
                email=row["mail"],
                gender=row["gender"],
                blood_type=row["blood_type"],
                birthday=row["birthday"],
                belong=row["belong"]
            ))
        Person.objects.bulk_create(create_list)
