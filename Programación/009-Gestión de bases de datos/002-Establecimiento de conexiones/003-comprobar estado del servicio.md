fabiana@fabiana-VirtualBox:~$ sudo service mongod status
● mongod.service - MongoDB Database Server
     Loaded: loaded (/usr/lib/systemd/system/mongod.service; enabled; preset: e>
     Active: active (running) since Mon 2026-02-02 10:13:06 CET; 3min 23s ago
       Docs: https://docs.mongodb.org/manual
   Main PID: 7945 (mongod)
     Memory: 111.9M (peak: 112.6M)
        CPU: 2.825s
     CGroup: /system.slice/mongod.service
             └─7945 /usr/bin/mongod --config /etc/mongod.conf

feb 02 10:13:06 fabiana-VirtualBox systemd[1]: Started mongod.service - MongoDB>
feb 02 10:13:06 fabiana-VirtualBox mongod[7945]: {"t":{"$date":"2026-02-02T10:1>
feb 02 10:13:06 fabiana-VirtualBox mongod[7945]: {"t":{"$date":"2026-02-02T10:1>
lines 1-13/13 (END)

