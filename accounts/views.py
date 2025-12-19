from django.shortcuts import render, get_object_or_404
from accounts.models import Profile

def profile_view(request):
    """
    プロフィールページを表示
    - ログインユーザーのプロフィールを取得して表示
    """
    profile = get_object_or_404(Profile, user=request.user)

    return render(request, 'accounts/profile.html', {
        'profile': profile
    })
