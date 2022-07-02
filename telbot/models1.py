# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from tkinter import CASCADE
from django.db import models




class Accrual(models.Model):
    accrual_id = models.AutoField(primary_key=True)
    counterparty_id = models.IntegerField()
    image = models.CharField(max_length=255)
    currency_code = models.CharField(max_length=3)
    currency_value = models.DecimalField(max_digits=9, decimal_places=2)
    total = models.DecimalField(max_digits=9, decimal_places=2)
    comment = models.CharField(max_length=255)
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'accrual'


class Action(models.Model):
    action_id = models.AutoField(primary_key=True)
    status = models.IntegerField()
    sort_order = models.IntegerField()
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()
    user_id = models.IntegerField()
    acom = models.IntegerField()
    viewed = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'action'


class ActionComment(models.Model):
    action_comment_id = models.AutoField(primary_key=True)
    action_id = models.IntegerField()
    status = models.IntegerField()
    parent_id = models.IntegerField()
    customer_id = models.IntegerField()
    author = models.CharField(max_length=128)
    date_added = models.DateTimeField()
    text = models.TextField()

    class Meta:
        managed = False
        db_table = 'action_comment'


class ActionDescription(models.Model):
    action_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    title = models.CharField(max_length=255)
    description = models.TextField()
    description_short = models.TextField()
    meta_title = models.CharField(max_length=255)
    meta_description = models.CharField(max_length=255)
    meta_keyword = models.CharField(max_length=255)
    tag = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'action_description'
        unique_together = (('action_id', 'language_id'),)


class ActionMedia(models.Model):
    action_id = models.IntegerField(primary_key=True)
    sort_order = models.IntegerField()
    status = models.IntegerField()
    type = models.IntegerField()
    value = models.TextField()

    class Meta:
        managed = False
        db_table = 'action_media'
        unique_together = (('action_id', 'sort_order'),)


class Address(models.Model):
    address_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    firstname = models.CharField(max_length=32)
    lastname = models.CharField(max_length=32)
    company = models.CharField(max_length=40)
    address_1 = models.CharField(max_length=128)
    address_2 = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    postcode = models.CharField(max_length=10)
    country_id = models.IntegerField()
    zone_id = models.IntegerField()
    custom_field = models.TextField()

    class Meta:
        managed = False
        db_table = 'address'


class Affiliate(models.Model):
    affiliate_id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=32)
    lastname = models.CharField(max_length=32)
    email = models.CharField(max_length=96)
    telephone = models.CharField(max_length=32)
    fax = models.CharField(max_length=32)
    password = models.CharField(max_length=40)
    salt = models.CharField(max_length=9)
    company = models.CharField(max_length=40)
    website = models.CharField(max_length=255)
    address_1 = models.CharField(max_length=128)
    address_2 = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    postcode = models.CharField(max_length=10)
    country_id = models.IntegerField()
    zone_id = models.IntegerField()
    code = models.CharField(max_length=64)
    commission = models.DecimalField(max_digits=4, decimal_places=2)
    tax = models.CharField(max_length=64)
    payment = models.CharField(max_length=6)
    cheque = models.CharField(max_length=100)
    paypal = models.CharField(max_length=64)
    bank_name = models.CharField(max_length=64)
    bank_branch_number = models.CharField(max_length=64)
    bank_swift_code = models.CharField(max_length=64)
    bank_account_name = models.CharField(max_length=64)
    bank_account_number = models.CharField(max_length=64)
    ip = models.CharField(max_length=40)
    status = models.IntegerField()
    approved = models.IntegerField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'affiliate'


class AffiliateActivity(models.Model):
    activity_id = models.AutoField(primary_key=True)
    affiliate_id = models.IntegerField()
    key = models.CharField(max_length=64)
    data = models.TextField()
    ip = models.CharField(max_length=40)
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'affiliate_activity'


class AffiliateLogin(models.Model):
    affiliate_login_id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=96)
    ip = models.CharField(max_length=40)
    total = models.IntegerField()
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'affiliate_login'


class AffiliateTransaction(models.Model):
    affiliate_transaction_id = models.AutoField(primary_key=True)
    affiliate_id = models.IntegerField()
    order_id = models.IntegerField()
    description = models.TextField()
    amount = models.DecimalField(max_digits=15, decimal_places=4)
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'affiliate_transaction'


class Api(models.Model):
    api_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    key = models.TextField()
    status = models.IntegerField()
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'api'


class ApiIp(models.Model):
    api_ip_id = models.AutoField(primary_key=True)
    api_id = models.IntegerField()
    ip = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'api_ip'


class ApiSession(models.Model):
    api_session_id = models.AutoField(primary_key=True)
    api_id = models.IntegerField()
    token = models.CharField(max_length=32)
    session_id = models.CharField(max_length=32)
    session_name = models.CharField(max_length=32)
    ip = models.CharField(max_length=40)
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'api_session'


class Attribute(models.Model):
    attribute_id = models.AutoField(primary_key=True)
    attribute_group_id = models.IntegerField()
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'attribute'


class AttributeDescription(models.Model):
    attribute_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    name = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'attribute_description'
        unique_together = (('attribute_id', 'language_id'),)


class AttributeGroup(models.Model):
    attribute_group_id = models.AutoField(primary_key=True)
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'attribute_group'


class AttributeGroupDescription(models.Model):
    attribute_group_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    name = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'attribute_group_description'
        unique_together = (('attribute_group_id', 'language_id'),)


class Banner(models.Model):
    banner_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'banner'


class BannerImage(models.Model):
    banner_image_id = models.AutoField(primary_key=True)
    banner_id = models.IntegerField()
    link = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'banner_image'


class BannerImageDescription(models.Model):
    banner_image_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    banner_id = models.IntegerField()
    title = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'banner_image_description'
        unique_together = (('banner_image_id', 'language_id'),)


class Blog(models.Model):
    blog_id = models.AutoField(primary_key=True)
    status = models.IntegerField()
    sort_order = models.IntegerField()
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()
    user_id = models.IntegerField()
    acom = models.IntegerField()
    viewed = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'blog'


class BlogComment(models.Model):
    blog_comment_id = models.AutoField(primary_key=True)
    blog_id = models.IntegerField()
    status = models.IntegerField()
    parent_id = models.IntegerField()
    customer_id = models.IntegerField()
    author = models.CharField(max_length=128)
    date_added = models.DateTimeField()
    text = models.TextField()

    class Meta:
        managed = False
        db_table = 'blog_comment'


class BlogDescription(models.Model):
    blog_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    title = models.CharField(max_length=255)
    description = models.TextField()
    description_short = models.TextField()
    meta_title = models.CharField(max_length=255)
    meta_description = models.CharField(max_length=255)
    meta_keyword = models.CharField(max_length=255)
    tag = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'blog_description'
        unique_together = (('blog_id', 'language_id'),)


class BlogMedia(models.Model):
    blog_id = models.IntegerField(primary_key=True)
    sort_order = models.IntegerField()
    status = models.IntegerField()
    type = models.IntegerField()
    value = models.TextField()

    class Meta:
        managed = False
        db_table = 'blog_media'
        unique_together = (('blog_id', 'sort_order'),)


class CallList(models.Model):
    call_list_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    user_id = models.IntegerField()
    date_start = models.DateField()
    date_end = models.DateField()
    date_added = models.DateTimeField()
    description = models.TextField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'call_list'


