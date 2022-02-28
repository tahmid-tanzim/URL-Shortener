from django.db import models


class TinyURL(models.Model):
    millisecond = models.PositiveBigIntegerField()
    short_code = models.CharField(max_length=7)
    main_url = models.URLField(max_length=255)

    class Meta:
        db_table = "tiny_url"
