from site_setup.models import SiteSetup


def Context_processor_example(request):
    return {
        "example": "isso veio do context processor example!"
    }


def Site_Setup(request):
    setup = SiteSetup.objects.order_by("-id").first()
    return {
        "Site_Setup": setup,
    }
