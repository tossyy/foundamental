from allauth.account.adapter import DefaultAccountAdapter
from .models import *


class AccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=True):
        user = super().save_user(request, user, form, commit=False)

        user.userType = request.POST.get('userType')

        # ユーザーIDを取得するために一旦保存する
        user.save()

        if user.userType == UserType.COUNSELOR.value:
            # カウンセラーユーザー
            counselor = UserDetailCounselor()
            counselor.user_id = user.id
            counselor.age = request.POST.get('age')
            counselor.save()

        elif user.userType == UserType.ENTREPRENEUR.value:
            # 起業家ユーザー
            entrepreneur = UserDetailEntrepreneur()
            entrepreneur.user_id = user.id
            entrepreneur.companyName = request.POST.get('companyName')
            entrepreneur.save()

        elif user.userType == UserType.ADMIN.value:
            # 管理者ユーザー
            admin = UserDetailAdmin()
            admin.user_id = user.id
            admin.save()

        else:
            print('エラー発生')
            raise Exception
