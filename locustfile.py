from locust import HttpUser, TaskSet, User, task
from flask import request


class UserBehavior(TaskSet):
    @task
    def index(self):
    #irá fazer o teste na raiz da aplicação
        self.client.get("localhost3000tutors")



    @task
    def new_todo(self):
        self.client.post('localhost3000tutors' , {
                          'username''developer@example.com',
                          'password''example'   
})


class WebsiteUser(HttpUser):
    get_tasks = UserBehavior
    #Tempo minino e maximo que o locust irá aguardar entre as tasks
    min_wait = 2000
    max_wait = 5000
    host = ("httplocalhost3000tutors")        