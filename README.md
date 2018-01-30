# LaunchCode LC-101 Blogz Project
Teaching Fellow help for students working on LC-101 Unit 2 final assigment Blogz

# Goal
- modularize the application by splitting the MVC pieces into separate modules
- [more information](https://www.digitalocean.com/community/tutorials/how-to-structure-large-flask-applications)

# How to use
### Clone the repo
- `git clone https://github.com/the-vampiire/blogz`

### Create and activate the virtual environment using the `env.yml` file
- `conda env create -n blogz -f env.yml`
- `source activate blogz`
- [more information](https://conda.io/docs/commands.html#conda-environment-commands)

### Startup the MySQL sever
- use MAMP or if you have `mysql` installed use `mysqld`
- make sure you have a login and password
- create a database called `blogz`

### Create the `config.py` file
- create the file **outside** of the `app/` directory
- add the following variables
- the port will typically default to `3306` or `8889` depending on the database server you use
```
DB_URI = 'mysql+pymysql://USERNAME:PASSWORD@localhost:PORT/blogz'

SESSION_SECRET = 'SECRET GOES HERE'
```

### Start the server
- start using `python run.py`

<hr>

## Original Project Requirements
- Log in (or register for a new account). The main page should display a list of users. Clicking on a user should redirect to a page displaying all blog posts written by them.
- Navigate to the page displaying all posts by all users. The author should be displayed below each post, and clicking on their name should redirect you to that user’s blog page.
- Click “New Post”, create a new post, and check that you are redirected to a page with just that individual entry. The username of the author should be shown at the bottom.
- Clicking on that username should redirect to that user’s blog page. 
- Navigate to the page displaying all posts. The new post should be on that page with the username listed underneath.
- Log out. Click all posts and make sure you can still see this page. Click new post, and you should be redirected to the login page.