class CallListClient(models.Model):
    call_list_id = models.IntegerField(primary_key=True)
    client_id = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'call_list_client'
        unique_together = (('call_list_id', 'client_id'),)


class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    client_id = models.IntegerField()
    session_id = models.CharField(max_length=32)
    product_id = models.IntegerField()
    imei = models.CharField(max_length=19)
    recurring_id = models.IntegerField()
    option = models.TextField()
    quantity = models.IntegerField()
    date_added = models.DateTimeField()
    price = models.DecimalField(max_digits=15, decimal_places=4)

    class Meta:
        managed = False
        db_table = 'cart'


class CashMove(models.Model):
    move_id = models.AutoField(primary_key=True)
    date_added = models.DateTimeField()
    from_cashbox_id = models.IntegerField()
    to_cashbox_id = models.IntegerField()
    sum_nal = models.DecimalField(max_digits=15, decimal_places=4)
    currency_code = models.CharField(max_length=3)
    sum_beznal = models.DecimalField(max_digits=15, decimal_places=4)
    sum = models.DecimalField(max_digits=15, decimal_places=4)
    from_type_money = models.CharField(max_length=10)
    in_type_money = models.CharField(max_length=10)
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cash_move'


class Cashbox(models.Model):
    cashbox_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'cashbox'


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


class CategoryFilter(models.Model):
    category_id = models.IntegerField(primary_key=True)
    filter_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'category_filter'
        unique_together = (('category_id', 'filter_id'),)


class CategoryFilters(models.Model):
    category_id = models.IntegerField()
    type = models.CharField(max_length=1)
    value = models.IntegerField()
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'category_filters'


class CategoryPath(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='cater', primary_key=True)
    path_id = models.IntegerField()
    level = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'category_path'
        unique_together = (('category_id', 'path_id'),)


class CategoryTags(models.Model):
    category_id = models.IntegerField(primary_key=True)
    tags_id = models.IntegerField()
    seo_h1 = models.CharField(max_length=255)
    description = models.TextField()
    description_lite = models.TextField()
    meta_title = models.CharField(max_length=255)
    meta_description = models.CharField(max_length=255)
    meta_keyword = models.CharField(max_length=255)
    image = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'category_tags'
        unique_together = (('category_id', 'tags_id'),)


class CategoryToLayout(models.Model):
    category_id = models.IntegerField(primary_key=True)
    store_id = models.IntegerField()
    layout_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'category_to_layout'
        unique_together = (('category_id', 'store_id'),)


class CategoryToStore(models.Model):
    category_id = models.IntegerField(primary_key=True)
    store_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'category_to_store'
        unique_together = (('category_id', 'store_id'),)


class CategoryUrl1(models.Model):
    # id = models.AutoField()
    category_id = models.PositiveIntegerField(primary_key=True)
    #Category, on_delete=models.CASCADE
    url = models.CharField(max_length=255)
    description = models.CharField(max_length=128)
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'category_url'
        # app_label = 'default'


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
        app_label = 'default'


class ClientAddress(models.Model):
    address_id = models.AutoField(primary_key=True)
    client_id = models.IntegerField()
    firstname = models.CharField(max_length=32)
    lastname = models.CharField(max_length=32)
    company = models.CharField(max_length=40)
    address_1 = models.CharField(max_length=128)
    address_2 = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    postcode = models.CharField(max_length=10)
    country_id = models.IntegerField()
    zone_id = models.IntegerField()
    custom_field = models.TextField()

    class Meta:
        managed = False
        db_table = 'client_address'


class ClientBonus(models.Model):
    product_id = models.IntegerField(primary_key=True)
    client_group_id = models.IntegerField()
    type = models.CharField(max_length=1)
    value = models.DecimalField(max_digits=9, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'client_bonus'
        unique_together = (('product_id', 'client_group_id'),)


class ClientCategories(models.Model):
    client_id = models.IntegerField()
    order_id = models.IntegerField()
    category_id = models.IntegerField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'client_categories'


class ClientCoupon(models.Model):
    client_coupon_id = models.AutoField(primary_key=True)
    client_id = models.IntegerField()
    coupon_id = models.IntegerField()
    order_id = models.IntegerField()
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'client_coupon'


class ClientGroup(models.Model):
    client_group_id = models.AutoField(primary_key=True)
    approval = models.IntegerField()
    sort_order = models.IntegerField()
    sms = models.IntegerField()
    order_status_id = models.IntegerField()
    stock_id = models.IntegerField()
    cashbox_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'client_group'


class ClientGroupDescription(models.Model):
    client_group_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    name = models.CharField(max_length=32)
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'client_group_description'
        unique_together = (('client_group_id', 'language_id'),)


class ClientHistory(models.Model):
    history_id = models.AutoField(primary_key=True)
    client_id = models.IntegerField()
    message = models.TextField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'client_history'


class ClientHistoryBinotel(models.Model):
    call_id = models.BigIntegerField(primary_key=True)
    call_type = models.IntegerField()
    internal_number = models.CharField(max_length=20)
    external_number = models.CharField(max_length=20)
    waitsec = models.IntegerField()
    billsec = models.IntegerField()
    binotel_id = models.IntegerField()
    date = models.DateTimeField()
    manager = models.CharField(max_length=20)
    disposition = models.CharField(max_length=20)
    sms = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'client_history_binotel'


class ClientHistoryStatus(models.Model):
    client_history_status_id = models.AutoField(primary_key=True)
    client_id = models.IntegerField()
    description = models.TextField()
    status = models.IntegerField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'client_history_status'


class ClientLabel(models.Model):
    label_id = models.AutoField(primary_key=True)
    client_id = models.IntegerField()
    product_ids = models.CharField(max_length=255)
    product_names = models.TextField()
    comment = models.TextField()
    date_added = models.DateTimeField()
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'client_label'


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
        app_label = 'default'


class ClientWishlist(models.Model):
    client_id = models.IntegerField(primary_key=True)
    product_id = models.IntegerField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'client_wishlist'
        unique_together = (('client_id', 'product_id'),)


class Conversions(models.Model):
    conversion_id = models.AutoField(primary_key=True)
    date_added = models.DateField()
    cashbox_id = models.IntegerField()
    before_currency = models.CharField(max_length=5)
    after_currency = models.CharField(max_length=5)
    before_sum = models.DecimalField(max_digits=10, decimal_places=4)
    after_sum = models.DecimalField(max_digits=10, decimal_places=4)
    from_type_money = models.CharField(max_length=10)
    in_type_money = models.CharField(max_length=10)
    course = models.DecimalField(max_digits=10, decimal_places=4)
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'conversions'


class Counterparty(models.Model):
    counterparty_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    contact_name = models.CharField(max_length=255)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    comment = models.TextField()
    date_added = models.DateTimeField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'counterparty'


class Country(models.Model):
    country_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    iso_code_2 = models.CharField(max_length=2)
    iso_code_3 = models.CharField(max_length=3)
    address_format = models.TextField()
    postcode_required = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'country'


class Coupon(models.Model):
    coupon_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    code = models.CharField(max_length=10)
    type = models.CharField(max_length=1)
    discount = models.DecimalField(max_digits=15, decimal_places=4)
    logged = models.IntegerField()
    shipping = models.IntegerField()
    total = models.DecimalField(max_digits=15, decimal_places=4)
    max = models.DecimalField(max_digits=5, decimal_places=2)
    date_start = models.DateField()
    date_end = models.DateField()
    uses_total = models.IntegerField()
    uses_customer = models.CharField(max_length=11)
    status = models.IntegerField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'coupon'


class CouponCategory(models.Model):
    coupon_id = models.IntegerField(primary_key=True)
    category_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'coupon_category'
        unique_together = (('coupon_id', 'category_id'),)


class CouponCustomerGroup(models.Model):
    coupon_customer_group_id = models.AutoField(primary_key=True)
    coupon_id = models.IntegerField()
    customer_group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'coupon_customer_group'


class CouponHistory(models.Model):
    coupon_history_id = models.AutoField(primary_key=True)
    coupon_id = models.IntegerField()
    order_id = models.IntegerField()
    customer_id = models.IntegerField()
    amount = models.DecimalField(max_digits=15, decimal_places=4)
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'coupon_history'


class CouponProduct(models.Model):
    coupon_product_id = models.AutoField(primary_key=True)
    coupon_id = models.IntegerField()
    product_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'coupon_product'


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


class CustomField(models.Model):
    custom_field_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=32)
    value = models.TextField()
    location = models.CharField(max_length=7)
    status = models.IntegerField()
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'custom_field'


