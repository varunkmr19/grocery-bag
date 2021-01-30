from datetime import datetime
from django.test import TestCase
from ..models import Item


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
