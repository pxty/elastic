Плейбук для установки ELK.
 Kibana + logstash устанавливаются на локальную машину vm-log
 nginx + filebeat устанавливаются на вторую локальную машину vm-app
Обе локальные машины находятся в приватной сети. Доступ через NAT. ansible устанавливается на машине с NAT.

Реализованы ansible роли: nginx и elatic 

Запуск: ansible-playbook eto.yml
Перед запуском проверить hosts.ini

