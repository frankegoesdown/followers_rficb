# -*- coding: utf-8 -*-
# django
import django.core.exceptions
from django.test import TestCase
from django.core import management
# local
from followers.models import Users, Follow

class TestManFollow(TestCase):
    def setUp(self):
        Users(name="Stepan Ivanov").save()
        Users(name="Modest Musorgsky").save()
        Follow(user=Users.objects.get(name="Stepan Ivanov"), follow_user=Users.objects.get(name="Modest Musorgsky")).save()

    def test_remove(self):
        Users.objects.get(name="Modest Musorgsky").delete()
        ivanov_follows = Follow.objects.filter(user=Users.objects.get(name="Stepan Ivanov"))
        self.assertEqual(len(ivanov_follows), 0)

    def test_follow_non_existent(self):
        katya = Users(name="Katya Ryabchikova")
        katya.save()
        try:
            Follow(user=katya, follow_user=Users.objects.get(name="non-existent")).save()
        except Exception as e:
            self.assertEquals(True, isinstance(e, django.core.exceptions.ObjectDoesNotExist))

    def test_duplicated_follow(self):
        Follow(user=Users.objects.get(name="Stepan Ivanov"), follow_user=Users.objects.get(name="Modest Musorgsky")).save()
        self.assertEqual(len(Follow.objects.filter(user=Users.objects.get(name="Stepan Ivanov"), follow_user=Users.objects.get(name="Modest Musorgsky"))), 2)
