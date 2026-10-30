from locust import HttpUser, between, task


class WebsiteUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def index(self):
        # новое соединение на каждый запрос, чтобы kube-proxy раздавал трафик и на новые реплики
        self.client.get("/", headers={"Connection": "close"})
