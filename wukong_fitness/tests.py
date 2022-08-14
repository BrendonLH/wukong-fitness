from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from wukong_fitness.models import Equipment


class EquipmentTests(TestCase):

    def setUp(self):
        self.equipment = Equipment.objects.create(name='mat', price=19.99)

    def test_equipment_name(self):
        self.assertEqual(f'{self.equipment.name}', 'mat')

    def test_equipment_not_name(self):
        self.assertIsNot(f'{self.equipment.name}', 'glove')

    def test_equipment_price(self):
        self.assertEqual(self.equipment.price, 19.99)

    def test_equipment_price_is_not(self):
        self.assertIsNot(self.equipment.price, 10.99)

class CoachesTests(TestCase):
    pass