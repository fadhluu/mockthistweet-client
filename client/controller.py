from django.shortcuts import render
from .bot import Bot
from .db_mongo import Database
from .forms.new_tweet import NewTweet
from django.http import HttpResponse

# Create your views here.

db = Database()
db.connect_db("mockthistweet_test")
db.select_col("environment")

ck = db.find_object("consumer_key")
cs = db.find_object("consumer_secret")
at = db.find_object("access_token")
ats = db.find_object("access_token_secret")

bot = Bot(ck, cs, at, ats)


def index(request):
    user_profile = bot.get_profile()
    user_profile.profile_image_url = user_profile.profile_image_url.replace(
        "_normal", "")
    context = {
        # 'mention_timeline': mention_timeline,
        'user_profile': user_profile,
        'form': NewTweet(),
    }
    return render(request, 'client/index.html', context)


def new_tweet(request):
    bot.api.update_status(status=request.POST['new_tweet'])
    return HttpResponse('Update tweet success')
