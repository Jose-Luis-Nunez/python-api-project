from enum import Enum, auto

import requests
import logging

from helper import Helper

base_url = "https://gorest.co.in"
auth_token = "Bearer 14647657e352a1a1857ea880578eba094e7ff99fce72d4167234576f7116c728"
logging.basicConfig(level=logging.INFO)


class HttpMethod(Enum):
    GET = "get"
    POST = "post"
    PUT = "put"
    DELETE = "delete"


def send_request(method: HttpMethod, endpoint: str, data=None):
    url = f"{base_url}{endpoint}"
    headers = {"Authorization": auth_token}
    try:
        response = requests.request(method.value, url, json=data, headers=headers)
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        logging.error(f"An error occurred: {e}")
        raise


def get_request():
    logging.info("Fetching users...")
    response = send_request(HttpMethod.GET, "/public/v2/users/")
    Helper.print_json_response(response)


def post_request():
    body = {
        "name": "random name",
        "email": Helper.generate_random_email(),
        "gender": "male",
        "status": "active"
    }
    response = send_request(HttpMethod.POST, "/public/v2/users/", body)
    Helper.print_json_response(response)
    return response


def put_request(user_id):
    body = {
        "name": "updated name",
        "email": Helper.generate_random_email(),
        "gender": "female",
        "status": "inactive"
    }
    response = send_request(HttpMethod.PUT, f"/public/v2/users/{user_id}", body)
    Helper.print_json_response(response)


def delete_request(user_id):
    send_request(HttpMethod.DELETE, f"/public/v2/users/{user_id}")
    logging.info(f"User {user_id} deleted.")


# Aufrufe
get_request()
user_id = Helper.extract_user_id(post_request())
put_request(user_id)
delete_request(user_id)
