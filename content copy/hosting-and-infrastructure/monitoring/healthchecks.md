---
draft: false
title: Healthchecks
content:
  id: healthchecks
  name: Healthchecks
  logo: /images/hosting-and-infrastructure/monitoring/healthchecks/logo.png
  website: https://healthchecks.io/
  iframe_website: /website/hosting-and-infrastructure/monitoring/healthchecks
  dashboardImage: /images/hosting-and-infrastructure/monitoring/healthchecks/screenshot-1.jpg
  short_description: Healthchecks is an online service for monitoring regularly running tasks such as cron jobs.
  description: "Healthchecks, a cron job monitoring service, listens for HTTP requests and email messages (pings) from your cron jobs and scheduled tasks (checks). When a ping does not arrive on time, it sends out alerts. It comes with a web dashboard, API, 25+ integrations for delivering notifications, monthly email reports, WebAuthn 2FA support, and team management features: projects, team members, read-only access."
  features:
    - title: Live-updating dashboard
      description: Healthchecks provides you with a list of your checks, one for each cron job, daemon or scheduled task you want to monitor. You can give names and assign tags to your checks to easily recognize them later; tap on the integration icons to toggle them on and off, and adjust period and grace time to match the periodicity and duration of your tasks.
    - title: Reliable
      description: The hosted Healthchecks.io service runs on Hetzner bare metal servers, with healthy excess capacity to handle traffic spikes (which cron jobs with common schedules are prone to create). The app servers are load-balanced. The PostgreSQL database has a hot standby as well as daily encrypted backups to S3.
    - title: Self-hostable
      description: The Healthchecks.io code base is BSD-licensed and is developed in the open on GitHub. Self-hosting is a good option if you need to extend the project with proprietary features, must run everything in-house for compliance reasons, or want to learn about developing and deploying Django web applications.
    - title: Public status badges
      description: Healthchecks provides status badges for each of the tags you have used. Additionally, the Healthchecks.io badge shows the overall status of all checks in your account. The badges have public but hard-to-guess URLs. You can use them in your READMEs, dashboards or status pages.
  screenshots:
    - /images/hosting-and-infrastructure/monitoring/healthchecks/screenshot-1.jpg
    - /images/hosting-and-infrastructure/monitoring/healthchecks/screenshot-2.jpg
---
