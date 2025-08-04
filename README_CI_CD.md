# CI/CD Pipeline Setup

This project uses GitHub Actions for continuous deployment to EC2 using Docker containers.

## Overview

The CI/CD pipeline automatically:
1. Builds a Docker image when code is pushed to the `main` branch
2. Pushes the image to Docker Hub
3. Deploys the application to your EC2 instance
4. Runs the application in a Docker container

## Required GitHub Secrets

You need to set up the following secrets in your GitHub repository:

### Docker Hub Credentials
- `DOCKER_USERNAME`: Your Docker Hub username
- `DOCKER_PASSWORD`: Your Docker Hub password or access token

### EC2 Connection Details
- `EC2_HOST`: Your EC2 instance's public IP address or domain name
- `EC2_USERNAME`: SSH username (usually `ubuntu` for Ubuntu instances)
- `EC2_PRIVATE_KEY`: Your EC2 private key content (the entire private key file content)
- `EC2_PORT`: SSH port (usually `22`)

## Setting Up GitHub Secrets

1. Go to your GitHub repository
2. Click on **Settings** → **Secrets and variables** → **Actions**
3. Click **New repository secret** for each required secret

### Getting Your EC2 Private Key

If you don't have the private key:
1. Go to AWS Console → EC2 → Key Pairs
2. Create a new key pair or use existing one
3. Download the `.pem` file
4. Copy the entire content of the `.pem` file as the `EC2_PRIVATE_KEY` secret

## EC2 Instance Setup

### Security Group Configuration
Ensure your EC2 security group allows:
- **SSH (Port 22)**: For deployment
- **HTTP (Port 80)**: If using a load balancer
- **Custom TCP (Port 5000)**: For direct access to Flask app

### Initial EC2 Setup
The deployment script will automatically install Docker and Docker Compose on your EC2 instance.

## Deployment Process

1. **Trigger**: Push to `main` branch or manual trigger
2. **Build**: Creates Docker image with your code
3. **Push**: Uploads image to Docker Hub
4. **Deploy**: 
   - Connects to EC2 via SSH
   - Installs Docker (if not present)
   - Pulls latest image
   - Stops old container
   - Starts new container
   - Cleans up old images

## Manual Deployment

You can trigger deployment manually:
1. Go to **Actions** tab in GitHub
2. Select **Deploy to EC2** workflow
3. Click **Run workflow**

## Monitoring

- **Application**: Access at `http://your-ec2-ip:5000`
- **Container Status**: SSH to EC2 and run `docker ps`
- **Logs**: `docker logs ajfm-app`

## Troubleshooting

### Common Issues

1. **SSH Connection Failed**
   - Verify EC2_HOST and EC2_PRIVATE_KEY
   - Check security group allows SSH
   - Ensure key pair is correct

2. **Docker Build Failed**
   - Check Docker Hub credentials
   - Verify Dockerfile syntax

3. **Application Not Accessible**
   - Check security group allows port 5000
   - Verify container is running: `docker ps`
   - Check logs: `docker logs ajfm-app`

### Useful Commands

```bash
# SSH to EC2
ssh -i your-key.pem ubuntu@your-ec2-ip

# Check container status
docker ps

# View logs
docker logs ajfm-app

# Restart container
docker-compose restart

# Update and redeploy
docker-compose pull && docker-compose up -d
```

## Security Notes

- The Dockerfile runs the application as a non-root user
- Private keys are stored securely in GitHub Secrets
- The deployment uses HTTPS for all communications
- Old Docker images are automatically cleaned up

## Customization

### Environment Variables
Add environment variables to the `docker-compose.yml` in the deployment script:

```yaml
environment:
  - FLASK_ENV=production
  - YOUR_CUSTOM_VAR=value
```

### Port Configuration
Change the port mapping in `docker-compose.yml` if needed:

```yaml
ports:
  - "80:5000"  # Map host port 80 to container port 5000
```

### Health Check
The Dockerfile includes a health check. Modify the endpoint in the Dockerfile if your app has a different health endpoint. 