from django.contrib import admin

from .models import Post, Categories


class CustomPostAdmin(admin.ModelAdmin):
    list_display = ['title','author','status']
    prepopulated_fields = {'slug':('title',)}

class CustomCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    
admin.site.register(Post, CustomPostAdmin)
admin.site.register(Categories, CustomCategoryAdmin)
