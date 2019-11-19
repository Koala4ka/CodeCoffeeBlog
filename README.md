# CodeCoffeeBlog

### Front-end guide ###

1. HTML go to `templates/`
1. Static assets go to `static/`

### Backend dev setup guide ### 

1. Clone the repo
1. Make sure you have `flask`, `mysql` and `pymysql` installed 
1. `CREATE DATABASE coffeeproject;`
1. `cp sample-config.py config.py` in your repo root folder and fill in your credentials. `config.py` is git-ignored
1. `python3 main.py` (or `python main.py` when using `venv`)
1. Enjoy :)

### Deployment guide ###

1. Ask Dan to add your `.pub` ssh key to the server and setup your `~/.ssh/config` with the ip address you get back from Dan
1. In your repo root folder: `git remote add live vultr:coffeeproject-git-repo`
1. `git push -f live master` to deploy. While `-f` can be skipped in most cases, sometimes it's needed

## Let's have fun, _coffee_ and some __IT__
