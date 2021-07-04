


#使得tutorial_content显示这个控件，注意tinymce的大小写
from django.contrib import admin
from .models import Tutorial
from tinymce.widgets import TinyMCE
from django.db import models
# Register your models here.
class TutorialAdmin(admin.ModelAdmin):
    fieldsets = [
            ("Title/Date", {'fields':['tutorial_title',    'tutorial_published']}),
            ("Content", {'fields':['tutorial_content']})
                ]
    formfield_overrides = {
            models.TextField:{'widget': TinyMCE()},
            }
admin.site.register(Tutorial, TutorialAdmin)


'''
#建立分组显示
from django.contrib import admin
from .models import Tutorial
# Register your models here.
class TutorialAdmin(admin.ModelAdmin):
    fieldsets = [
            ("Title/Date", {'fields':['tutorial_title','tutorial_published']}),
            ("Content", {'fields':['tutorial_content']})
                ]

admin.site.register(Tutorial, TutorialAdmin)
'''


'''  原始
from django.contrib import admin
from .models import Tutorial

# Register your models here.

class TutorialAdmin(admin.ModelAdmin):
    fields = ['tutorial_title',
            'tutorial_published',
            'tutorial_content']

admin.site.register(Tutorial, TutorialAdmin)
'''

#admin.site.register(Tutorial)   #2021-07-01 11:52