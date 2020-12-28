from .models import Item
from controllers.categories.models import Category
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator


def home(request, category_id=None, template_name="home.html"):
    sort = request.GET.get("sort", "model")
    page = request.GET.get("page", 1)

    ctx = {}

    if sort == "model":
        ctx["sort_arg"] = "-model"
        ctx["sort_by"] = "model"
    elif sort == "-model":
        ctx["sort_art"] = "model"
        ctx["sort_by"] = "-model"

    base_queryset = Item.objects.prefetch_related("manufacturer", "category")

    if category_id and category_id != "0":
        cat = get_object_or_404(Category, id=category_id)
        base_queryset = base_queryset.filter(category=cat)
        ctx["category"] = cat
        ctx["category_path"] = cat.__str__().split("->")
    elif category_id == "0":
        base_queryset = base_queryset.filter(category__isnull=True)
        ctx["category"] = 0
        ctx["category_path"] = "uncategorized"
    else:
        cat = None

    ctx["object_list"] = base_queryset.order_by(ctx["sort_by"])
    paginator = Paginator(ctx["object_list"], 40)
    ctx["paginator"] = paginator.page(page)
    ctx["page"] = page

    return render(request, template_name, ctx)


def item(request, item_id, template_name="item.html"):
    item = get_object_or_404(Item, id=item_id)
    ctx = {}
    ctx["item"] = item
    return render(request, template_name, ctx)
