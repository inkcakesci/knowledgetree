from django.db import models

class KnowledgeTree(models.Model):
    title = models.CharField(max_length=255, default="Untitled Knowledge Tree")
    data = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
