from django import forms
from . import models, lalafo_kg

class ParserProductForm(forms.Form):
    MEDIA_CHOISCES = (
        ('Lalafo.kg', 'Lalafo.kg'),
    )
    media_type = forms.ChoiceField(choices=MEDIA_CHOISCES)

    class Meta:
        filds = [
            'media_type',
        ]
    def parser_data(self):
        if self.data['media_type'] == 'lalafo.kg':
            lalafo_parser = lalafo_kg.parser()
            for i in kivano_parser:
                models.KivanoProducts.objects.create(**i)