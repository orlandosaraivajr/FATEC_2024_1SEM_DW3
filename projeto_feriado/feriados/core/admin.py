from django.contrib import admin
from core.models import FeriadoModel
from datetime import datetime

class FeriadoModelAdmin(admin.ModelAdmin):
    list_display = ('nome','dia','mes','modificado_em','registrado_esse_ano','registrado_hoje')
    date_hierarchy = 'modificado_em'
    search_fields = ('nome','dia','mes')
    list_filter = ('modificado_em',)
    

    def registrado_esse_ano(self, obj):
        hoje = datetime.today()
        return obj.modificado_em.year == hoje.year
  
    def registrado_hoje(self, obj):
        hoje = datetime.today()
        return obj.modificado_em.day == hoje.day and obj.modificado_em.month == hoje.month
  
    registrado_esse_ano.boolean = True
    registrado_hoje.boolean = True
    
admin.site.register(FeriadoModel, FeriadoModelAdmin)
