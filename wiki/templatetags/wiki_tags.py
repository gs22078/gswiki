from django import template
from wiki import utils

register = template.Library()


def slugify(value):
    return utils.slugify(value)


register.filter('slugify', slugify)


@register.filter()
def unslugify(value):
    return utils.unslugify(value)
