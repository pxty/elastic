Плейбук для установки ELK.

 Kibana + logstash устанавливаются на локальную машину vm-log.
 
 Nginx + filebeat устанавливаются на вторую локальную машину vm-app.
 
Обе локальные машины находятся в приватной сети. Доступ через NAT. ansible устанавливается на машине с NAT.

Реализованы ansible роли: nginx и elatic 

Запуск: ansible-playbook eto.yml
Перед запуском проверить hosts.ini

Проброс портов через NAT:

1) NGINX ssh -L 8000:vm-app-host:80 user@nat-instance-host

2) ELK ssh -L 55601:vm-log-host:5601 user@nat-instance-host
