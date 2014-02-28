from django.db import models
from django.core.urlresolvers import reverse
from imagekit.models import ProcessedImageField
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill
from pilkit.processors import ResizeToCover
from tinymce.models import HTMLField
from filebrowser.fields import FileBrowseField
from django.template.defaultfilters import slugify



class PostType(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True,max_length=255)
    def __unicode__(self):
        return u'%s' % self.name

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True,max_length=255)
    thumbnail = FileBrowseField("Image", max_length=200, directory="uploads/", extensions=[".jpg"], blank=True, null=True)
    description = models.CharField(max_length=255,null=True)
    content = HTMLField(null=True)
    published = models.BooleanField(default=True)
    # created = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField()
    external_link = models.URLField(null=True)
    external_data = models.TextField(null=True)
    external_image = models.CharField(max_length=255,null=True)
    post_type = models.ForeignKey(PostType)
    class Meta:
        ordering = ['-created']
    def __unicode__(self):
        return u'%s' % self.title
    def get_absolute_url(self):
        return reverse('blog.views.post',args=[self.slug])
    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)


class Image(models.Model):
    # image = models.ImageField(upload_to='images/')
    image = ProcessedImageField(upload_to='images/',
                                processors=[ResizeToCover(600,600)],
                               format='JPEG',
                               options={'quality':90})
    thumbnail = ImageSpecField(source='image',
                                      processors=[ResizeToFill(300, 300)],
                                      format='JPEG',
                                      options={'quality': 70})
    pub_date = models.DateTimeField((u'Publication Date'),auto_now=True)

    def __unicode__(self):
        return u'%s' % self.image.url

# image = Image.objects.all()[0]
# print image.thumbnail.url
# print image.thumbnail.width
