from django.db import models


class Hack(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default="n/a")
    author = models.CharField(max_length=100, default="???")
    status = models.CharField(max_length=100)
    file = models.CharField(max_length=100)
    process = models.CharField(max_length=100, default="csgo.exe")
    source = models.CharField(max_length=300, default="n/a")
    game = models.CharField(max_length=100, default="CSGO")

    # flags
    steam_module = models.BooleanField(
        default=False, help_text="Is this hack using the steam module?"
    )
    # ======
    working = models.BooleanField(default=True)

    def __str__(self):
        return self.name
