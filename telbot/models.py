from tkinter import CASCADE
from django.db import models


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    thumb = models.CharField(max_length=255)
    ico = models.CharField(max_length=32)
    parent_id = models.IntegerField()
    top = models.IntegerField()
    column = models.IntegerField()
    sort_order = models.IntegerField()
    status = models.IntegerField()
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()
    url = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'category'




class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    client_group_id = models.IntegerField()
    store_id = models.IntegerField()
    firstname = models.CharField(max_length=32)
    lastname = models.CharField(max_length=32)
    email = models.CharField(max_length=96)
    telephone_display = models.CharField(max_length=32)
    telephone = models.CharField(max_length=20)
    fax = models.CharField(max_length=32)
    password = models.CharField(max_length=40)
    salt = models.CharField(max_length=9)
    cart = models.TextField(blank=True, null=True)
    wishlist = models.TextField(blank=True, null=True)
    newsletter = models.IntegerField()
    address_id = models.IntegerField()
    region = models.CharField(max_length=100)
    custom_field = models.TextField()
    ip = models.CharField(max_length=40)
    status = models.IntegerField()
    approved = models.IntegerField()
    safe = models.IntegerField()
    token = models.TextField()
    date_added = models.DateTimeField()
    sex = models.IntegerField()
    date_last_order = models.DateTimeField()
    total_bonus = models.DecimalField(max_digits=9, decimal_places=2)
    product_ids = models.CharField(max_length=255)
    product_names = models.TextField()
    comment = models.CharField(max_length=255)
    user_id = models.IntegerField()
    binotel_id = models.IntegerField()
    updated = models.IntegerField()
    last_billsec = models.IntegerField()
    last_date_in = models.DateTimeField()
    last_date_out = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'client'
        # app_label = 'telbot'


class ClientReward(models.Model):
    client_reward_id = models.AutoField(primary_key=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    order_id = models.IntegerField()
    return_id = models.IntegerField()
    description = models.TextField()
    points = models.IntegerField()
    date_added = models.DateTimeField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'client_reward'
        # app_label = 'default'


class Currency(models.Model):
    currency_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)
    code = models.CharField(max_length=3)
    symbol_left = models.CharField(max_length=12)
    symbol_right = models.CharField(max_length=12)
    decimal_place = models.CharField(max_length=1)
    value = models.FloatField()
    status = models.IntegerField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'currency'


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    invoice_no = models.IntegerField()
    invoice_prefix = models.CharField(max_length=26)
    store_id = models.IntegerField()
    store_name = models.CharField(max_length=64)
    store_url = models.CharField(max_length=255)
    customer_id = models.IntegerField()
    customer_group_id = models.IntegerField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    client_group_id = models.IntegerField()
    firstname = models.CharField(max_length=32)
    lastname = models.CharField(max_length=32)
    email = models.CharField(max_length=96)
    telephone = models.CharField(max_length=32)
    fax = models.CharField(max_length=32)
    custom_field = models.TextField()
    payment_firstname = models.CharField(max_length=32)
    payment_lastname = models.CharField(max_length=32)
    payment_company = models.CharField(max_length=40)
    payment_address_1 = models.CharField(max_length=128)
    payment_address_2 = models.CharField(max_length=128)
    payment_city = models.CharField(max_length=128)
    payment_postcode = models.CharField(max_length=10)
    payment_country = models.CharField(max_length=128)
    payment_country_id = models.IntegerField()
    payment_zone = models.CharField(max_length=128)
    payment_zone_id = models.IntegerField()
    payment_address_format = models.TextField()
    payment_custom_field = models.TextField()
    payment_method = models.CharField(max_length=128)
    payment_code = models.CharField(max_length=128)
    shipping_firstname = models.CharField(max_length=32)
    shipping_lastname = models.CharField(max_length=32)
    shipping_company = models.CharField(max_length=40)
    shipping_address_1 = models.CharField(max_length=128)
    shipping_address_2 = models.CharField(max_length=128)
    shipping_city = models.CharField(max_length=128)
    shipping_postcode = models.CharField(max_length=10)
    shipping_country = models.CharField(max_length=128)
    shipping_country_id = models.IntegerField()
    shipping_zone = models.CharField(max_length=128)
    shipping_zone_id = models.IntegerField()
    shipping_address_format = models.TextField()
    shipping_custom_field = models.TextField()
    shipping_method = models.CharField(max_length=128)
    shipping_code = models.CharField(max_length=128)
    comment = models.TextField()
    total = models.DecimalField(max_digits=15, decimal_places=2)
    order_status_id = models.IntegerField()
    affiliate_id = models.IntegerField()
    commission = models.DecimalField(max_digits=15, decimal_places=4)
    marketing_id = models.IntegerField()
    tracking = models.CharField(max_length=64)
    language_id = models.IntegerField()
    currency = models.ForeignKey(Currency, related_name='currency', on_delete=models.CASCADE)
    currency_code = models.CharField(max_length=3)
    currency_value = models.DecimalField(max_digits=15, decimal_places=8)
    ip = models.CharField(max_length=40)
    forwarded_ip = models.CharField(max_length=40)
    user_agent = models.CharField(max_length=255)
    accept_language = models.CharField(max_length=255)
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()
    cost_of_delivery = models.CharField(max_length=20)
    number_of_ttn = models.CharField(max_length=20)
    author_id = models.IntegerField()
    sms_sent = models.IntegerField()
    stock_id = models.IntegerField()
    procent_of_komisia = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'order'
        # app_label = 'default'



