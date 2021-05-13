# FrontendApplication
### Frontend Application for Mountkirk Games Repository
<br><br>
1. This application will be used as a frontend for Mountkirk Games Repository.<br>
2. Create a vm with following configuration:
  a. n1-standard-1<br>
  b. ubuntu-20.04 LTS<br>
  c. 10 gb persistent disk<br>
  d. Custom VPC<br>
  e. Others as default<br>
 3. SSH into VM.<br>
 5. Download following softwares <br>
    sudo -s<br>
    cd /<br>
    sudo apt update && sudo apt upgrade -y<br>
    apt install git -y<br>
    apt install python3 python3-pip -y<br>
    apt install mysql-client
    apt install vim -y<br>
    pip3 install Flask<br>
    pip3 install google-cloud-logging<br>
    pip3 install PyMySQL</p><br>
 6. git clone https://github.com/shalligoel/FrontendApplication<br>
 7. cd FrontendApplication/frontend<br>
 8. Get IP Addres of Cloud-SQL Instance and save in dblocal.py. Update username, password and Database name if needed.
 9. Get IP Address of VM where your MountkirkGames is running and save in game.html.
 10. Create a user in cloud-sql instance as mkuser and password - root123.
 11. Create a database and tables in cloudSQL Instance
     mysql -h <cloudsql ip address> -umkuser -proot123 < profile.sql
     mysql -h <cloudsql ip address> -umkuser -proot123
     show databases;
     use MKGames;
     show tables;
     exit
 12. Run your application:<br>
     python3 app.py 
 
