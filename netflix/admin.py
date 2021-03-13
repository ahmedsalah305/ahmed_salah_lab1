from django.contrib import admin
from .models import Movie , Category , Country , Rate
# Register your models here.

# class MovieInline(admin.TabularInline):
#     model   = Movie
#     extra   = 1
#     max_num = 10
class MovieInline(admin.StackedInline):
    model   = Movie
    extra   = 1
    max_num = 10

class CountryAdmin(admin.ModelAdmin):
    inlines = [MovieInline]

class MovieAdmin(admin.ModelAdmin):
    list_display = ("title" , "overView" , "year")
    list_filter  = ("year",)

admin.site.register(Movie    , MovieAdmin)
admin.site.register(Category)
admin.site.register(Country , CountryAdmin)
admin.site.register(Rate)