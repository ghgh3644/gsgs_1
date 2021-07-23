from django.contrib.auth.models import User
from django.http import HttpResponseForbidden


def account_ownership_required(func): #받는인자의 이름은 맘대로 설정가능
    def decorated(request, *args, **kwargs):
        target_user = User.objects.get(pk=kwargs['pk']) #db에 접근, 유저 객체에서 전부말고말고 pk하나만 가져오기
        if target_user == request.user: #두개가 동일한지 확인
            return func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()

    return decorated