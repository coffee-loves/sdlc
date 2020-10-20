from locust import HttpUser, TaskSet, task,between
from locust.contrib.fasthttp import FastHttpLocust
import  os
import psutil
import  urllib3,requests #取消报警


class UserBehavior(TaskSet):#任务集  用户行为脚本

    def on_start(self):#初始化数据，每个虚拟用户只执行一次
        pass
    def on_stop(self):
        pass

    @task(1) #接口权重
    def queryallorg(self):
        self.payload = {'data': ''}
        self.header = {
            "Content-Type": "x-www-form-urlencoded",
            'Authorization': 'Basic YWRtaW46YWRtaW4xMjMhQCM='
        }
        requests.packages.urllib3.disable_warnings()
        self.client.post("/api/org/queryallorg/", data=self.payload, headers=self.header,verify=False)

    @task(10)
    def view_thread(self):
        pass
class WebsiteUser(HttpUser):#用户类
    tasks = {UserBehavior: 2}
    wait_time = between(0, 0)
    host ="https://10.44.155.188"

if __name__ == "__main__":
#     #os.system('locust -f load_test.py --headless   -u 10 -r 1 -t 20s --csv=example') #非UI模式运行才可设置时间
#     #os.system('locust -f load_test.py    -u 10 -r 1 ') #UI模式运行
      os.system('locust -f load_test.py --master') #单机主从分布式运行，master不执行发送请求，由slave发送请求
      #os.system('locust -f load_test.py --worker  --master-host=127.0.0.1') #一个进程，占据一个core，另外开启cmd启动slave

print(psutil.cpu_count()) #获取核数
print(psutil.cpu_percent()) #获取cpu使用率
