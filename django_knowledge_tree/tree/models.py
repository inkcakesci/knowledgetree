from django.db import models

class KnowledgeTree(models.Model):
    # data 字段存储知识树结构，格式例如：
    # {
    #   "学科": {
    #       "人教版高中英语必修第一册": {
    #           "章节1": ["知识点1", "知识点2"],
    #           "章节2": ["知识点A", "知识点B"]
    #       },
    #       "其他课本": { ... }
    #   }
    # }
    data = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"KnowledgeTree {self.pk}"
