server {
		    listen 88;
		    server_name 52.172.183.85;
		    
		    location /static/ {
		        alias {{projdir}}/static/;
		    }
		    
		    location /media/ {
                alias {{projdir}}/../media/;
            }

		    location / {
		        proxy_pass http://127.0.0.1:{{gunicorn_port}};
		    }
		} 