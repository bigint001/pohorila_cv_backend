from rest_framework import serializers
from .models import Header, Summary, PdfFile, PdfCategory, Project, ProjectImage

class HeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Header
        fields = ['avatar', 'background']


class PdfCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PdfCategory
        fields = ('id', 'name')

class PdfFileSerializer(serializers.ModelSerializer):
    category = PdfCategorySerializer(read_only=True)  # <-- Сериализуем категорию полностью
    file_url = serializers.SerializerMethodField()
    file_name = serializers.SerializerMethodField()

    class Meta:
        model = PdfFile
        fields = ('id', 'file', 'title', 'category', 'file_url', 'file_name')

    def get_file_url(self, obj):
        if obj.file:
            return obj.file.url
        return ""

    def get_file_name(self, obj):
        if obj.file:
            return obj.file.name.split('/')[-1]
        return ""

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
    class Meta:
        model = ProjectImage
        fields = ["id", "image"]

class ProjectSerializer(serializers.ModelSerializer):
    images = ProjectImageSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ["id", "title", "main_image", "images"]