class CustomFieldCustomerGroup(models.Model):
    custom_field_id = models.IntegerField(primary_key=True)
    customer_group_id = models.IntegerField()
    required = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'custom_field_customer_group'
        unique_together = (('custom_field_id', 'customer_group_id'),)


class CustomFieldDescription(models.Model):
    custom_field_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    name = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'custom_field_description'
        unique_together = (('custom_field_id', 'language_id'),)


class CustomFieldValue(models.Model):
    custom_field_value_id = models.AutoField(primary_key=True)
    custom_field_id = models.IntegerField()
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'custom_field_value'


class CustomFieldValueDescription(models.Model):
    custom_field_value_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    custom_field_id = models.IntegerField()
    name = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'custom_field_value_description'
        unique_together = (('custom_field_value_id', 'language_id'),)


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_group_id = models.IntegerField()
    store_id = models.IntegerField()
    firstname = models.CharField(max_length=32)
    lastname = models.CharField(max_length=32)
    email = models.CharField(max_length=96)
    telephone = models.CharField(max_length=32)
    fax = models.CharField(max_length=32)
    password = models.CharField(max_length=40)
    salt = models.CharField(max_length=9)
    cart = models.TextField(blank=True, null=True)
    wishlist = models.TextField(blank=True, null=True)
    newsletter = models.IntegerField()
    address_id = models.IntegerField()
    custom_field = models.TextField()
    ip = models.CharField(max_length=40)
    status = models.IntegerField()
    approved = models.IntegerField()
    safe = models.IntegerField()
    token = models.TextField()
    date_added = models.DateTimeField()
    sex = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'customer'


class CustomerActivity(models.Model):
    activity_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    key = models.CharField(max_length=64)
    data = models.TextField()
    ip = models.CharField(max_length=40)
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'customer_activity'


class CustomerGroup(models.Model):
    customer_group_id = models.AutoField(primary_key=True)
    approval = models.IntegerField()
    sort_order = models.IntegerField()
    sms = models.IntegerField()
    order_status_id = models.IntegerField()
    stock_id = models.IntegerField()
    cashbox_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'customer_group'


class CustomerGroupDescription(models.Model):
    customer_group_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    name = models.CharField(max_length=32)
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'customer_group_description'
        unique_together = (('customer_group_id', 'language_id'),)


class CustomerHistory(models.Model):
    customer_history_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'customer_history'


class CustomerIp(models.Model):
    customer_ip_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    ip = models.CharField(max_length=40)
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'customer_ip'


class CustomerLogin(models.Model):
    customer_login_id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=96)
    ip = models.CharField(max_length=40)
    total = models.IntegerField()
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'customer_login'


class CustomerOnline(models.Model):
    ip = models.CharField(primary_key=True, max_length=40)
    customer_id = models.IntegerField()
    url = models.TextField()
    referer = models.TextField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'customer_online'


class CustomerReward(models.Model):
    customer_reward_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    order_id = models.IntegerField()
    description = models.TextField()
    points = models.IntegerField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'customer_reward'


class CustomerTransaction(models.Model):
    customer_transaction_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    order_id = models.IntegerField()
    description = models.TextField()
    amount = models.DecimalField(max_digits=15, decimal_places=4)
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'customer_transaction'


class CustomerWishlist(models.Model):
    customer_id = models.IntegerField(primary_key=True)
    product_id = models.IntegerField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'customer_wishlist'
        unique_together = (('customer_id', 'product_id'),)


class Description(models.Model):
    description_id = models.AutoField(primary_key=True)
    language_id = models.IntegerField()
    name = models.CharField(max_length=255)
    description = models.TextField()
    description_lite = models.TextField()
    faq = models.TextField()
    faq_title = models.CharField(max_length=255)
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'description'


class Docs(models.Model):
    docs_id = models.AutoField(primary_key=True)
    type = models.IntegerField()
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()
    order_id = models.IntegerField()
    stock_id = models.IntegerField()
    return_id = models.IntegerField()
    author_id = models.IntegerField()
    order_status_id = models.IntegerField()
    cashbox_id = models.IntegerField()
    type_cost_id = models.IntegerField()
    type_prihod_id = models.IntegerField()
    conversion_id = models.IntegerField()
    move_id = models.IntegerField()
    sum_nal = models.DecimalField(max_digits=15, decimal_places=2)
    sum_beznal = models.DecimalField(max_digits=15, decimal_places=2)
    comment = models.CharField(max_length=255)
    expenses = models.IntegerField()
    customer_group_id = models.IntegerField()
    currency_code = models.CharField(max_length=3)
    currency_value = models.DecimalField(max_digits=15, decimal_places=4)
    image = models.CharField(max_length=255, blank=True, null=True)
    provider_id = models.IntegerField()
    purchase_type = models.IntegerField()
    unit_id = models.IntegerField()
    counterparty_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'docs'


class Download(models.Model):
    download_id = models.AutoField(primary_key=True)
    filename = models.CharField(max_length=128)
    mask = models.CharField(max_length=128)
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'download'


class DownloadDescription(models.Model):
    download_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    name = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'download_description'
        unique_together = (('download_id', 'language_id'),)


class EbayCategory(models.Model):
    ebay_category_id = models.AutoField(primary_key=True)
    categoryid = models.IntegerField(db_column='CategoryID')  # Field name made lowercase.
    categoryparentid = models.IntegerField(db_column='CategoryParentID')  # Field name made lowercase.
    categorylevel = models.SmallIntegerField(db_column='CategoryLevel')  # Field name made lowercase.
    categoryname = models.CharField(db_column='CategoryName', max_length=100)  # Field name made lowercase.
    bestofferenabled = models.IntegerField(db_column='BestOfferEnabled')  # Field name made lowercase.
    autopayenabled = models.IntegerField(db_column='AutoPayEnabled')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ebay_category'


class EbayCategoryHistory(models.Model):
    ebay_category_history_id = models.AutoField(primary_key=True)
    categoryid = models.IntegerField(db_column='CategoryID')  # Field name made lowercase.
    breadcrumb = models.CharField(max_length=255)
    used = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ebay_category_history'


class EbayImageImport(models.Model):
    image_original = models.TextField()
    image_new = models.TextField()
    name = models.TextField()
    product_id = models.IntegerField()
    imgcount = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ebay_image_import'


class EbayListing(models.Model):
    ebay_listing_id = models.AutoField(primary_key=True)
    ebay_item_id = models.CharField(max_length=100)
    product_id = models.IntegerField()
    variant = models.IntegerField()
    status = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'ebay_listing'


