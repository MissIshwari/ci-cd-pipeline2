#!/bin/bash
cd /var/www/ci-cd-pipeline/
sudo git pull
echo "Pulled code."
sudo service nginx restart
