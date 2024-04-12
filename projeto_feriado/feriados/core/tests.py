from django.test import TestCase

class NatalTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/')

    def test_200_response(self):
        self.assertEqual(200, self.resp.status_code)

    def test_texto(self):
        self.assertContains(self.resp, 'natal')


class CarnavalTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/carnaval')
    
    def test_url_ok(self):
        self.assertEqual(self.resp.status_code, 200)


from .models import FeriadoModel
from datetime import datetime

class FeriadoModelTest(TestCase):
    def setUp(self):
        self.feriado = 'Natal'
        self.mes = 12
        self.dia = 25
        self.cadastro = FeriadoModel(
        nome=self.feriado,
        dia=self.dia,
        mes=self.mes)
        self.cadastro.save()  

    def test_created(self):
        self.assertTrue(FeriadoModel.objects.exists())

    def test_modificado_em(self):
        self.assertIsInstance(self.cadastro.modificado_em, datetime) 
    
    def test_nome_feriado(self):
        self.assertEqual(self.cadastro.nome, 'Natal')