class EbayListingPending(models.Model):
    ebay_listing_pending_id = models.AutoField(primary_key=True)
    ebay_item_id = models.CharField(max_length=25)
    product_id = models.IntegerField()
    key = models.CharField(max_length=50)
    variant = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ebay_listing_pending'


class EbayOrder(models.Model):
    ebay_order_id = models.AutoField(primary_key=True)
    parent_ebay_order_id = models.IntegerField()
    order_id = models.IntegerField()
    smp_id = models.IntegerField()
    tracking_no = models.CharField(max_length=100)
    carrier_id = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'ebay_order'


class EbayOrderLock(models.Model):
    smp_id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'ebay_order_lock'


class EbayPaymentMethod(models.Model):
    ebay_payment_method_id = models.AutoField(primary_key=True)
    ebay_name = models.CharField(max_length=50)
    local_name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'ebay_payment_method'


class EbayProfile(models.Model):
    ebay_profile_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    type = models.IntegerField()
    default = models.IntegerField()
    data = models.TextField()

    class Meta:
        managed = False
        db_table = 'ebay_profile'


class EbaySettingOption(models.Model):
    ebay_setting_option_id = models.AutoField(primary_key=True)
    key = models.CharField(max_length=100)
    last_updated = models.DateTimeField()
    data = models.TextField()

    class Meta:
        managed = False
        db_table = 'ebay_setting_option'


class EbayShipping(models.Model):
    ebay_shipping_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=100)
    internationalservice = models.IntegerField(db_column='InternationalService')  # Field name made lowercase.
    shippingservice = models.CharField(db_column='ShippingService', max_length=100)  # Field name made lowercase.
    shippingserviceid = models.IntegerField(db_column='ShippingServiceID')  # Field name made lowercase.
    servicetype = models.CharField(db_column='ServiceType', max_length=100)  # Field name made lowercase.
    validforsellingflow = models.IntegerField(db_column='ValidForSellingFlow')  # Field name made lowercase.
    shippingcategory = models.CharField(db_column='ShippingCategory', max_length=100)  # Field name made lowercase.
    shippingtimemin = models.IntegerField(db_column='ShippingTimeMin')  # Field name made lowercase.
    shippingtimemax = models.IntegerField(db_column='ShippingTimeMax')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ebay_shipping'


class EbayShippingLocation(models.Model):
    ebay_shipping_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=100)
    detail_version = models.CharField(max_length=100)
    shipping_location = models.CharField(max_length=100)
    update_time = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'ebay_shipping_location'


class EbayShippingLocationExclude(models.Model):
    ebay_shipping_exclude_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    region = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'ebay_shipping_location_exclude'


class EbayStockReserve(models.Model):
    product_id = models.IntegerField()
    variant_id = models.CharField(max_length=100)
    item_id = models.CharField(max_length=100)
    reserve = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ebay_stock_reserve'


class EbayTemplate(models.Model):
    template_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    html = models.TextField()

    class Meta:
        managed = False
        db_table = 'ebay_template'


class EbayTransaction(models.Model):
    ebay_transaction_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    product_id = models.IntegerField()
    sku = models.CharField(max_length=100)
    txn_id = models.CharField(max_length=100)
    item_id = models.CharField(max_length=100)
    containing_order_id = models.CharField(max_length=100)
    order_line_id = models.CharField(max_length=100)
    qty = models.IntegerField()
    smp_id = models.IntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ebay_transaction'


class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=32)
    trigger = models.TextField()
    action = models.TextField()

    class Meta:
        managed = False
        db_table = 'event'


class Extension(models.Model):
    extension_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=32)
    code = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'extension'


class FacebookEvents(models.Model):
    data = models.CharField(max_length=4092)
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'facebook_events'


class FaqInfo(models.Model):
    faq_info_id = models.AutoField(primary_key=True)
    faq_tab_id = models.IntegerField()
    title = models.CharField(max_length=128)
    description = models.TextField()
    status = models.IntegerField()
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'faq_info'


class FaqTab(models.Model):
    faq_tab_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=64)
    status = models.IntegerField()
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'faq_tab'


class Filter(models.Model):
    filter_id = models.AutoField(primary_key=True)
    filter_group_id = models.IntegerField()
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'filter'


class FilterDescription(models.Model):
    filter_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    filter_group_id = models.IntegerField()
    name = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'filter_description'
        unique_together = (('filter_id', 'language_id'),)


class FilterGroup(models.Model):
    filter_group_id = models.AutoField(primary_key=True)
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'filter_group'


class FilterGroupDescription(models.Model):
    filter_group_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    name = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'filter_group_description'
        unique_together = (('filter_group_id', 'language_id'),)


class GeoZone(models.Model):
    geo_zone_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=255)
    date_modified = models.DateTimeField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'geo_zone'


class GoogleBaseCategory(models.Model):
    google_base_category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'google_base_category'


class GoogleBaseCategoryToCategory(models.Model):
    google_base_category_id = models.IntegerField(primary_key=True)
    category_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'google_base_category_to_category'
        unique_together = (('google_base_category_id', 'category_id'),)


class GroupCost(models.Model):
    group_cost_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    counterparty = models.IntegerField()
    unit = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'group_cost'


class Information(models.Model):
    information_id = models.AutoField(primary_key=True)
    bottom = models.IntegerField()
    sort_order = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'information'


class InformationDescription(models.Model):
    information_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    title = models.CharField(max_length=64)
    description = models.TextField()
    meta_title = models.CharField(max_length=255)
    meta_description = models.CharField(max_length=255)
    meta_keyword = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'information_description'
        unique_together = (('information_id', 'language_id'),)


class InformationToLayout(models.Model):
    information_id = models.IntegerField(primary_key=True)
    store_id = models.IntegerField()
    layout_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'information_to_layout'
        unique_together = (('information_id', 'store_id'),)


class InformationToStore(models.Model):
    information_id = models.IntegerField(primary_key=True)
    store_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'information_to_store'
        unique_together = (('information_id', 'store_id'),)


class Inventory(models.Model):
    inventory_id = models.AutoField(primary_key=True)
    date = models.DateField()
    comment = models.CharField(max_length=50)
    inventory_status_id = models.IntegerField()
    stock_id = models.IntegerField()
    summa = models.DecimalField(max_digits=15, decimal_places=4)

    class Meta:
        managed = False
        db_table = 'inventory'


class InventoryProduct(models.Model):
    inventory_product_id = models.AutoField(primary_key=True)
    inventory_id = models.IntegerField()
    product_id = models.IntegerField()
    imei = models.CharField(max_length=19)
    option_comb_id = models.IntegerField()
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=15, decimal_places=4)

    class Meta:
        managed = False
        db_table = 'inventory_product'


class KBanner(models.Model):
    k_banner_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'k_banner'


class KBannerSlide(models.Model):
    k_banner_slide_id = models.AutoField(primary_key=True)
    k_banner_id = models.IntegerField()
    title = models.CharField(max_length=100)
    image = models.CharField(max_length=255)
    sort_order = models.IntegerField()
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    timing = models.IntegerField()
    time_start = models.TimeField()
    time_end = models.TimeField()

    class Meta:
        managed = False
        db_table = 'k_banner_slide'


