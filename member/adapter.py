from allauth.account.adapter import DefaultAccountAdapter
from .models import *


class AccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=True):
        user = super().save_user(request, user, form, commit=False)
        user.userType = form.cleaned_data.get('userType')

        # ユーザーIDを取得するために一旦保存する
        user.save()

        if user.userType == UserType.COUNSELOR:
            # カウンセラーユーザー
            counselor = UserDetailCounselor()
            counselor.user_id = user.id
            counselor.age = form.cleaned_data.get('age')
            counselor.save()

        else:
            # 起業家ユーザー
            entrepreneur = UserDetailEntrepreneur()
            entrepreneur.user_id = user.id
            entrepreneur.companyName = form.cleaned_data.get('companyName')
            entrepreneur.save()
