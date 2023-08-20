# importing python components
from django.contrib import admin

# importing project components
from store import models


admin.site.register(models.Category)
admin.site.register(models.SubCategory)
admin.site.register(models.Currency)
admin.site.register(models.Product)
admin.site.register(models.Tag)
admin.site.register(models.TaggedProduct)
