import os

os.environ["DJANGO_SETTINGS_MODULE"] = "config.settings"

import django

django.setup()

from django.core.management import call_command


def save_fixtures(app_name):
    fixture_dir = "fixtures"
    fixture_filename = f"{app_name}_fixtures.json"

    if not os.path.exists(fixture_dir):
        os.makedirs(fixture_dir)

    with open(os.path.join(fixture_dir, fixture_filename), "w", encoding="utf-8") as f:
        call_command("dumpdata", app_name, stdout=f)


save_fixtures("article")
save_fixtures("main")
save_fixtures("servises")
save_fixtures("users")

