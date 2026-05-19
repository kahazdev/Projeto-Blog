from django.core.exceptions import ValidationError


def validadorPNG(image):
    if not image.name.lower().endswith(".png"):
        raise ValidationError("A Imagem precisa ser PNG!")
