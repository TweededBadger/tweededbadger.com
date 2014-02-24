from django.contrib import admin
from blog.models import Post,Image


class PostAdmin(admin.ModelAdmin):
    list_display = ['title','description']
    list_filter = ['published','created']
    search_fields = ['title','description','content']
    date_hierarchy = 'created'
    save_on_top = True;
    prepopulated_fields = {"slug":("title",)}

class ImageAdmin(admin.ModelAdmin):
    fields = ['image']
    fields = ['image']



admin.site.register(Post,PostAdmin)
admin.site.register(Image,ImageAdmin)
