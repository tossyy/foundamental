from allauth.account.adapter import DefaultAccountAdapter
from .models import *


class AccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=True):
        """
        This is called when saving user via allauth registration.
        We override this to set additional data on user object.
        """
        # Do not persist the user yet so we pass commit=False
        # (last argument)
        user = super(AccountAdapter, self).save_user(request, user, form, commit=False)
        # user.userType = form.cleaned_data.get('userType')
        user.userType = UserType(request.POST['userType'])

        if not user.userType:
            user.userType = UserType(USERTYPE_DEFAULT)  # デフォルトのユーザ種別を設定

        # ユーザIDを取得するために一旦保存する
        user.save()

        if int(user.userType.id) == USERTYPE_COUNSELOR:
            # カウンセラーユーザ
            counselor = UserDetailCounselor()
            counselor.user_id = user.id
            counselor.save()
        else:
            # それ以外は起業家ユーザ
            user.userType = UserType(USERTYPE_ENTREPRENEUR)
            entrepreneur = UserDetailEntrepreneur()
            entrepreneur.user_id = user.id
            entrepreneur.save()
