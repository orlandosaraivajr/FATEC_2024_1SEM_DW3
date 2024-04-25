from django.test import TestCase
from .models import FeriadoModel
from datetime import datetime

class FeriadoVazioTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/')

    def test_200_response(self):
        self.assertEqual(200, self.resp.status_code)

    def test_texto(self):
        self.assertContains(self.resp, 'Não tem feriado hoje')

    def test_templateUsed(self):
        self.assertTemplateUsed(self.resp, 'feriado.html')

class FeriadoDiaArquivoMortoTest(TestCase):
    def setUp(self):
        hoje = datetime.today()
        self.cadastro = FeriadoModel(
            nome="Dia do Arquivo Morto",
            dia=hoje.day,
            mes=hoje.month)
        self.cadastro.save()  
        self.resp = self.client.get('/')

    def test_200_response(self):
        self.assertEqual(200, self.resp.status_code)

    def test_texto(self):
        self.assertContains(self.resp, 'Dia do Arquivo Morto')

    def test_templateUsed(self):
        self.assertTemplateUsed(self.resp, 'feriado.html')




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

from core.forms import FeriadoForm

class FeriadoFormTest(TestCase):
    def test_form_has_fields(self):
        form = FeriadoForm()
        expected = ['nome', 'dia', 'mes']
        self.assertSequenceEqual(expected, list(form.fields))