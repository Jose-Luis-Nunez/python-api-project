import random
import string
import logging
import json


class Helper:
    @staticmethod
    def generate_random_email(domain="automation.com", length=10):
        random_string = ''.join(random.choice(string.ascii_lowercase) for _ in range(length))
        return f"{random_string}@{domain}"

    @staticmethod
    def extract_user_id(response):
        try:
            json_data = response.json()
            return json_data.get("id")
        except ValueError:
            logging.error("Fehler beim Parsen der JSON-Antwort.")
            return None

    @staticmethod
    def print_json_response(response):
        try:
            json_str = json.dumps(response.json(), indent=4)
            logging.info(f"JSON Response:\n{json_str}")
        except ValueError:
            logging.warning("Response contains no JSON data.")
