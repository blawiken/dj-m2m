from django.contrib import admin
from django.forms import BaseInlineFormSet
from django.core.exceptions import ValidationError

from .models import Article, Scope


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        count_main_tag = 0
        
        for form in self.forms:
            if form.cleaned_data.get('is_main'):
                count_main_tag += 1
        
        if count_main_tag < 1:
            raise ValidationError('Select main tag')

        if count_main_tag > 1:
            raise ValidationError('Tag must be one')
        
        return super().clean()


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset
    extra = 1


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]
