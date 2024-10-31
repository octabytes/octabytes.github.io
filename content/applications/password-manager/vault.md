---
draft: false
title: Vault
content:
  id: vault
  name: Vault
  logo: /images/applications/password-manager/vault/logo.png
  website: https://www.vaultproject.io/
  iframe_website: /website-iframe/applications/password-manager/vault
  dashboardImage: /images/applications/password-manager/vault/screenshot-1.png
  short_description: Vault is a tool for secrets management, encryption as a service, and privileged access management
  description: Vault is a tool for securely accessing secrets. A secret is anything that you want to tightly control access to, such as API keys, passwords, certificates, and more. Vault provides a unified interface to any secret, while providing tight access control and recording a detailed audit log.
  features:
    - title: Secure Secret Storage
      description: Arbitrary key/value secrets can be stored in Vault. Vault encrypts these secrets prior to writing them to persistent storage, so gaining access to the raw storage isn't enough to access your secrets.
    - title: Dynamic Secrets
      description: Vault can generate secrets on-demand for some systems, such as AWS or SQL databases
    - title: Data Encryption
      description: Vault can encrypt and decrypt data without storing it. This allows security teams to define encryption parameters and developers to store encrypted data in a location such as a SQL database without having to design their own encryption methods.
    - title: Leasing and Renewal
      description: All secrets in Vault have a lease associated with it. At the end of the lease, Vault will automatically revoke that secret. Clients are able to renew leases via built-in renew APIs.
  screenshots:
    - /images/applications/password-manager/vault/screenshot-1.png
    - /images/applications/password-manager/vault/screenshot-2.png
---