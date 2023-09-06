from django import template

register = template.Library()

@register.filter
def to_persian_numbers(number):
    number = str(number)
    translation_table = number.maketrans('0123456789', '۰۱۲۳۴۵۶۷۸۹')

    return number.translate(translation_table)
