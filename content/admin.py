from django.contrib import admin

from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin

from content.models import CImages, Menu, Content
from product.models import Images


class ContentImageInline(admin.TabularInline):
    model = CImages
    extra = 3


class MenuContentInlıne(admin.TabularInline):
    model = Content
    extra = 1


class ContentAdmin(admin.ModelAdmin):
    list_display = ['title', 'type', 'status', 'create_at']
    list_filter = ['status', 'type']
    inlines = [ContentImageInline]
    prepopulated_fields = {'slug': ('title',)}


class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title', 'image_tag']


class MenuAdmin(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title', 'status')
    list_filter = ['status']
    inlines = [MenuContentInlıne]


admin.site.register(Menu, MenuAdmin)
admin.site.register(Content, ContentAdmin)
admin.site.register(CImages, ImagesAdmin)