class KBannerSlideData(models.Model):
    k_banner_slide_data_id = models.AutoField(primary_key=True)
    k_banner_id = models.IntegerField()
    k_banner_slide_id = models.IntegerField()
    name = models.CharField(max_length=100)
    language_id = models.IntegerField()
    class_field = models.CharField(db_column='class', max_length=255)  # Field renamed because it was a Python reserved word.
    type = models.IntegerField()
    pos_x = models.CharField(max_length=16)
    pos_y = models.CharField(max_length=16)
    data = models.TextField()
    url = models.CharField(max_length=255)
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'k_banner_slide_data'


class Language(models.Model):
    language_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    code = models.CharField(max_length=5)
    locale = models.CharField(max_length=255)
    image = models.CharField(max_length=64)
    directory = models.CharField(max_length=32)
    sort_order = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'language'


class Layout(models.Model):
    layout_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'layout'


class LayoutModule(models.Model):
    layout_module_id = models.AutoField(primary_key=True)
    layout_id = models.IntegerField()
    code = models.CharField(max_length=64)
    position = models.CharField(max_length=14)
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'layout_module'


class LayoutRoute(models.Model):
    layout_route_id = models.AutoField(primary_key=True)
    layout_id = models.IntegerField()
    store_id = models.IntegerField()
    route = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'layout_route'


class LengthClass(models.Model):
    length_class_id = models.AutoField(primary_key=True)
    value = models.DecimalField(max_digits=15, decimal_places=8)

    class Meta:
        managed = False
        db_table = 'length_class'


class LengthClassDescription(models.Model):
    length_class_id = models.AutoField(primary_key=True)
    language_id = models.IntegerField()
    title = models.CharField(max_length=32)
    unit = models.CharField(max_length=4)

    class Meta:
        managed = False
        db_table = 'length_class_description'
        unique_together = (('length_class_id', 'language_id'),)


class Location(models.Model):
    location_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    address = models.TextField()
    telephone = models.CharField(max_length=32)
    fax = models.CharField(max_length=32)
    geocode = models.CharField(max_length=32)
    image = models.CharField(max_length=255, blank=True, null=True)
    open = models.TextField()
    comment = models.TextField()

    class Meta:
        managed = False
        db_table = 'location'


class Manufacturer(models.Model):
    manufacturer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    name_old = models.CharField(max_length=64)
    image = models.CharField(max_length=255, blank=True, null=True)
    logo = models.CharField(max_length=255)
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'manufacturer'


class ManufacturerDescription(models.Model):
    manufacturer_id = models.IntegerField(primary_key=True)
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
        db_table = 'manufacturer_description'
        unique_together = (('manufacturer_id', 'language_id'),)


class ManufacturerToStore(models.Model):
    manufacturer_id = models.IntegerField(primary_key=True)
    store_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'manufacturer_to_store'
        unique_together = (('manufacturer_id', 'store_id'),)


class Marketing(models.Model):
    marketing_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    description = models.TextField()
    code = models.CharField(max_length=64)
    clicks = models.IntegerField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'marketing'


class Modification(models.Model):
    modification_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    code = models.CharField(max_length=64)
    author = models.CharField(max_length=64)
    version = models.CharField(max_length=32)
    link = models.CharField(max_length=255)
    xml = models.TextField()
    status = models.IntegerField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'modification'


class Module(models.Model):
    module_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    code = models.CharField(max_length=32)
    setting = models.TextField()

    class Meta:
        managed = False
        db_table = 'module'


