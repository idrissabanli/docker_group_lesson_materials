import math
from django.db import models
from django.contrib.auth import get_user_model
from stories.tools.slug_generator import slugify
from datetime import datetime
from ckeditor.fields import RichTextField
from django.urls import reverse_lazy

USER_MODEL = get_user_model()


class Category(models.Model):
    """
    Bu model reseptlerin ve storilerin kategoriyalarini saxlamaq ucundu.
    Misal: Deset, Yemek
    """

    #informations
    title = models.CharField('Title', max_length=120)
    image = models.ImageField('Image', upload_to='category_images')

    # moderations
    is_published = models.BooleanField('is published', default=True)
    order = models.PositiveIntegerField('Order', default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ('order',)
    
    def __str__(self):
        return self.title


class Tag(models.Model):

    #information
    title = models.CharField('Title', max_length=40)

    # moderations
    is_published = models.BooleanField('is published', default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tag'
    
    def __str__(self):
        return self.title


class Recipe(models.Model):
    # relations
    category = models.ForeignKey(Category, verbose_name='Kateqoriya', on_delete=models.CASCADE, db_index=True, related_name='recipes')
    tags = models.ManyToManyField(Tag, verbose_name='Tags', related_name='recipes')
    author = models.ForeignKey(USER_MODEL, on_delete=models.CASCADE, db_index=True, related_name='recipes')

    # informations
    title = models.CharField('Basligi', max_length=120)
    short_description = models.CharField('Qisa Mezmunu', max_length=255, help_text='Bu sahe repestler siyahisinda reseptin mezmunu olaraq gorunur...')
    image = models.ImageField('Sekil', upload_to='recipes')
    long_description = RichTextField('Genis mezmunu')
    show_home_page = models.BooleanField(default=False)
    # author = models.CharField('Muellif', max_length=50)

    # moderations
    min_read_time = models.PositiveIntegerField('Min read time', editable=False, default=1)
    slug = models.SlugField('slug', max_length=255, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField('is published', default=True)

    class Meta: # table name: stroies_recipe
        # app_label = 'story'
        # db_table = 'resept'
        verbose_name = 'Resept'
        verbose_name_plural = 'Reseptler'
        ordering = ('-created_at', '-title')

    def __str__(self):
        return f"{self.title} category: {self.category}"

    def save(self, *args, **kwargs):
        article_word_count = len(self.long_description.split(' '))
        self.min_read_time = math.ceil(article_word_count/120)
        if not self.slug:
            self.slug = f"{slugify(self.title)}-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse_lazy('recipe_detail', kwargs={'slug': self.slug }) #f'/stories/{self.slug}/'


class Story(models.Model):
    # relations
    category = models.ForeignKey(Category, verbose_name='Kateqoriya', on_delete=models.CASCADE, db_index=True, related_name='stories')
    tags = models.ManyToManyField(Tag, verbose_name='Tags', related_name='stories')
    author = models.ForeignKey(USER_MODEL, on_delete=models.CASCADE, db_index=True, related_name='stories')

    # informations
    title = models.CharField('Basligi', max_length=120)
    image = models.ImageField('Sekil', upload_to='recipes')
    long_description = RichTextField('Genis mezmunu')
    # author = models.CharField('Muellif', max_length=50)

    # moderations
    slug = models.SlugField('slug', max_length=255, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    min_read_time = models.PositiveIntegerField('Min read time', editable=False, default=1)
    is_published = models.BooleanField('is published', default=True)

    class Meta: # table name: stroies_recipe
        # app_label = 'story'
        # db_table = 'resept'
        verbose_name = 'Hekaye'
        verbose_name_plural = 'Hekayeler'
        ordering = ('-created_at', '-title')

    def __str__(self):
        return f"{self.title} category: {self.category}"

    def save(self, *args, **kwargs):
        article_word_count = len(self.long_description.split(' '))
        self.min_read_time = math.ceil(article_word_count/120)
        if not self.slug:
            self.slug = f"{slugify(self.title)}-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse_lazy('story_detail', kwargs={'slug': self.slug }) #f'/stories/{self.slug}/'


class Comment(models.Model):
    # relations
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='comments')
    # story to do add story model and relation here
    user = models.ForeignKey(USER_MODEL, related_name='comments', on_delete=models.CASCADE, null=True, blank=True)
    parent_comment = models.ForeignKey('self', related_name='child_comments', on_delete=models.CASCADE, null=True, blank=True)

    user_name = models.CharField('Name', max_length=50, null=True, blank=True)
    email = models.EmailField('Email', max_length=40, null=True, blank=True)
    # website = models.URLField('Website', null=True, blank=True)
    message = models.TextField('Message')


class Contact(models.Model):
    name = models.CharField('Name', max_length=40)
    email = models.EmailField('Email', max_length=40)
    subject = models.CharField('Subject', max_length=255)
    message = models.TextField('Message')

    # moderations
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta: 
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return f"{self.name} subject: {self.subject}"

    def get_email(self):
        return self.email


class SavedArticle(models.Model):
    user = models.ForeignKey(USER_MODEL, on_delete=models.CASCADE, related_name='saved_articles',)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='recipe_saved_articles', null=True, blank=True)
    story = models.ForeignKey(Story, on_delete=models.CASCADE, related_name='story_saved_articles', null=True, blank=True)

    # moderations
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta: 
        verbose_name = 'Saved Article'
        verbose_name_plural = 'Saved Articles'

    def __str__(self):
        return f"{self.user} recipe: {self.recipe} story: {self.story}"


class Subscriber(models.Model):
    # information's
    email = models.EmailField('Email', max_length=30, unique=True)
    is_active = models.BooleanField('is active', default=True)

    # moderation's
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta: 
        verbose_name = 'Subscriber'
        verbose_name_plural = 'Subscribers'

    def __str__(self):
        return self.email


"""
|id | message | parent_id |
| 1 | Eladi | null |
| 2 | Chsdnfklsdf | 1 |
| 3 | Chsdnfklsdf | 1 |
| 4 | Chsdnfklsdf | null |
| 5 | Chsdnfklsdf | 2 |
"""

# 1,       4 
# 2, 3     []
# 5, []

