workers = 2
syslog = True
bind = ['127.0.0.1:{{gunicorn_port}}'] #52.172.183.85 wont work here #0.0.0.0 is dangerous..and why it is djangerous, I have explained in my notes files
umask = 0
loglevel = 'info'
user = 'yashazure'
group = 'yashazure'

accesslog = '{{projdir}}/../access.log' #An access log is a list of all requests for individual files that people or bots have requested from a website.
errorlog = '{{projdir}}/../error.log'
