# Construire l'image du serveur d'applications : api-and-worker

Construire l'image `api-and-worker`

```bash
cd docker
. ./build.sh
```

# Nginx

Le frontal devant django est configuré sur un vhost "plateform", doit exister dans le /etc/hosts sur 127.0.0.1

```
127.0.0.1    plateform
```

# Exécuter la tâche

http://plateform/api/execute_task/

