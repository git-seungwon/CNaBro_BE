import requests

class req_backend():
    def __init__(self):
        self.URL = "http://3.36.76.129:8000/tasks"

    def get_json(self):
        '''백엔드에 입력된 정보를 모두 가져옵니다.'''

        res = requests.get(url=self.URL)
        print(f"status_code :  {res.status_code}")
        print("데이터 목록 :")
        if res.status_code == 200:
            for i in res.json():
                print(i)
        
    
    def post_json(self, contentMain, tag, score):
        '''백엔드에 값을 입력합니다.'''
        
        data = {
        "contentMain": contentMain,
        "tag": tag,
        "score": score
        }

        res = requests.post(url=self.URL, json=data)
        print(f"status_code :  {res.status_code}")
        print(f"입력된 데이터 : {res.json()}")

if __name__ == "__main__":
    client = req_backend()
    client.post_json("제목", "태그", "10")
    client.get_json()
    