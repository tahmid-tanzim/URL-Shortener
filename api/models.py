from django.db import models


class TinyURL(models.Model):
    millisecond = models.PositiveBigIntegerField()
    short_code = models.CharField(max_length=7)
    main_url = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "tiny_url"
