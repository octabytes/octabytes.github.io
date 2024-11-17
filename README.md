# OctaByte

## Start

First install npm packages

- `npm install`

Second run hugo server for dev

- `hugo server`

For build run just `hugo`

## Nginx

### Stop nginx

`sudo systemctl stop nginx`

### Create Backup

1. `cd /etc/nginx/`
2. `sudo cp -r conf.d conf.bak`

### Copy new conf

`cp -r extractor/nginx/* /etc/nginx/conf.d/`

### Test nginx

`sudo nginx -t`

### Start nginx

`sudo systemctl start nginx`

### Reload nginx

`sudo systemctl reload nginx`