class OrderProduct(models.Model):
    order_product_id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_id = models.IntegerField()
    imei = models.CharField(max_length=19)
    name = models.CharField(max_length=255)
    model = models.CharField(max_length=64)
    quantity = models.IntegerField()
    option_comb_id = models.IntegerField()
    price = models.DecimalField(max_digits=15, decimal_places=4)
    total = models.DecimalField(max_digits=15, decimal_places=4)
    guarantee = models.CharField(max_length=255)
    tax = models.DecimalField(max_digits=15, decimal_places=4)
    reward = models.IntegerField()
    url = models.CharField(max_length=255)
    client_bonus = models.DecimalField(max_digits=9, decimal_places=2)
    bonus = models.DecimalField(max_digits=9, decimal_places=2)
    bonus_text = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'order_product'
        # app_label = 'default'



class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    thumb = models.CharField(max_length=255)
    ico = models.CharField(max_length=32)
    parent_id = models.IntegerField()
    top = models.IntegerField()
    column = models.IntegerField()
    sort_order = models.IntegerField()
    status = models.IntegerField()
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()
    url = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'category'


class CategoryDescription(models.Model):
    category = models.ForeignKey(Category, related_name='categor', on_delete=models.CASCADE, primary_key=True)
    language_id = models.IntegerField()
    name = models.CharField(max_length=255)
    description = models.TextField()
    description_lite = models.TextField()
    meta_title = models.CharField(max_length=255)
    meta_description = models.CharField(max_length=255)
    meta_keyword = models.CharField(max_length=255)
    faq = models.TextField()
    faq_title = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'category_description'
        unique_together = (('category_id', 'language_id'),)



class CategoryPath(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='cater', primary_key=True)
    path_id = models.IntegerField()
    level = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'category_path'
        unique_together = (('category_id', 'path_id'),)



class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=64)
    sku = models.CharField(max_length=64)
    upc = models.CharField(max_length=12)
    ean = models.CharField(max_length=14)
    jan = models.CharField(max_length=13)
    isbn = models.CharField(max_length=17)
    mpn = models.CharField(max_length=255)
    location = models.CharField(max_length=128)
    quantity = models.IntegerField()
    description_id = models.IntegerField()
    always_in_stock = models.IntegerField()
    stock_status_id = models.IntegerField()
    image = models.CharField(max_length=255, blank=True, null=True)
    video = models.TextField()
    manufacturer_id = models.IntegerField()
    shipping = models.IntegerField()
    price = models.DecimalField(max_digits=15, decimal_places=4)
    price_z = models.DecimalField(max_digits=15, decimal_places=4)
    price_calc = models.IntegerField()
    points = models.IntegerField()
    tax_class_id = models.IntegerField()
    date_available = models.DateField()
    weight = models.DecimalField(max_digits=15, decimal_places=8)
    weight_class_id = models.IntegerField()
    length = models.DecimalField(max_digits=15, decimal_places=8)
    width = models.DecimalField(max_digits=15, decimal_places=8)
    height = models.DecimalField(max_digits=15, decimal_places=8)
    length_class_id = models.IntegerField()
    subtract = models.IntegerField()
    minimum = models.IntegerField()
    sort_order = models.IntegerField()
    status = models.IntegerField()
    viewed = models.IntegerField()
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()
    url = models.CharField(max_length=255)
    guarantee = models.CharField(max_length=255)
    hotline_url = models.CharField(max_length=255)
    product_link_id = models.IntegerField()
    warranty_month = models.IntegerField()
    warranty_total = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'product'



class ProductDescription(models.Model):
    # product_id = models.IntegerField(primary_key=True)
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name="prod_desc", primary_key=True)
    language_id = models.IntegerField()
    name = models.CharField(max_length=255)
    description = models.TextField()
    description_lite = models.TextField()
    tag = models.TextField()
    meta_title = models.CharField(max_length=255)
    meta_description = models.CharField(max_length=255)
    meta_keyword = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'product_description'
        unique_together = (('product_id', 'language_id'),)


class ProductToCategory(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, primary_key=True)
    category_id = models.IntegerField()
    main_category = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'product_to_category'
        unique_together = (('product_id', 'category_id'),)


class UrlAlias(models.Model):
    url_alias_id = models.AutoField(primary_key=True)
    query = models.CharField(max_length=255)
    keyword = models.CharField(max_length=255)
    seo_mod = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'url_alias'