from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile

from copa.models import Comentario

class ComentarioListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 13 authors for pagination tests
        number_of_comment = 13

        for genre_id in range(number_of_comment):
            Comentario.objects.create(
                rut1='12345677',
                nombre='Camilo',
                descripcion='Prueba comentario',
            )
           
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('vistacomentario'))
        self.assertEqual(response.status_code, 200)
        
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('vistacomentario'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'copa/comentario_list.html')
        
    def test_pagination_is_ten(self):
        response = self.client.get(reverse('vistacomentario'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['comentario_list']) == 10)

    def test_lists_all_genres(self):
        # Get second page and confirm it has (exactly) remaining 3 items
        response = self.client.get(reverse('vistacomentario')+'?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['comentario_list']) == 3)
    