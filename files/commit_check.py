import requests
from datetime import datetime
import subprocess

def get_latest_commits(username, repository, token):
    #Token of user from github
    token='TOKEN'
    
    #API to get commit list
    url = f'https://api.github.com/repos/MissIshwari/ci-cd-pipeline/commits'
    headers = {'Authorization': f'token {token}'}
    
    #API call with authorization header
    response = requests.get(url, headers=headers)
    
    #If the request to API is successful, the response is stored, else an error message is shown.
    if response.status_code == 200:
        commits = response.json()
        return commits
    else:
        print(f"Error: {response.status_code}")
        return None
def check_commit(commits):
    #If latest commit is fetched without api fail.
    if commits:
        print("Latest commits:")
        #The below details are extracted for the latest commit.
        sha = commit['sha']
        author = commit['commit']['author']['name']
        message = commit['commit']['message']
        timestamp = commit['commit']['author']['date']
        formatted_time = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%SZ")
            #print(f"{sha[:7]} by {author} - {formatted_time} - {message}")

	'''The text file contains last commit id, it is compared with the current fetched,if they are not then the commit id is replaced 
        in commitId.txt and deploy.sh bash script is run to pull the code and restart nginx. '''
        with open("commitId.txt","r+") as file1:
            prev_sha = file1.readline()
            print("PREVIOUS*****"+prev_sha)
            print("NEW******"+sha)
            if(not prev_sha==sha):
                file1.seek(0)
                file1.truncate()
                file1.write(sha)
                subprocess.run(["bash","/home/ubuntu/deploy.sh"])
                print("Successful write")
            #file1.close()
    else:
        print("No commits found.")
if __name__ == "__main__":
    # GitHub username, repository name, and personal access token.
    github_username = 'MissIshwari'
    github_repository = 'ci-cd-pipeline2'
    github_token = 'TOKEN'
    
    #Passing the above credentials and repo name to get latest commits.
    latest_commits = get_latest_commits(github_username, github_repository, github_token)
    
    #Calling function to check commmit and call shell script to pull code and restart nginx.
    check_commit([latest_commits[0]])
