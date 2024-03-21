# Наталья Петрова, 14-я когорта — Финальный проект. Инженер по тестированию плюс

import data
import funcs


def test_get_order_by_track():
    response_create_user = funcs.create_order_request(data.create_order_body)
    track = funcs.get_order_track(response_create_user)
    response_get_order = funcs.get_order_by_track(track)
    assert response_get_order.status_code == 200
