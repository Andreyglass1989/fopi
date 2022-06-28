from unicodedata import category
from telbot.models import Category, CategoryDescription, CategoryUrl1, CategoryPath, UrlAlias, ProductToCategory
from django.db.models import F
from django.core.exceptions import ObjectDoesNotExist

# c = Category.objects.get(category_id="3508")
# cd = CategoryDescription.objects.get(category_id=c.category_id)


#first level
# c = Category.objects.filter(category_id=)
"""
    Уживані iPhone
    New Iphone
    Apple
"""


#################################### Second level #####################################################

#second level Apple 3508
def second_level_apple():
    # cu = CategoryUrl1.objects.filter(category_id=3508).exclude(description='iPhone').order_by("sort_order")
    cu = Category.objects.filter(category_id__in=[3587,3671,3679,3735,3522,3511]) #.exclude(category_id=3512)
    return cu

#second level iphone 3512
def second_level_iphone():
    # cu = CategoryUrl1.objects.filter(category_id=3512).exclude(description__icontains='Уживані').order_by("sort_order")
    cu = CategoryPath.objects.filter(path_id=3512, category__status=1).exclude(category_id=3512).order_by("category_id")
    return cu



#second Уживані iphone 3786
def second_level_uzhivani_iphone():
    list_uzh = []
    cp = CategoryPath.objects.filter(path_id=3786, category__status=1).exclude(category_id__in=[3786,3794])
    for c in cp:
        list_uzh.append(c)
    # cp = CategoryPath.objects.filter(path_id=3786).exclude(category_id__in=[3786,3794])
    # for c in cp:
    #     try:
    #         c1 = Category.objects.get(category_id=c.category_id, status=1)
    #         list_uzh.append(c1)
    #     except ObjectDoesNotExist:
    #         c.category_id
    return list_uzh
# c_url = UrlAlias.objects.filter(keyword__icontains = "ujyvani-iphone")
# for c_u in c_url:
    # print(c_u.query[12:])

# cu = CategoryUrl1.objects.filter(category_id=3512, description__icontains='Уживані').order_by("sort_order")
# for x in cu:
    # print(x.description)


#################################### Third level #####################################################
ptc = ProductToCategory.objects.filter(category_id=3815, product__status=1, product__price__gt=0)
for p in ptc:
    # if p.product.status==1 and p.product.price!=0.0:
    print(p.product.price, p.product.prod_desc.name)




# list_uzh = []
# # cd = CategoryDescription.objects.get(name__icontains="iPhone 11")

# # cp = CategoryPath.objects.filter(path_id=3508).exclude(category_id=3508)
# # cp.count()
# cu = CategoryUrl1.objects.filter(category_id=3508).exclude(category_id=3512).order_by("sort_order")

# # for c in cp:
# #     try:
# #         c1 = Category.objects.get(category_id=c.category_id, status=1)
# #         list_a.append(c1)
# #     except ObjectDoesNotExist:
# #         c.category_id

# for l in list_a:
#     try:
#         cd = CategoryDescription.objects.get(category_id=l.category_id)
#         print(cd.name)
#     except ObjectDoesNotExist:
#         l.category_id

#     # cp1 = CategoryDescription.objects.get(category_id=c.category_id)

#     # print(cp1.name)
# # cu = CategoryUrl1.objects.filter(category_id=3508).order_by("sort_order")





"""
iphone => 3512 => 3803(pro)
                  3804(promax)
path_id



ipad= 3617
mac = 3587
watch =3679
airpods = 3735
apple TV = 3522
navushnyky-ta-akustyka-apple = 3511





cabeli = 3495
zaryadni-prystroyi-apple = 3736


ujyvani-iphone = 3786



url_alias table
https://fopi.ua/apple-store/ +?query=zaryadni-prystroyi-apple
"""
# cu = CategoryUrl1.objects.filter(category_id=3508).order_by("sort_order")