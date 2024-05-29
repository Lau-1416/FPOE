from django.contrib import admin
from .models.models_api import Post
from .models.models_ropa import Ropa
admin.site.register(Post)
admin.site.register(Ropa)