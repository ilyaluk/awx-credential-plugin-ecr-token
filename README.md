# awx-credential-plugin-ecr-token

This is a custom credential plugin for AWX that allows to use ECR token as a source for Container Registry credentials.

## Installation

Create custom Dockerfile and build a new AWX image:

```dockerfile
ARG AWX_VERSION=24.6.1
FROM quay.io/ansible/awx:${AWX_VERSION}

USER root
RUN awx-python -m pip install git+https://github.com/ilyaluk/awx-credential-plugin-ecr-token.git

USER 1000
```

Override in AWX operator in `image`, `image_version` parameters.

Then run in init_script or manually in a pod: `awx-manage setup_managed_credential_types`

## Usage

1. Create a new credential of type `ECR Token`, specify region
2. Create a new credential of type `Container Registry`, use `AWS` as username, source password from the ECR Token credential
3. Use the `Container Registry` credential in EE
