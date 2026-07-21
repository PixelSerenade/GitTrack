import fire 
import urllib.request
import urllib.error
import json

class github:

    def github_activity(self,username):
        
        url = f"https://api.github.com/users/{username}/events/public"

        request_headers = {'User-Agent': 'Python-Activity-Fetcher'}

        try:
            req=urllib.request.Request(url,headers=request_headers)
            #print(req)
            with urllib.request.urlopen(req) as res:
                data=json.loads(res.read().decode("utf-8"))

        except urllib.error.HTTPError as e:
            if(e.code==404):
                print(f"{username} was Not found On github")
            else:
                print(f"Github API Error {e.close} reason is {e.reason}")
            return
        
        except urllib.error.URLError as e:
            print(f"Github Error bec of reason  {e.reason}")

        if not data:
            print(f"No new Activities were found for the user {username}")
        
        for x in data:
            event_type=x["type"]
            repo_url=x["repo"]["name"]
            user_nm=x["actor"]["login"]

            if(event_type=="PushEvent"):
                print(f"{user_nm} Pushed to {repo_url}")

            elif (event_type=="CreateEvent"):
                ref_type=x["payload"]["ref_type"]
                ref_nm=x["payload"]["ref"]
                print(f"{user_nm} Created A new {ref_type} ({ref_nm}) in repo {repo_url}")

            elif(event_type=="WatchEvent"):
                print(f"{user_nm} Starred the Repo {repo_url}")

            elif(event_type=="IssuesEvent"):
                action=x["payload"]["action"]
                print(f"{user_nm} {action} an issue in repo {repo_url}")

            else:
                print(f"{user_nm} triggered an event in repo {repo_url}")


if __name__=="__main__":
    fire.Fire(github)    
        

        