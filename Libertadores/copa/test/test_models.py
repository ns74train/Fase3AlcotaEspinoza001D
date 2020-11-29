from django.test import TestCase
from copa.models import Usuario

class UsuarioTestCase(TestCase):
    def setUp(self):
        Usuario.objects.create(first_name="Francisco",last_name="Rodriguez")


    def test_usuario(self):
        usuario1 = Usuario.objects.get(first_name="Francisco")
        self.assertEqual(usuario1.first_name, "Francisco")  


        
