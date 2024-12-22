---
draft: false
title: Loki fully managed open source service | OctaByte.io

meta:
  cover: /images/hosting-and-infrastructure/monitoring/dockerregistry/screenshot-1.jpg
  description: description
  keywords: keywords
  breadcrumb:
    - name: Home
      url: /
    - name: Fully managed Open-Source Services
      url: /fully-managed-open-source-services
    - name: Hosting and Infrastructure
      url: /fully-managed-open-source-services/hosting-and-infrastructure
    - name: Monitoring
      url: /fully-managed-open-source-services/hosting-and-infrastructure/monitoring
    - name: DockerRegistry
      url: /fully-managed-open-source-services/hosting-and-infrastructure/monitoring/dockerregistry

content:
  id: loki
  name: Loki
  logo: /images/hosting-and-infrastructure/monitoring/loki/logo.png
  website: https://grafana.com/oss/loki/
  iframe_website: /website/hosting-and-infrastructure/monitoring/loki
  direct_link: true
  description: "description"
  features:
    - title: feature
      description: "description"
    - title: feature
      description: "description"
    - title: feature
      description: "description"
    - title: feature
      description: "description"
    - title: feature
      description: "description"
    - title: feature
      description: "description"
  screenshots:
    - /images/hosting-and-infrastructure/monitoring/loki/screenshot-1.png
    - /images/hosting-and-infrastructure/monitoring/loki/screenshot-2.png
---

Write seo optimizaed content for "Loki" write a title, long description, short description, keywords and 6 features(with title and medium description) below is some content for your knowledge.

```yml
description: Loki is a horizontally scalable, highly available, multi-tenant log aggregation system inspired by Prometheus. It is designed to be very cost-effective and easy to operate. It does not index the contents of the logs, but rather a set of labels for each log stream.
  features:
    - title: Pull in any logs with Promtail
      description: Promtail is a log collector built specifically for Loki. It uses the same service discovery as Prometheus and includes analogous features for labeling, transforming, and filtering logs before ingestion into Loki.
    - title: Store the logs in Loki
      description: Loki does not index the text of logs. Instead, entries are grouped into streams and indexed with labels. Not only does this reduce costs, but it also means log lines are available to query within milliseconds of being received by Loki.
    - title: Use LogQL to explore
      description: Use Loki’s powerful query language, LogQL, to explore your logs. Run LogQL queries directly within Grafana to visualize your logs alongside other data sources, or with LogCLI, for those who prefer a command-line experience.
    - title: Alert on your logs
      description: Set up alerting rules for Loki to evaluate your incoming log data. Configure Loki to send the resulting alerts to a Prometheus Alert manager so they can then get routed to the right team.
```
