# git clone https://github.com/skypro-008/coursework2_source
import json

path = './data/data.json'


# def json_load():
#     with open(path, 'r', encoding='UTF-8') as f:
#         our_list = json.load(f)
#         return our_list


def get_posts_all():
    with open(path, 'r', encoding='UTF-8') as f:
        our_list = json.load(f)
        return our_list


def get_posts_by_user(user_name):
    pass


def get_comments_by_post_id(post_id):
    pass


def search_for_posts(query):
    pass


def get_post_by_pk(pk):
    pass
