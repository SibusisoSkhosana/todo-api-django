from django.db import models
from django.core.exceptions import ValidationError

class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        # title and description need to be present
        if self.description and len(self.description) > 500:
            raise ValidationError({
                "description": "Description cannot exceed 500 characters."
            })

   # here we run clean before saving, ensures our validation is applied to both create and update operations     
    def save(self, *args, **kwargs):
        self.full_clean()  
        super().save(*args, **kwargs)        

    def __str__(self):
        return self.title
