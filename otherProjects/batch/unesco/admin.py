from django.contrib import admin

# Register your models here.
import unesco.models as m

admin.site.register(m.Site)
admin.site.register(m.Category)
admin.site.register(m.Region)
admin.site.register(m.State)
admin.site.register(m.Iso)