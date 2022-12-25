from JobPost.models import Post
from django.contrib.auth.models import User
# drop existing models
Post.objects.all().delete()
User.objects.all().delete()
# insert the predefined entries
from Login import insertUsers
from JobPost import insertList
