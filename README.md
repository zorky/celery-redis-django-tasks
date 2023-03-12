# Construire l'image du serveur d'applications : api-and-worker

Pré-requis : docker !

Construire l'image `api-and-worker`

```bash
$ cd docker
$ . ./build.sh
```

# Nginx

Le frontal devant django est configuré sur un vhost "plateform", doit exister dans le /etc/hosts sur 127.0.0.1

```
127.0.0.1    plateform
```

# Lancer le serveur d'applications et le worker

```bash
$ cd docker && docker-compose up
```

# Exécuter la tâche

par le navigateur http://plateform/api/execute_task/

ou

par curl `$ curl http://plateform/api/execute_task/`

