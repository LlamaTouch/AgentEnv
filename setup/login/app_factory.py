from .Apps import *


def app_factory(device, app_name):
    if app_name == "Google_Tasks":
        return Google_Tasks(device, app_name)
    elif app_name == "YT_Music":
        return YT_Music(device, app_name)
    elif app_name == "Google_Podcast":
        return Google_Podcast(device, app_name)
    elif app_name == "Google_Play_Books":
        return Google_Play_Books(device, app_name)
    elif app_name == "Google_Drive":
        return Google_Drive(device, app_name)
    elif app_name == "Google_Keep":
        return Google_Keep(device, app_name)
    elif app_name == "Google_News":
        return Google_News(device, app_name)
    elif app_name == "Youtube":
        return Youtube(device, app_name)
    elif app_name == "WEBTOON":
        return WEBTOON(device, app_name)
    elif app_name == "Pinterest":
        return Pinterest(device, app_name)
    elif app_name == "NewsBreak":
        return NewsBreak(device, app_name)
    elif app_name == "BurgerKing":
        return BurgerKing(device, app_name)
    elif app_name == "Yelp":
        return Yelp(device, app_name)
    elif app_name == "Expedia":
        return Expedia(device, app_name)
    elif app_name == "Reddit":
        return Reddit(device, app_name)
    elif app_name == "Coursera":
        return Coursera(device, app_name)
    elif app_name == "Spotify":
        return Spotify(device, app_name)
    elif app_name == "Gmail":
        return Gmail(device, app_name)
    elif app_name == "CBS_Sports":
        return CBS_Sports(device, app_name)
    elif app_name == "Google_Keep_Notes":
        return Google_Keep_Notes(device, app_name)
    else:
        raise ValueError("Unsupported app type")
