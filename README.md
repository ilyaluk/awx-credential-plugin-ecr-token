# awx-credential-plugin-ecr-token

This is a custom credential plugin for AWX that allows to use ECR token as a source for Container Registry credentials.

This is useful if you run AWX not on EKS, but still want to use ECR as a container registry for custom EE images.

## Installation

Create custom Dockerfile and build a new AWX image:

```dockerfile
ARG AWX_VERSION=24.6.1
FROM quay.io/ansible/awx:${AWX_VERSION}

USER root
RUN awx-python -m pip install git+https://github.com/ilyaluk/awx-credential-plugin-ecr-token.git

USER 1000
```

Or, just run the `pip install` in your AWX.

If you are adding this plugin to an existing AWX installation, run `awx-manage setup_managed_credential_types` once to update DB.

## Usage

1. Create a new credential of type `ECR Password`, specify region
2. Create a new credential of type `Container Registry`, use `AWS` as username, source password from the ECR Password credential
3. Use the `Container Registry` credential in EE
