from locust import HttpUser,task,between


class QuicksUser(HttpUser):
    
    def on_start(self):
        response = self.client.post('/accounts/api/v2/jwt/create/',data={
            "email":"shahramsamar2010@gmail.com",
            "password":"Ss123456@#"
        }).json()
        self.client.headers = { 'Authentication':f"Bearer {response.get('access',None)}"}



    @task
    def posr_list(self):
        self.client.get("/api/v1/post")
       
