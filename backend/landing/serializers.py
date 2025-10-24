from rest_framework import serializers
from .models import Header, Summary, PdfFile, PdfCategory, Project, ProjectImage


class HeaderSerializer(serializers.ModelSerializer):
    avatar = serializers.SerializerMethodField()
    background = serializers.SerializerMethodField()

    class Meta:
        model = Header
        fields = ["avatar", "background"]

    def get_avatar(self, obj):
        if obj.avatar:
            url = obj.avatar.url
            # Если Cloudinary, он всегда начинается с https://res.cloudinary.com
            if url.startswith("http"):
                return url
            # если вдруг локальный /media/
            request = self.context.get("request")
            if request:
                return request.build_absolute_uri(url)
            return f"https://pohorila-cv-backend.onrender.com{url}"
        return ""

    def get_background(self, obj):
        if obj.background:
            url = obj.background.url
            if url.startswith("http"):
                return url
            request = self.context.get("request")
            if request:
                return request.build_absolute_uri(url)
            return f"https://pohorila-cv-backend.onrender.com{url}"
        return ""


class PdfCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PdfCategory
        fields = ("id", "name")


class PdfFileSerializer(serializers.ModelSerializer):
    category = PdfCategorySerializer(read_only=True)
    file_url = serializers.SerializerMethodField()
    file_name = serializers.SerializerMethodField()

    class Meta:
        model = PdfFile
        fields = ("id", "file", "title", "category", "file_url", "file_name")

    def get_file_url(self, obj):
        if obj.file:
            url = obj.file.url
            if url.startswith("http"):
                return url
            request = self.context.get("request")
            if request:
                return request.build_absolute_uri(url)
            return f"https://pohorila-cv-backend.onrender.com{url}"
        return ""

    def get_file_name(self, obj):
        if obj.file:
            return obj.file.name.split("/")[-1]
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
            "pdfs",
        )


class ProjectImageSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = ProjectImage
        fields = ["id", "image"]

    def get_image(self, obj):
        if obj.image:
            url = obj.image.url
            if url.startswith("http"):
                return url
            request = self.context.get("request")
            if request:
                return request.build_absolute_uri(url)
            return f"https://pohorila-cv-backend.onrender.com{url}"
        return ""


class ProjectSerializer(serializers.ModelSerializer):
    main_image = serializers.SerializerMethodField()
    images = ProjectImageSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ["id", "title", "main_image", "images"]

    def get_main_image(self, obj):
        if obj.main_image:
            url = obj.main_image.url
            if url.startswith("http"):
                return url
            request = self.context.get("request")
            if request:
                return request.build_absolute_uri(url)
            return f"https://pohorila-cv-backend.onrender.com{url}"
        return ""




