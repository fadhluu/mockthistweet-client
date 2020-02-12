from django.shortcuts import render
from .bot import Bot

# Create your views here.


def index(request):
    ck = ""
    cs = ""
    at = ""
    ats = ""
    bot = Bot(ck, cs, at, ats)
    # mention_timeline = bot.api.mentions_timeline()
    user_profile = bot.get_profile()
    user_profile.profile_image_url = user_profile.profile_image_url.replace(
        "_normal", "")
    context = {
        # 'mention_timeline': mention_timeline,
        'user_profile': user_profile
    }
    return render(request, 'client/index.html', context)
