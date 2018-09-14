# GOMOKUBOT

```python
Team  = 'Pyaneers'
Members = ['Andrew Baik', 'Jason Burns', 'Christopher Chapman', 'Alexander Stone']
```

---

### About
Gomokubot learns the game of [gomoku](https://en.wikipedia.org/wiki/Gomoku) using 
Google [tensorflow](https://www.tensorflow.org/).

##### Play Mechanics
win:
	five in a row

first move:
	black

mechanics:
	forcing moves: plays which line up four in a row, which force defensive moves by the other side, often for an extended time. Skilled players can read chains of these out to 40 moves. response: end forcing mechanics by playing interupting moves towards clusters of your own pieces that are already on the board, increading the chance for offensive opportunities.

---

Getting Started
---------------

- Change directory into your newly created project.

    cd Gomokubot

- Create a Python virtual environment.

    python3 -m venv env

- Upgrade packaging tools.

    env/bin/pip install --upgrade pip setuptools

- Install the project in editable mode with its testing requirements.

    env/bin/pip install -e ".[testing]"

- Run your project's tests.

    env/bin/pytest

- Run your project.

    env/bin/pserve development.ini

---

### Setting up an AWS Instance of Gomokubot:

1. Create a new EC2 Instance

2. Set up an ssh configuration for the EC2 instance and connect to it. Note the rest of these instructions will be for an Ubuntu Server 16.x instance.

3. Update your EC2 Instance and install nginx, build-essential, python-dev and python3-pip.

4. Clone the repo into the src directory.

5. Navigate to the repo. Switch to either the development_aws branch(for a 15x15 board) or the s_aws_deploy branch(for a 5x5 board).

6. run pip3 install -e . --user
to install all the neccessary files. In addition run 
pip3 install pytest.

7. go to src/Gomokubot/models/gmk_board.py and find the update in the DBBoard class. Change config_uri from 'development.ini' to 'production.ini'.

8. go to src/Gomokubot/views/board.py and change the first line in the try block of the update method of the BoardAPIView class from kwargs = json.loads(request.body) to kwargs = json.loads(request.body.decodes())

9. Make an Amazon RDS Postgres database and ensure that your ec2 instance can connect to it.

10. Go to src/production.ini and add the line sqlalchemy.url = postgres://DB_USER:PASSWORD@DB_ENDPOINT:5432/DB_NAME under the [app:main] section.

11. run initialize_gomokubot_db production.ini in src.

12. in ~ run mkdir logs; touch error.log access.log

13. Run sudo nano /etc/nginx/nginx.conf and delete the contents of that file and replace them with:

    # nginx.conf
    user wwwd
    
14. run sudo nano /etc/nginx/conf.d/gomokubot.conf to create a project specific conf file for your nginx server. Paste the following into it:
    
    # gomokubot.conf
    upstream gomokubot {
        server 127.0.0.1:8000;
    }

    server {
        listen 80;

        server_name (EC2 public DNS);

        access_log  /home/ubuntu/.local/nginx.access.log;

        location / {
            proxy_set_header        Host $http_host;
            proxy_set_header        X-Real-IP $remote_addr;
            proxy_set_header        X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header        X-Forwarded-Proto $scheme;

            client_max_body_size    10m;
            client_body_buffer_size 128k;
            proxy_connect_timeout   60s;
            proxy_send_timeout      90s;
            proxy_read_timeout      90s;
            proxy_buffering         off;
            proxy_temp_file_write_size 64k;
            proxy_pass http://gomokubot;
            proxy_redirect          off;
        }
    }

15. Validate your settings with sudo nginx -t and look for the message that says the conf test is successful.

16. check that nginx is working with sudo service nginx status
If it is not working run sudo service nginx restart

17. install gunicorn with pip3 install gunicorn --user

18. run sudo nano /etc/systemd/sytem/gunicorn.service to make a gunicorn config file. Put the following into it:

    # gunicorn.service
    [Unit]
    Description=(your description)
    After=network.target

    [Service]
    User=ubuntu
    Group=www-data
    WorkingDirectory=/home/ubuntu/src
    ExecStart=/home/ubuntu/.local/bin/gunicorn --access-logfile /home/ubuntu/logs/access.log --error-logfile /home/ubuntu/logs/error.log -w 3 --log-level warning --paste production.ini


    [Install]
    WantedBy=multi-user.target
    
19. Run the following three commands:
sudo systemctl enable gunicorn
sudo systemctl start gunicorn
sudo systemctl status gunicorn

### Development

- As a player, I like to be able to play against a computer
- As a player, I like to see computer learning
- As a player, I like to display the board on the web application while I play against computer
- As a developer, I like to access to play against computer
- As a developer, I like to transfer server data using json format
- As a developer, I like to store results to the database so that computer can learn from previous games

##### Workflow

Fractalkine workflow;  major level: squad, minor level: pairs, patch level: single.
Conflict will be handled in the thunderdome, AKA the whiteboard.

##### Branching:

Deployment: final product<br>
:arrow_up:<br>
Master: successful development commits<br>
:arrow_up:<br>
Developlemt: feature integration, code merging, and testing<br>
:arrow_up::arrow_up::arrow_up:<br>
f_feature_specific_branches: feature development<br>


ini concept:
![wireframe](https://github.com/GoTeam5/Gomokubot/blob/master/assets/GOMOKU.jpg) <br>

training flow:
![tf1](https://github.com/GoTeam5/Gomokubot/blob/master/assets/training_flow.jpg) <br>
![tf2](https://github.com/GoTeam5/Gomokubot/blob/master/assets/reboard.jpg) <br>

06SEP18:
Design

Game logic (Controller)
- validation of the victory
- Validation move

RESTful endpoints (Server/APIView)
- Post (new game)
- Put (send new point)
- Get (front-end for user)

ML(tensorflow, itertools)

Front-end
- Bare minimum of yellow background with black outlines, black and white rocks. text block
