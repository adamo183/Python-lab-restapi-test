import time
from locust import HttpUser, task, between

class TestApi(HttpUser):
    wait_time = between(0.5, 1)

    @task
    def test_prime(self):
        self.client.get(f"/prime/2")

    @task
    def test_image_sender(self):
        with open('wc22.jpg', 'rb') as image:
            self.client.post(
                "/photo/",
                files={'file': image}
            )

    @task
    def test_date_with_token(self):
        self.client.get(f"/date/currentTime",headers={
                "Accept": "Application/Json",
                "Authorization":f"Bearer {self.token}"})

    def on_start(self):
        response = self.client.post("/auth/login", data={
            "login": "user",
            "password": "password"})
        self.token = response.json()['access_token']
