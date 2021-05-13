# FrontendApplication
Frontend Application for Mountkirk Games Repository
<br><br>

1. This application will be used as a frontend for Mountkirk Games Repository.<br>
2. Create a vm with following configuration:
  a. f1-micro
  b. debian-9
  c. 10 gb persistent disk
  d. Custom VPC
  e. Others as default
 <br>
 3. SSH into VM.<br>
 5. Download following softwares <br>
   <p> sudo -s
    mkdir /frontend
    cd /frontend
    apt update
    apt install git
    apt install python3 python3-pip -y
    pip3 install Flask
    pip3 install google-cloud-logging
    pip3 install PyMySQL</p>
 6. git clone https://github.com/shalligoel/FrontendApplication<br>
 7. cd frontend<br>
 8. Get IP Addres of Cloud-SQL Instance and save in config.py file<br>
 9. Get IP Address of VM where your MountkirkGames is running and save in config.py.<br>
 10. Run your application:<br>
     python3 app.py 
 
