from django.contrib import admin
from django.utils.html import format_html
from .models import Header, Summary, PdfFile, PdfCategory, Project, ProjectImage

# Header admin
@admin.register(Header)
class HeaderAdmin(admin.ModelAdmin):
    list_display = ("id", "avatar_preview", "background_preview")

    def avatar_preview(self, obj):
        if obj.avatar:
            return format_html('<img src="{}" width="100" />', obj.avatar.url)
        return "-"
    avatar_preview.short_description = "Avatar"

    def background_preview(self, obj):
        if obj.background:
            return format_html('<img src="{}" width="100" />', obj.background.url)
        return "-"
    background_preview.short_description = "Background"


class PdfFileInline(admin.TabularInline):
    model = Summary.pdfs.through
    extra = 1


@admin.register(Summary)
class SummaryAdmin(admin.ModelAdmin):
    inlines = [PdfFileInline]
    exclude = ('pdfs',)


@admin.register(PdfFile)
class PdfFileAdmin(admin.ModelAdmin):
    list_display = ('title', 'file', 'category')
    list_filter = ('category',)


@admin.register(PdfCategory)
class PdfCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1  # сколько полей для добавления сразу видно


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "created_at", "updated_at")
    search_fields = ("title", "description")
    list_filter = ("created_at", "updated_at")
    inlines = [ProjectImageInline]  # показываем картинки прямо в проекте


@admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):
    list_display = ("id", "project", "image")
    search_fields = ("project__title",)
