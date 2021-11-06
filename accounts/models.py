from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# تعریف کاربران
class MyAccountManager(BaseUserManager):
    # یوزر معمولی
    def create_user(self, first_name, last_name, username, email, password=None):
        if not email:
            raise ValueError('User Must Have An Email!')

        if not username:
            raise ValueError('User Must Have An Username!')

        user = self.model(
            # نرمالیز کردن برای تبدیل به حروف کوچک
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    # ادمین اصلی
    def create_superuser(self, first_name, last_name, username, email, password):
        # اینا رو مث همون یوزرها میگیریم
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
        )
        # باید تمام اختیارات را بش بدیم
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.set_password(password)
        user.save(using=self._db)
        return user


# تعریف مدل اکانت
class Account(AbstractBaseUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=250, unique=True)
    phone_number = models.CharField(max_length=50)

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    # به اکانت می گیم که می خوایم از اکانت منیجرخودمون استفاده کنیم
    objects = MyAccountManager()

    # زمانی که اکانتی رو در تمپلت رترن می کنیم می خوایم ایمیل رو نشون بده
    def __str__(self):
        return self.email

    # وقتی ادمین بود می تونه تغییرات رو اعمال کنه
    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True
