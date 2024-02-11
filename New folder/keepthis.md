ubuntu@45817-lb-01:/etc/haproxy$ cd ~
ubuntu@45817-lb-01:~$ sudo systemctl stop nginx
ubuntu@45817-lb-01:~$ sudo service haproxy stop
ubuntu@45817-lb-01:~$ sudo certbot certonly --standalone -d www.iconnects.tech
Saving debug log to /var/log/letsencrypt/letsencrypt.log
Plugins selected: Authenticator standalone, Installer None
Obtaining a new certificate
Performing the following challenges:
http-01 challenge for www.iconnects.tech
Waiting for verification...
Cleaning up challenges

IMPORTANT NOTES:
 - Congratulations! Your certificate and chain have been saved at:
   /etc/letsencrypt/live/www.iconnects.tech/fullchain.pem
   Your key file has been saved at:
   /etc/letsencrypt/live/www.iconnects.tech/privkey.pem
   Your cert will expire on 2024-05-11. To obtain a new or tweaked
   version of this certificate in the future, simply run certbot
   again. To non-interactively renew *all* of your certificates, run
   "certbot renew"
 - If you like Certbot, please consider supporting our work by:

   Donating to ISRG / Let's Encrypt:   https://letsencrypt.org/donate
   Donating to EFF:                    https://eff.org/donate-le

ubuntu@45817-lb-01:~$

