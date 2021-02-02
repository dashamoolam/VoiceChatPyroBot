import pymongo
from config import MONGO_DB_URI


try:
    client = pymongo.MongoClient(MONGO_DB_URI)
    db = client["vcpb"]
    playlist = db["playlist"]
except:
    pass


def add_to_playlist(title, url):
    all_ = playlist.find_one({'url': url})
    if all_:
        return False
    playlist.insert_one(
        {
            "title": title,
            "url": url,
        }
    )
    return True


def remove_from_playlist(url):
    all_ = playlist.find_one({'url': url})
    if all_:
        playlist.delete_one({"url": url})
        return True
    return False


def get_playlist():
    all_ = playlist.find()
    all_ = [i for i in all_]

    if len(all_) != 0:
        return all_
    else:
        return False


def remove_all():
    all_ = get_playlist()
    if not all_:
        return False

    for item in all_:
        playlist.delete_one({"url": item["url"]})
    return True
