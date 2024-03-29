# Simple Distributed Architecture POC

![architecture](architecture.png "An optional title")

## How to run project

install TILT (https://docs.tilt.dev/):

```shell
    curl -fsSL https://raw.githubusercontent.com/tilt-dev/tilt/master/scripts/install.sh | bash
```

run TILT

```commandline
tilt up
```

#TODO fix this step

create a port forward to the load balancer service

```commandline
kubectl port-forward service/load-balancer 8080
```

run the test or navigate to the browser

```commandline
pytest -rP tests/
```