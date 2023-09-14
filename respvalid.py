import requests
import pyfiglet

xdxd = pyfiglet.figlet_format("basic resp validator " )
print(xdxd) 
ydyd = ("Coded w/ <3 By - @p474nj4y")
print(ydyd)

def give_requests(url):
    try:
        response = requests.get(url)
        if response.status_code == 200 :
            print("jainwinn response 200 OK :) ")
            print("response pkdo sir : ")
            print(response.text)
    
        else:
            print(f"request fail hogis n apka status code :{response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"invalid hai bhyii : {e}")

if __name__ == "__main__" :
    target_url=input("sir url daalo : ")
    give_requests(target_url)