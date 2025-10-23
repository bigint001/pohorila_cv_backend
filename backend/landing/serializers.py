from rest_framework import serializers
from .models import Header, Summary, PdfFile, PdfCategory, Project, ProjectImage


class HeaderSerializer(serializers.ModelSerializer):
    avatar = serializers.SerializerMethodField()
    background = serializers.SerializerMethodField()

    class Meta:
        model = Header
        fields = ['avatar', 'background']

    def get_avatar(self, obj):
        return obj.avatar.url if obj.avatar else ''

    def get_background(self, obj):
        return obj.background.url if obj.background else ''


class PdfCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PdfCategory
        fields = ('id', 'name')


class PdfFileSerializer(serializers.ModelSerializer):
    category = PdfCategorySerializer(read_only=True)
    file_url = serializers.SerializerMethodField()
    file_name = serializers.SerializerMethodField()

    class Meta:
        model = PdfFile
        fields = ('id', 'file', 'title', 'category', 'file_url', 'file_name')

    def get_file_url(self, obj):
        return obj.file.url if obj.file else ""

    def get_file_name(self, obj):
        return obj.file.name.split('/')[-1] if obj.file else ""


class SummarySerializer(serializers.ModelSerializer):
    pdfs = PdfFileSerializer(many=True, read_only=True)

    class Meta:
        model = Summary
        fields = (
            "id",
            "paragraph_1",
            "paragraph_2",
            "paragraph_3",
            "phone_1",
            "phone_2",
            "email",
            "pdfs"
        )


class ProjectImageSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = ProjectImage
        fields = ["id", "image"]

    def get_image(self, obj):
        return obj.image.url if obj.image else ''


class ProjectSerializer(serializers.ModelSerializer):
    main_image = serializers.SerializerMethodField()
    images = ProjectImageSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ["id", "title", "main_image", "images"]

    def get_main_image(self, obj):
        return obj.main_image.url if obj.main_image else ''


