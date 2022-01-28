# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CafeCount(models.Model):
    in_count = models.FloatField()
    out_count = models.FloatField()
    sum_count = models.IntegerField()
    status_year = models.IntegerField()
    status_month = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cafe_count'


class CafeFranchise(models.Model):
    fran_name = models.CharField(primary_key=True, max_length=256)
    price = models.IntegerField()
    quality_up = models.IntegerField()
    quality_down = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cafe_franchise'


class CafeStatus(models.Model):
    cafe_id = models.AutoField(primary_key=True)
    lng = models.FloatField()
    lat = models.FloatField()
    cafe_area = models.FloatField()
    business = models.IntegerField()
    cafe_name = models.CharField(max_length=256)
    open_date = models.IntegerField()
    close_date = models.IntegerField()
    gu = models.CharField(max_length=256)
    franchise = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cafe_status'


class CommercialArea(models.Model):
    comm_id = models.IntegerField(primary_key=True)
    comm_id_name = models.CharField(max_length=256, blank=True, null=True)
    comm_category = models.CharField(max_length=256)
    comm_category_name = models.CharField(max_length=256)
    lat = models.FloatField()
    lng = models.FloatField()

    class Meta:
        managed = False
        db_table = 'commercial_area'


class Culture(models.Model):
    culture_id = models.AutoField(primary_key=True)
    culture_category = models.CharField(max_length=256, blank=True, null=True)
    culture_name = models.CharField(max_length=256, blank=True, null=True)
    culture_addr = models.CharField(max_length=256, blank=True, null=True)
    lat = models.FloatField()
    lng = models.FloatField()

    class Meta:
        managed = False
        db_table = 'culture'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Population(models.Model):
    gu = models.CharField(primary_key=True, max_length=256)
    number_20_29 = models.IntegerField(db_column='20-29')  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_30_39 = models.IntegerField(db_column='30-39')  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_40_49 = models.IntegerField(db_column='40-49')  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_50_59 = models.IntegerField(db_column='50-59')  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_60_69 = models.IntegerField(db_column='60-69')  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    total_worker = models.IntegerField()
    density = models.IntegerField()
    totalpop = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'population'


class Traffic(models.Model):
    code = models.IntegerField(primary_key=True)
    station = models.CharField(max_length=256)
    lat = models.FloatField()
    lng = models.FloatField()
    coms = models.IntegerField()
    many75 = models.IntegerField()
    trans = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'traffic'
