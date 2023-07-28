from django.contrib.auth.models import User


class HookSet(object):

    def get_blog(self, **kwargs):
        username = kwargs.get("username", None)
        return User.objects.get(username=username).blog