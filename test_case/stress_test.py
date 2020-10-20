from locust import HttpUser, TaskSet,task, between
import os,json

# 定义用户行为
class UserTask(TaskSet):
#    weight=3


    def on_start(self):
        '''初始化数据，每个虚拟用户只执行一次'''
        payload = {
            "username": "superadmin",
            "password": "ct123!@#",
        }
        header = {
            "Content-Type":"multipart/form-data",
            "Cookie":"JSESSIONID2=2DDB204C833BF7FAF447F5C79DDDC79E; OSS-TOKEN=''"
        }
        response=self.client.post("/api/login", data=payload, headers=header)

        # response=self.client.post("/api/login",{"username":"superadmin","password":"ct123!@#"})
        print("on_start Response status code:", response.status_code)
        print("Response content:", response.text)


    # @task(2)
    # def repo_search(self):
    #     response=self.client.get("/api/repo/page?page=1&size=10&language=&repoName=test&label=&description=&startTime=&endTime=&protocals=&homePage=&repoType=&organ=")
    #     print("repo_search Response status code:", response.status_code)
    #     print("Response content:", response.text)
    #
    # @task(2)
    # def binary_search(self):
    #     response=self.client.get("/api/binary/list?page=0&size=10&fileName=item&deviceClass=&sort=&ifFirmware=&description=&website=&vendor=&startTime=&endTime=")
    #     print("binary_search Response status code:", response.status_code)
    #     print("Response content:", response.text)
    #
    @task(1)
    def count_repo(self):
        pydata={
            "page":0,
            "size":10
        }
        response=self.client.get("/api/repo/countByLanguage/page",params=pydata)
        print("count_repo status code:", response.status_code)
        print("Response content:", response.text)


class WebsiteUser(HttpUser):
    host = 'http://10.249.171.254:7443'
    task_set = UserTask
    wait_time = between(3, 5)

if __name__ == "__main__":
    os.system('locust -f stress_test.py --headless -u 1 -r 1 --run-time 2s')


