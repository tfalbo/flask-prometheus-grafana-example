$ docker run -p 9090:9090 -v /home/thaissafalbo/Meetups/pyladiesrio/prometheus/prometheus.yml:/etc/prometheus/prometheus.yml prom/prometheus
$ docker network connect --alias prometheus my-bridge-network prometheus
$ docker network connect --alias app my-bridge-network app