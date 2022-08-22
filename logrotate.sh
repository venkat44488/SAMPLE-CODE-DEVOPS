prev_day=`date -d '-1 day' +"_%Y%m%d"`
prev_date=`date -d '-1 day' +"%d_%m_%Y"`
#current_date=`date +"%d_%m_%Y"`

#ls -lrt | grep "${prev_day}" | awk '{print $9}' | xargs tar -czvf /mnt/net/net_backups/${prev_date}_net.tar.gz

ls -lrt | grep "${prev_day}" | awk '{print $9}' > /mnt/net/all_file_name.txt

ls -lrt | grep "${prev_day}" | awk '{print $9}' | xargs zip /mnt/net/net_backups/${prev_date}_net.zip

#cp /mnt/net/net_backups/${prev_date}_net.tar.gz /mnt/nas-archive/

cp /mnt/net/net_backups/${prev_date}_net.zip /mnt/nas-archive/
rm /mnt/net/net_backups/${prev_date}_net.zip

find /mnt/net/ -maxdepth 1 -daystart -mtime +3 -type f -name '*.gz' -exec rm -rf {} \;
