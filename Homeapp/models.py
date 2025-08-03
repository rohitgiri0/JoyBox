from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ConsoleListing(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    console_name=models.CharField(max_length=60)
    description=models.TextField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    location=models.CharField(max_length=100)
    available=models.BooleanField(default=True)
    photo1=models.ImageField(upload_to='console_photos/',null=False,blank=False)
    photo2=models.ImageField(upload_to='console_photos/',null=False,blank=False)
    posted_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}-{self.console_name}"


class ChatRoom(models.Model):
    user1 = models.ForeignKey(User, related_name='chatrooms_as_user1', on_delete=models.CASCADE)
    user2 = models.ForeignKey(User, related_name='chatrooms_as_user2', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user1', 'user2'], name='unique_chat_between_users')
        ]

    def __str__(self):
        return f"Chat between {self.user1.username} & {self.user2.username}"

    def get_opponent(self, user):
        return self.user2 if self.user1 == user else self.user1

class Message(models.Model):
    chat_room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['timestamp']

    def __str__(self):
        return f"{self.sender.username}: {self.content[:30]}"
