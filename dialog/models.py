import uuid

from django.db import models

# Create your models here.


class DialogMessage(models.Model):
    USER_MESSAGE = 1
    BOT_MESSAGE = 2

    TYPE_CHOICES = (
        (1, 'User Message'),
        (2, 'Bot Message')
    )

    uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    type = models.PositiveSmallIntegerField(choices=TYPE_CHOICES, null=False)
    message = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, editable=False, null=False)

    def __str__(self) -> str:
        return f'{DialogMessage.TYPE_CHOICES[self.type - 1][1]}: {self.message}'

    class Meta:
        ordering = ('created',)


class DialogChat(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    messages = models.ForeignKey(DialogMessage, on_delete=models.CASCADE)
