# ci-cd-pipeline2
Created a repo named ci-cd-pipeline2 with Readme.md file, with private scope. 

Created an index.html file which displays Hello in the browser.
Created EC2 instance using Ubuntu AMI, t2.micro type, key-value pairs and SSH connections, named gi_cicd_pipeline.

Connected to EC2 instance and installed nginx by
sudo apt update
sudo apt-get install nginx

Installed git and created a global user to clone and pull code.
sudo apt install git
git config --global user.email ishwaripillay198@gmail.com

Cloned git repo in /var/www/ci-cd-pipeline

Deleted the default configuration within /etc/nginx/
Created configuration file named cicd and set its root to /var/www/ci-cd-pipeline and index as index.html

Started nginx -
sudo systemctl start nginx

Created commitId.txt to hold in commit Ids.

Enabled the virtual host
sudo ln -s /etc/nginx/sites-available/cicd /etc/nginx/sites-enabled/cicd

Personal Access Token to use Github api can be generated from the below steps -
Go to GitHub Account settings
Navigate to "Developer settings" -> "Personal access tokens." 
Click "Generate token" and select the repo:status scope for commit status and select expiration as 30 days.

       
Created a deploy.sh that pulls new code from the repo and restarts nginx to directly load the updated code from /var/www/ci-cd-pipeline
       
Created a commit_check.py python script that checks for commits using Github commit status api https://api.github.com/repos/MissIshwari/ci-cd-pipeline/commits
This api gives a list of commits, latest at 0 along with other important details like author, message, timestamp.
If there is a new commit, it gets added in commitId.txt and a deploy.sh shell runs.

Created a cronjob in crontab that runs every minute and executes commit_check.py.
* * * * * python3 /home/ubuntu/commit_check.py

Every new commit to index.html triggers the cronjob and the code is pulled and deployed in nginx.

The files directory in this repo contains the configuration and code.





