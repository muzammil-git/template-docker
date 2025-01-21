# Docker Commands for Test-KBS

This README provides a set of essential Docker commands used to build, run, and manage the `test-kbs` Docker container.

## Build the Docker Image

Before running the container, you need to build the Docker image from the `Dockerfile`. Use the following commands:

```bash
# Build the Docker image
docker build -t test-kbs .

# Build without cache (forces a fresh build)
docker build --no-cache -t test-kbs .
```

The second command is useful when you want to ensure the build is clean and unaffected by any cached layers.

## Run the Docker Container

Once the Docker image is built, you can run the container:

```bash
# Run the container and map port 8000
docker run -p 8000:8000 test-kbs
```

This command starts the container and maps port 8000 in the container to port 8000 on your local machine, allowing you to access the application via http://localhost:8000.

## Manage Docker Containers

Here are the essential commands for managing your Docker containers:

```bash
# List all containers (including stopped ones)
docker ps -a

# Stop a running container
docker stop <container_id_or_name>

# Remove a stopped container
docker rm <container_id_or_name>

# Stop and remove a container in a single command (force removal)
docker rm -f <container_id_or_name>
```

Replace `<container_id_or_name>` with the actual container ID or name (e.g., abc123def456).

## Clean Up Docker Builder Cache

To remove unused build cache and free up disk space:

```bash
# Prune Docker builder cache
docker builder prune
```

This command removes any build cache that is no longer needed. It's useful when you want to clean up and optimize your Docker environment.

## Quick Reference

| Command | Description |
|---------|------------|
| `docker build -t test-kbs .` | Build the Docker image |
| `docker build --no-cache -t test-kbs .` | Build without cache |
| `docker run -p 8000:8000 test-kbs` | Run container with port mapping |
| `docker ps -a` | List all containers |
| `docker stop <container_id_or_name>` | Stop a container |
| `docker rm <container_id_or_name>` | Remove a stopped container |
| `docker rm -f <container_id_or_name>` | Force stop and remove |
| `docker builder prune` | Clean up builder cache |
