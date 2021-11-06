from category.models import Category


def menu_links(request):
    # فراخوانی تمام دسته بندی ها از دیتابیس
    links = Category.objects.all()
    return dict(links=links)
