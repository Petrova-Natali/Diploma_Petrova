import requests
import configuration


def create_order_request(data):
    url = configuration.URL_SERVICE + configuration.CREATE_ORDER
    return requests.post(url=url, json=data)


def get_order_track(response):
    track_dict = response.json()
    track = track_dict["track"]
    return str(track)


def get_order_by_track(track):
    url = configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK + track
    return requests.get(url=url)
