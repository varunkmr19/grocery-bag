from datetime import datetime
from django.test import TestCase
from ..models import Item, User


class UserTest(TestCase):
    ''' Test module for User model '''

    def setUp(self):
        User.objects.create(
            username='test_user1',
            email='test_user1@test.com',
            password='test_pass'
        )
        User.objects.create(
            username='test_user2',
            email='test_user2@test.com',
            password='test_pass'
        )

    def test_username(self):
        USER1_USERNAME = 'test_user1'
        USER2_USERNAME = 'test_user2'
        user1 = User.objects.get(username=USER1_USERNAME)
        user2 = User.objects.get(username=USER2_USERNAME)
        self.assertEqual(user1.username, USER1_USERNAME)
        self.assertEqual(user2.username, USER2_USERNAME)


class ItemTest(TestCase):
    ''' Test module for Item model '''

    def setUp(self):
        Item.objects.create(
            name='Chicken',
            quantity='1kg',
            status='BOUGHT',
            date=datetime.now().date()
        )
        Item.objects.create(
            name='Milk',
            quantity='1 ltr',
            status='PENDING',
            date=datetime.now().date()
        )

    def test_item_name(self):
        chicken = Item.objects.get(name='Chicken')
        milk = Item.objects.get(name='Milk')
        self.assertEqual(chicken.__str__(), 'Chicken')
        self.assertEqual(milk.__str__(), 'Milk')
