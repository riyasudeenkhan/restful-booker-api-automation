import requests

BASE_URL = "https://restful-booker.herokuapp.com"

class RestfulBookerAPI:
    def __init__(self):
        self.token = None

    def authenticate(self, username="admin", password="password123"):
        response = requests.post(f"{BASE_URL}/auth", json={"username": username, "password": password})
        self.token = response.json().get("token")
        return self.token

    def create_booking(self, payload):
        response = requests.post(f"{BASE_URL}/booking", json=payload)
        return response

    def get_all_bookings(self):
        return requests.get(f"{BASE_URL}/booking")

    def get_booking_details(self, booking_id):
        return requests.get(f"{BASE_URL}/booking/{booking_id}")

    def update_booking(self, booking_id, payload):
        headers = {"Cookie": f"token={self.token}"}
        return requests.put(f"{BASE_URL}/booking/{booking_id}", json=payload, headers=headers)

    def delete_booking(self, booking_id):
        headers = {"Cookie": f"token={self.token}"}
        return requests.delete(f"{BASE_URL}/booking/{booking_id}", headers=headers)
