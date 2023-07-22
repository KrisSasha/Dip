# Кристина Денисовна, 6-я когорта — Финальный проект. Инженер по тестированию плюс
import stand_requests
import data


def test_suit():
    track_number = stand_requests.post_create_order(
        data.headers, data.order_body)
    status_code = stand_requests.get_get_order(track_number)
    assert 200 == status_code, "Код возврата не равен 200"


test_suit()
