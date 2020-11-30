
from django.test import SimpleTestCase
from copa.forms import ComentarioForm

class TestForms(SimpleTestCase):

    def test_comentario_form_valid_data(self):
        form = ComentarioForm(data={
            'rut1': '12345678',
            'nombre': 'Benjamiin',
            'descripcion': 'Jugadores excelentes'
        })

        self.assertTrue(form.is_valid())



    def test_comentario_form_no_data(self):
        form = ComentarioForm(data={})


        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors),3)