class MonoOrders(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    invoiceid = models.CharField(db_column='InvoiceId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    orderid = models.IntegerField(db_column='OrderId', blank=True, null=True)  # Field name made lowercase.
    secretkey = models.CharField(db_column='SecretKey', max_length=51, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mono_orders'


class Move(models.Model):
    move_id = models.AutoField(primary_key=True)
    date = models.DateField()
    comment = models.CharField(max_length=50)
    move_status_id = models.IntegerField()
    from_stock_id = models.IntegerField()
    to_stock_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'move'


class MoveProduct(models.Model):
    move_product_id = models.AutoField(primary_key=True)
    move_id = models.IntegerField()
    product_id = models.IntegerField()
    imei = models.CharField(max_length=19)
    option_comb_id = models.IntegerField()
    quantity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'move_product'


class OpenbayFaq(models.Model):
    route = models.TextField()

    class Meta:
        managed = False
        db_table = 'openbay_faq'


class Option(models.Model):
    option_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=32)
    sort_order = models.IntegerField()
    for_filter = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'option'


class OptionComb(models.Model):
    option_comb_id = models.AutoField(primary_key=True)
    product_id = models.IntegerField()
    active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'option_comb'


class OptionCombValue(models.Model):
    option_comb_value_id = models.AutoField(primary_key=True)
    option_comb_id = models.IntegerField()
    option_id = models.IntegerField()
    option_value_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'option_comb_value'


class OptionDescription(models.Model):
    option_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    name = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'option_description'
        unique_together = (('option_id', 'language_id'),)


class OptionValue(models.Model):
    option_value_id = models.AutoField(primary_key=True)
    option_id = models.IntegerField()
    image = models.CharField(max_length=255)
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'option_value'


class OptionValueDescription(models.Model):
    option_value_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    option_id = models.IntegerField()
    name = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'option_value_description'
        unique_together = (('option_value_id', 'language_id'),)


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
        app_label = 'default'


class OrderCustomField(models.Model):
    order_custom_field_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    custom_field_id = models.IntegerField()
    custom_field_value_id = models.IntegerField()
    name = models.CharField(max_length=255)
    value = models.TextField()
    type = models.CharField(max_length=32)
    location = models.CharField(max_length=16)

    class Meta:
        managed = False
        db_table = 'order_custom_field'


class OrderHistory(models.Model):
    order_history_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    order_status_id = models.IntegerField()
    notify = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'order_history'


class OrderOption(models.Model):
    order_option_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    order_product = models.IntegerField()
    product_option_id = models.IntegerField()
    product_option_value_id = models.IntegerField()
    name = models.CharField(max_length=255)
    value = models.TextField()
    type = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'order_option'


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
        app_label = 'default'


class OrderReceipt(models.Model):
    order_receipt_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    receipt_id = models.CharField(max_length=60)
    serial = models.IntegerField()
    status = models.CharField(max_length=32)
    fiscal_code = models.CharField(max_length=32)
    fiscal_date = models.CharField(max_length=32)
    is_created_offline = models.IntegerField()
    is_sent_dps = models.IntegerField()
    sent_dps_at = models.IntegerField()
    all_json_data = models.TextField()
    type = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'order_receipt'


class OrderRecurring(models.Model):
    order_recurring_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    reference = models.CharField(max_length=255)
    product_id = models.IntegerField()
    product_name = models.CharField(max_length=255)
    product_quantity = models.IntegerField()
    recurring_id = models.IntegerField()
    recurring_name = models.CharField(max_length=255)
    recurring_description = models.CharField(max_length=255)
    recurring_frequency = models.CharField(max_length=25)
    recurring_cycle = models.SmallIntegerField()
    recurring_duration = models.SmallIntegerField()
    recurring_price = models.DecimalField(max_digits=10, decimal_places=4)
    trial = models.IntegerField()
    trial_frequency = models.CharField(max_length=25)
    trial_cycle = models.SmallIntegerField()
    trial_duration = models.SmallIntegerField()
    trial_price = models.DecimalField(max_digits=10, decimal_places=4)
    status = models.IntegerField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'order_recurring'


class OrderRecurringTransaction(models.Model):
    order_recurring_transaction_id = models.AutoField(primary_key=True)
    order_recurring_id = models.IntegerField()
    reference = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=4)
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'order_recurring_transaction'


class OrderStatus(models.Model):
    order_status_id = models.AutoField(primary_key=True)
    language_id = models.IntegerField()
    name = models.CharField(max_length=32)
    sms = models.CharField(max_length=128)
    delay = models.CharField(max_length=10)
    viber_data = models.TextField()

    class Meta:
        managed = False
        db_table = 'order_status'
        unique_together = (('order_status_id', 'language_id'),)


class OrderTotal(models.Model):
    order_total_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    code = models.CharField(max_length=32)
    title = models.CharField(max_length=255)
    value = models.DecimalField(max_digits=15, decimal_places=4)
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'order_total'


class OrderVoucher(models.Model):
    order_voucher_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    voucher_id = models.IntegerField()
    description = models.CharField(max_length=255)
    code = models.CharField(max_length=10)
    from_name = models.CharField(max_length=64)
    from_email = models.CharField(max_length=96)
    to_name = models.CharField(max_length=64)
    to_email = models.CharField(max_length=96)
    voucher_theme_id = models.IntegerField()
    message = models.TextField()
    amount = models.DecimalField(max_digits=15, decimal_places=4)

    class Meta:
        managed = False
        db_table = 'order_voucher'


class Preorder(models.Model):
    preorder_id = models.AutoField(primary_key=True)
    product_id = models.IntegerField()
    name = models.CharField(max_length=255)
    options = models.CharField(max_length=255)
    quantity = models.IntegerField()
    firstname = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    date_added = models.DateTimeField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'preorder'


class Price(models.Model):
    price_id = models.AutoField(primary_key=True)
    product_id = models.IntegerField(unique=True)
    price_z = models.DecimalField(max_digits=9, decimal_places=2)
    profit = models.DecimalField(max_digits=9, decimal_places=2)
    use_profit = models.IntegerField()
    position = models.CharField(max_length=100)
    provider = models.CharField(max_length=100)
    date_modified = models.DateTimeField()
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'price'


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


class ProductAttribute(models.Model):
    product_id = models.IntegerField(primary_key=True)
    attribute_id = models.IntegerField()
    language_id = models.IntegerField()
    text = models.TextField()

    class Meta:
        managed = False
        db_table = 'product_attribute'
        unique_together = (('product_id', 'attribute_id', 'language_id'),)


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


class ProductDiscount(models.Model):
    product_discount_id = models.AutoField(primary_key=True)
    product_id = models.IntegerField()
    customer_group_id = models.IntegerField()
    quantity = models.IntegerField()
    priority = models.IntegerField()
    price = models.DecimalField(max_digits=15, decimal_places=4)
    date_start = models.DateField()
    date_end = models.DateField()

    class Meta:
        managed = False
        db_table = 'product_discount'


class ProductFilter(models.Model):
    product_id = models.IntegerField(primary_key=True)
    filter_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'product_filter'
        unique_together = (('product_id', 'filter_id'),)


class ProductImage(models.Model):
    product_image_id = models.AutoField(primary_key=True)
    product_id = models.IntegerField()
    image = models.CharField(max_length=255, blank=True, null=True)
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'product_image'


class ProductLink(models.Model):
    product_link_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    option = models.CharField(max_length=255)
    image = models.CharField(max_length=100)
    image_product = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'product_link'


class ProductOption(models.Model):
    product_option_id = models.AutoField(primary_key=True)
    product_id = models.IntegerField()
    option_id = models.IntegerField()
    value = models.TextField()
    required = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'product_option'


class ProductOptionValue(models.Model):
    product_option_value_id = models.AutoField(primary_key=True)
    product_option_id = models.IntegerField()
    product_id = models.IntegerField()
    option_id = models.IntegerField()
    option_value_id = models.IntegerField()
    quantity = models.IntegerField()
    subtract = models.IntegerField()
    price = models.DecimalField(max_digits=15, decimal_places=4)
    price_prefix = models.CharField(max_length=1)
    points = models.IntegerField()
    points_prefix = models.CharField(max_length=1)
    weight = models.DecimalField(max_digits=15, decimal_places=8)
    weight_prefix = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'product_option_value'


class ProductRecurring(models.Model):
    product_id = models.IntegerField(primary_key=True)
    recurring_id = models.IntegerField()
    customer_group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'product_recurring'
        unique_together = (('product_id', 'recurring_id', 'customer_group_id'),)


class ProductRelated(models.Model):
    product_id = models.IntegerField(primary_key=True)
    related_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'product_related'
        unique_together = (('product_id', 'related_id'),)


class ProductReward(models.Model):
    product_reward_id = models.AutoField(primary_key=True)
    product_id = models.IntegerField()
    customer_group_id = models.IntegerField()
    points = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'product_reward'


class ProductSpecial(models.Model):
    product_special_id = models.AutoField(primary_key=True)
    product_id = models.IntegerField()
    customer_group_id = models.IntegerField()
    priority = models.IntegerField()
    price = models.DecimalField(max_digits=15, decimal_places=4)
    price_z = models.DecimalField(max_digits=15, decimal_places=4)
    price_calc = models.IntegerField()
    date_start = models.DateField()
    date_end = models.DateField()

    class Meta:
        managed = False
        db_table = 'product_special'


class ProductToCategory(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, primary_key=True)
    category_id = models.IntegerField()
    main_category = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'product_to_category'
        unique_together = (('product_id', 'category_id'),)


class ProductToDownload(models.Model):
    product_id = models.IntegerField(primary_key=True)
    download_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'product_to_download'
        unique_together = (('product_id', 'download_id'),)


class ProductToLayout(models.Model):
    product_id = models.IntegerField(primary_key=True)
    store_id = models.IntegerField()
    layout_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'product_to_layout'
        unique_together = (('product_id', 'store_id'),)


class ProductToStore(models.Model):
    product_id = models.IntegerField(primary_key=True)
    store_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'product_to_store'
        unique_together = (('product_id', 'store_id'),)


class Provider(models.Model):
    provider_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    contact_name = models.CharField(max_length=255)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    login = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    web = models.CharField(max_length=255)
    comment = models.TextField()
    date_added = models.DateTimeField()
    status = models.IntegerField()
    days = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'provider'


class ProviderReturn(models.Model):
    provider_return_id = models.AutoField(primary_key=True)
    provider_id = models.IntegerField()
    date = models.DateField()
    total = models.DecimalField(max_digits=15, decimal_places=4)
    comment = models.CharField(max_length=50)
    provider_return_status_id = models.IntegerField()
    stock_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'provider_return'


class ProviderReturnProduct(models.Model):
    provider_return_product_id = models.AutoField(primary_key=True)
    provider_return_id = models.IntegerField()
    purchase_product_id = models.IntegerField()
    purchase_order_product_id = models.IntegerField()
    product_id = models.IntegerField()
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=15, decimal_places=4)
    currency_code = models.CharField(max_length=3)
    currency_value = models.DecimalField(max_digits=15, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'provider_return_product'


class Purchase(models.Model):
    purchase_id = models.AutoField(primary_key=True)
    date = models.DateField()
    comment = models.CharField(max_length=50)
    purchase_status_id = models.IntegerField()
    stock_id = models.IntegerField()
    order_number = models.CharField(max_length=30)
    track_number = models.CharField(max_length=30)
    delivery_status = models.CharField(max_length=30)
    delivery_price = models.DecimalField(max_digits=15, decimal_places=4)
    delivery_coef = models.DecimalField(max_digits=15, decimal_places=4)
    additional_price = models.DecimalField(max_digits=15, decimal_places=4)
    additional_coef = models.DecimalField(max_digits=15, decimal_places=4)
    product_coef = models.DecimalField(max_digits=15, decimal_places=4)
    currency_code = models.CharField(max_length=3, blank=True, null=True)
    weight = models.DecimalField(max_digits=15, decimal_places=4)
    provider_id = models.IntegerField()
    purchase_type = models.IntegerField()
    author_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'purchase'


class PurchaseOrderProduct(models.Model):
    purchase_order_product_id = models.AutoField(primary_key=True)
    purchase_product_id = models.IntegerField(blank=True, null=True)
    order_product_id = models.IntegerField()
    product_id = models.IntegerField(blank=True, null=True)
    option_comb_id = models.IntegerField()
    quantity = models.IntegerField()
    test = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'purchase_order_product'


class PurchasePrice(models.Model):
    purchase_product_id = models.IntegerField(primary_key=True)
    purchase_id = models.IntegerField()
    product_id = models.IntegerField()
    price_z = models.DecimalField(max_digits=65, decimal_places=20, blank=True, null=True)
    price = models.DecimalField(max_digits=59, decimal_places=12, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'purchase_price'


class PurchaseProduct(models.Model):
    purchase_product_id = models.AutoField(primary_key=True)
    purchase_id = models.IntegerField()
    product_id = models.IntegerField()
    imei = models.CharField(max_length=19)
    option_comb_id = models.IntegerField()
    quantity = models.IntegerField()
    quantity_lack = models.IntegerField()
    price = models.DecimalField(max_digits=15, decimal_places=4)
    weight = models.DecimalField(max_digits=15, decimal_places=4)
    price_z = models.DecimalField(max_digits=15, decimal_places=4)
    price_base = models.DecimalField(max_digits=15, decimal_places=4)

    class Meta:
        managed = False
        db_table = 'purchase_product'


class PurchaseStatus(models.Model):
    purchase_status_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'purchase_status'


class QuickLinks(models.Model):
    quick_links_id = models.AutoField(primary_key=True)
    text = models.CharField(max_length=64)
    link = models.CharField(max_length=255)
    order = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'quick_links'


class Recurring(models.Model):
    recurring_id = models.AutoField(primary_key=True)
    price = models.DecimalField(max_digits=10, decimal_places=4)
    frequency = models.CharField(max_length=10)
    duration = models.PositiveIntegerField()
    cycle = models.PositiveIntegerField()
    trial_status = models.IntegerField()
    trial_price = models.DecimalField(max_digits=10, decimal_places=4)
    trial_frequency = models.CharField(max_length=10)
    trial_duration = models.PositiveIntegerField()
    trial_cycle = models.PositiveIntegerField()
    status = models.IntegerField()
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'recurring'


class RecurringDescription(models.Model):
    recurring_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'recurring_description'
        unique_together = (('recurring_id', 'language_id'),)


class Return(models.Model):
    return_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    product_id = models.IntegerField()
    imei = models.CharField(max_length=19)
    customer_id = models.IntegerField()
    client_id = models.IntegerField()
    firstname = models.CharField(max_length=32)
    lastname = models.CharField(max_length=32)
    email = models.CharField(max_length=96)
    telephone = models.CharField(max_length=32)
    product = models.CharField(max_length=255)
    model = models.CharField(max_length=64)
    quantity = models.IntegerField()
    opened = models.IntegerField()
    return_reason_id = models.IntegerField()
    return_action_id = models.IntegerField()
    return_status_id = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    sum = models.FloatField()
    currency_code = models.CharField(max_length=3)
    stock_id = models.IntegerField()
    user_id = models.IntegerField()
    option_comb_id = models.IntegerField()
    date_ordered = models.DateField()
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()
    edit_total = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'return'


class ReturnAction(models.Model):
    return_action_id = models.AutoField(primary_key=True)
    language_id = models.IntegerField()
    name = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'return_action'
        unique_together = (('return_action_id', 'language_id'),)


class ReturnHistory(models.Model):
    return_history_id = models.AutoField(primary_key=True)
    return_id = models.IntegerField()
    return_status_id = models.IntegerField()
    notify = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'return_history'


class ReturnReason(models.Model):
    return_reason_id = models.AutoField(primary_key=True)
    language_id = models.IntegerField()
    name = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'return_reason'
        unique_together = (('return_reason_id', 'language_id'),)


class ReturnStatus(models.Model):
    return_status_id = models.AutoField(primary_key=True)
    language_id = models.IntegerField()
    name = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'return_status'
        unique_together = (('return_status_id', 'language_id'),)


class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    product_id = models.IntegerField()
    customer_id = models.IntegerField()
    author = models.CharField(max_length=64)
    text = models.TextField()
    rating = models.IntegerField()
    status = models.IntegerField()
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()
    user_id = models.IntegerField()
    answer = models.TextField()

    class Meta:
        managed = False
        db_table = 'review'


class RevsliderAttachmentImages(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    file_name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'revslider_attachment_images'


class RevsliderCss(models.Model):
    handle = models.TextField()
    settings = models.TextField(blank=True, null=True)
    hover = models.TextField(blank=True, null=True)
    params = models.TextField()

    class Meta:
        managed = False
        db_table = 'revslider_css'


class RevsliderLayerAnimations(models.Model):
    handle = models.TextField()
    params = models.TextField()

    class Meta:
        managed = False
        db_table = 'revslider_layer_animations'


class RevsliderSettings(models.Model):
    general = models.TextField()
    params = models.TextField()

    class Meta:
        managed = False
        db_table = 'revslider_settings'


class RevsliderSliders(models.Model):
    title = models.TextField()
    alias = models.TextField(blank=True, null=True)
    params = models.TextField()

    class Meta:
        managed = False
        db_table = 'revslider_sliders'


class RevsliderSlides(models.Model):
    slider_id = models.IntegerField()
    slide_order = models.IntegerField()
    params = models.TextField()
    layers = models.TextField()

    class Meta:
        managed = False
        db_table = 'revslider_slides'


class RevsliderStaticSlides(models.Model):
    slider_id = models.IntegerField()
    params = models.TextField()
    layers = models.TextField()

    class Meta:
        managed = False
        db_table = 'revslider_static_slides'


class Setting(models.Model):
    setting_id = models.AutoField(primary_key=True)
    store_id = models.IntegerField()
    code = models.CharField(max_length=32)
    key = models.CharField(max_length=64)
    value = models.TextField()
    serialized = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'setting'


class Shift(models.Model):
    shift_id = models.CharField(max_length=64)
    serial = models.IntegerField()
    status = models.CharField(max_length=32)
    z_report_id = models.CharField(max_length=64)
    all_json_data = models.TextField()

    class Meta:
        managed = False
        db_table = 'shift'


class Sms(models.Model):
    sms_id = models.AutoField(primary_key=True)
    date_added = models.DateTimeField()
    date_send = models.DateTimeField()
    destination = models.CharField(max_length=64)
    message = models.CharField(max_length=255)
    sender = models.CharField(max_length=11)
    params = models.TextField()
    status = models.IntegerField()
    result = models.TextField()
    date_locked = models.DateTimeField()
    customer_id = models.IntegerField()
    user_id = models.IntegerField()
    viber_data = models.TextField()

    class Meta:
        managed = False
        db_table = 'sms'


class Stock(models.Model):
    stock_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'stock'


class StockControl(models.Model):
    stock_control_id = models.AutoField(primary_key=True)
    stock_id = models.IntegerField()
    product_id = models.IntegerField()
    min = models.IntegerField()
    plan = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'stock_control'
        unique_together = (('product_id', 'stock_id'),)


class StockOptionComb(models.Model):
    stock_option_comb_id = models.AutoField(primary_key=True)
    stock_id = models.IntegerField()
    product_id = models.IntegerField()
    imei = models.CharField(max_length=19)
    option_comb_id = models.IntegerField()
    quantity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'stock_option_comb'
        unique_together = (('stock_id', 'product_id', 'option_comb_id', 'imei'),)


class StockOptionCombOld(models.Model):
    stock_option_comb_id = models.AutoField(primary_key=True)
    stock_id = models.IntegerField()
    product_id = models.IntegerField()
    option_comb_id = models.IntegerField()
    quantity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'stock_option_comb_old'
        unique_together = (('stock_id', 'product_id', 'option_comb_id'),)


class StockStatus(models.Model):
    stock_status_id = models.AutoField(primary_key=True)
    language_id = models.IntegerField()
    name = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'stock_status'
        unique_together = (('stock_status_id', 'language_id'),)


class Store(models.Model):
    store_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    url = models.CharField(max_length=255)
    ssl = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'store'


class Subscribe(models.Model):
    email = models.CharField(primary_key=True, max_length=128)
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'subscribe'


class Tags(models.Model):
    tags_id = models.AutoField(primary_key=True)
    status = models.IntegerField()
    name = models.CharField(max_length=255)
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tags'


class TagsToItem(models.Model):
    tags_id = models.IntegerField()
    item_type = models.IntegerField(primary_key=True)
    item_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tags_to_item'
        unique_together = (('item_type', 'item_id', 'tags_id'),)


class TaxClass(models.Model):
    tax_class_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)
    description = models.CharField(max_length=255)
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tax_class'


class TaxRate(models.Model):
    tax_rate_id = models.AutoField(primary_key=True)
    geo_zone_id = models.IntegerField()
    name = models.CharField(max_length=32)
    rate = models.DecimalField(max_digits=15, decimal_places=4)
    type = models.CharField(max_length=1)
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tax_rate'


class TaxRateToCustomerGroup(models.Model):
    tax_rate_id = models.IntegerField(primary_key=True)
    customer_group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tax_rate_to_customer_group'
        unique_together = (('tax_rate_id', 'customer_group_id'),)


class TaxRule(models.Model):
    tax_rule_id = models.AutoField(primary_key=True)
    tax_class_id = models.IntegerField()
    tax_rate_id = models.IntegerField()
    based = models.CharField(max_length=10)
    priority = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tax_rule'


class TypeCost(models.Model):
    type_cost_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    group_cost_id = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'type_cost'


class TypePrihod(models.Model):
    type_prihod_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'type_prihod'


class Unit(models.Model):
    unit_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    contact_name = models.CharField(max_length=255)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    comment = models.TextField()
    date_added = models.DateTimeField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'unit'


class Upload(models.Model):
    upload_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    filename = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'upload'


class UrlAlias(models.Model):
    url_alias_id = models.AutoField(primary_key=True)
    query = models.CharField(max_length=255)
    keyword = models.CharField(max_length=255)
    seo_mod = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'url_alias'


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_group_id = models.IntegerField()
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=40)
    salt = models.CharField(max_length=9)
    firstname = models.CharField(max_length=32)
    lastname = models.CharField(max_length=32)
    email = models.CharField(max_length=96)
    image = models.CharField(max_length=255)
    code = models.CharField(max_length=40)
    ip = models.CharField(max_length=40)
    status = models.IntegerField()
    date_added = models.DateTimeField()
    binotel_number = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'user'


class UserBonus(models.Model):
    product_id = models.IntegerField(primary_key=True)
    user_group_id = models.IntegerField()
    type = models.CharField(max_length=1)
    value = models.DecimalField(max_digits=9, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'user_bonus'
        unique_together = (('product_id', 'user_group_id'),)


class UserGroup(models.Model):
    user_group_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    permission = models.TextField()
    bonus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_group'


class UserGroupAccess(models.Model):
    route = models.CharField(max_length=64)
    user_group_id = models.IntegerField()
    value = models.TextField()

    class Meta:
        managed = False
        db_table = 'user_group_access'


class Voucher(models.Model):
    voucher_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    code = models.CharField(max_length=10)
    from_name = models.CharField(max_length=64)
    from_email = models.CharField(max_length=96)
    to_name = models.CharField(max_length=64)
    to_email = models.CharField(max_length=96)
    voucher_theme_id = models.IntegerField()
    message = models.TextField()
    amount = models.DecimalField(max_digits=15, decimal_places=4)
    status = models.IntegerField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'voucher'


class VoucherHistory(models.Model):
    voucher_history_id = models.AutoField(primary_key=True)
    voucher_id = models.IntegerField()
    order_id = models.IntegerField()
    amount = models.DecimalField(max_digits=15, decimal_places=4)
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'voucher_history'


class VoucherTheme(models.Model):
    voucher_theme_id = models.AutoField(primary_key=True)
    image = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'voucher_theme'


class VoucherThemeDescription(models.Model):
    voucher_theme_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    name = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'voucher_theme_description'
        unique_together = (('voucher_theme_id', 'language_id'),)


class Warranty(models.Model):
    warranty_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    product_id = models.IntegerField()
    imei = models.CharField(max_length=16)
    customer_id = models.IntegerField()
    client_id = models.IntegerField()
    product = models.CharField(max_length=255)
    model = models.CharField(max_length=64)
    quantity = models.IntegerField()
    complectation = models.TextField()
    condition = models.TextField()
    warranty_status_id = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    sum = models.FloatField()
    currency_code = models.CharField(max_length=3)
    stock_id = models.IntegerField()
    option_comb_id = models.IntegerField()
    date_ordered = models.DateField()
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'warranty'


class WarrantyHistory(models.Model):
    warranty_history_id = models.AutoField(primary_key=True)
    warranty_id = models.IntegerField()
    warranty_status_id = models.IntegerField()
    notify = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'warranty_history'


class WarrantyStatus(models.Model):
    warranty_status_id = models.AutoField(primary_key=True)
    language_id = models.IntegerField()
    name = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'warranty_status'
        unique_together = (('warranty_status_id', 'language_id'),)


class WeightClass(models.Model):
    weight_class_id = models.AutoField(primary_key=True)
    value = models.DecimalField(max_digits=15, decimal_places=8)

    class Meta:
        managed = False
        db_table = 'weight_class'


class WeightClassDescription(models.Model):
    weight_class_id = models.AutoField(primary_key=True)
    language_id = models.IntegerField()
    title = models.CharField(max_length=32)
    unit = models.CharField(max_length=4)

    class Meta:
        managed = False
        db_table = 'weight_class_description'
        unique_together = (('weight_class_id', 'language_id'),)


class Zone(models.Model):
    zone_id = models.AutoField(primary_key=True)
    country_id = models.IntegerField()
    name = models.CharField(max_length=128)
    code = models.CharField(max_length=32)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'zone'


class ZoneToGeoZone(models.Model):
    zone_to_geo_zone_id = models.AutoField(primary_key=True)
    country_id = models.IntegerField()
    zone_id = models.IntegerField()
    geo_zone_id = models.IntegerField()
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'zone_to_geo_zone'
