from django.contrib import admin
from blog.models import Post,Image,PostType


class PostAdmin(admin.ModelAdmin):
    list_display = ['title','description']
    list_filter = ['published','created']
    search_fields = ['title','description','content']
    date_hierarchy = 'created'
    save_on_top = True;
    prepopulated_fields = {"slug":("title",)}

class PostTypeAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("name",)}

class ImageAdmin(admin.ModelAdmin):
    fields = ['image']



admin.site.register(Post,PostAdmin)
admin.site.register(PostType,PostTypeAdmin)
admin.site.register(Image,ImageAdmin)
