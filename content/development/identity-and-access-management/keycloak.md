---
draft: false
title: Keycloak
content:
  id: keycloak
  name: Keycloak
  logo: /images/development/identity-and-access-management/keycloak/logo.png
  website: https://www.keycloak.org/
  iframe_website: /website-iframe/development/identity-and-access-management/keycloak
  dashboardImage: /images/development/identity-and-access-management/keycloak/screenshot-1.jpg
  short_description: Keycloak is an open-source identity and access management solution aimed at modern applications and services.
  description: Keycloak allows single sign-on with identity and access management. You can add authentication to applications and secure services with minimum fuss. There's no need to deal with storing or authenticating users. It's all available out of the box. You also get advanced features such as user federation, identity brokering and social login.
  features:
    - title: Single sign-on/out
      description: Users authenticate with Keycloak rather than individual applications. This means that your applications don't have to deal with login forms, authenticating users, and storing users. Once logged in to Keycloak, users don't have to log in again to access a different application. This also applies to logging out. The single sign-out means users only have to log out once to be logged out of all applications that use Keycloak.
    - title: Identity brokering and social login
      description: With Keycloak, enabling login with social networks is easy to add through the admin console – just select the social network you want to add. No code or changes to your application are required. Keycloak can also authenticate users with OpenID Connect or SAML 2.0 identity providers. Again, this is just a matter of configuring the identity provider through the admin console.
    - title: User federation
      description: Keycloak has built-in support to connect to LDAP or Active Directory servers. You can also implement your own provider if you have users in other stores, such as a relational database.
    - title: Admin console
      description: "Through the admin console administrators can centrally manage all aspects of the Keycloak server: enable and disable various features; configure identity brokering and user federation; create and manage applications and services; define fine-grained authorization policies, and manage users, including permissions and sessions."
  screenshots:
    - /images/development/identity-and-access-management/keycloak/screenshot-1.jpg
    - /images/development/identity-and-access-management/keycloak/screenshot-2.jpg
---