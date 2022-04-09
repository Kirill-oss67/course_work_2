# git clone https://github.com/skypro-008/coursework2_source
import json

path_data = './data/data.json'
path_comments = './data/comments.json'


def get_posts_all():
    with open(path_data, 'r', encoding='UTF-8') as f:
        our_list = json.load(f)
        return our_list


def get_posts_by_user(user_name):
    users_posts = []
    data = get_posts_all()
    for i in data:
        if i['poster_name'] == user_name:
            users_posts.append(i)
    return users_posts


def get_comments_by_post_id(pk):
    list_comments = []
    post = get_post_by_pk(pk)
    with open(path_comments, 'r', encoding='UTF-8') as f:
        all_comments = json.load(f)
    for comments in all_comments:
        if comments["post_id"] == pk:
            list_comments.append(comments)
    return list_comments


def search_for_posts(query):
    data = get_posts_all()
    searched_posts = []
    for i in data:
        if query.lower() in i['content'].lower():
            searched_posts.append(i)
    return searched_posts


def get_post_by_pk(pk):
    data = get_posts_all()
    for i in data:
        if i['pk'] == pk:
            post = i
            return post
