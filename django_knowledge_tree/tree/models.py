from django.db import models

class KnowledgeTree(models.Model):
    title = models.CharField(
        max_length=255, 
        default="Untitled Knowledge Tree",
        help_text="知识点树的名称"
    )
    data = models.JSONField(
        default=dict, 
        blank=True,
        help_text="存储知识点的 JSON 数据，PostgreSQL 中会被存为 jsonb 类型"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name = "知识点树"
        verbose_name_plural = "知识点树"
        # 如果需要在 title 字段上添加索引可以使用 indexes 属性：
        # indexes = [
        #     models.Index(fields=['title'], name='idx_knowledge_title'),
        # ]
