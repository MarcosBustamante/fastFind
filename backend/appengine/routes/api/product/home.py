__author__ = 'bustamante'
from gaecookie.decorator import no_csrf
from config.template_middleware import TemplateResponse

@no_csrf
def listing():
    return TemplateResponse()
