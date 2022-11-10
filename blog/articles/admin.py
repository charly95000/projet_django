from django.contrib import admin

from articles.models import Article, Author


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','description','genre','author') #Liste des champs que nous voulons afficher

class AuthorAdmin(admin.ModelAdmin):
    list_display= ('firstname','lastname')

#admin.site.register(Article) #On enregistre le modele Article sur le site d'administration
admin.site.register(Article,ArticleAdmin)
admin.site.register(Author,AuthorAdmin)
