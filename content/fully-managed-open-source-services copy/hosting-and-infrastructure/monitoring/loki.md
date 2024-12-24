---
draft: false
title: Loki fully managed open source service | OctaByte.io

meta:
  cover: /images/hosting-and-infrastructure/monitoring/dockerregistry/screenshot-1.jpg
  description: Loki is a highly scalable, multi-tenant log aggregation tool inspired by Prometheus, designed to provide cost-effective log management with easy operation.
  keywords: Loki, log aggregation, scalable logs, cost-effective logging, Prometheus, Grafana, multi-tenant logs, log management, LogQL, cloud logging, log storage, Promtail
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
  title: "Cost-Effective, Scalable Log Aggregation System for Modern Environments"
  logo: /images/hosting-and-infrastructure/monitoring/loki/logo.png
  website: https://grafana.com/oss/loki/
  iframe_website: /website/hosting-and-infrastructure/monitoring/loki
  direct_link: true
  description: "Loki is a horizontally scalable and highly available log aggregation system that is inspired by Prometheus. This open-source tool simplifies log management by using labels instead of indexing the content of the logs, making it both efficient and cost-effective. Loki supports multi-tenancy, ensuring isolated log streams for different users or environments. Its seamless integration with Prometheus and Grafana allows you to collect, store, and query logs with ease, offering a streamlined solution for monitoring and troubleshooting in complex systems.

With Loki, logs are grouped into streams indexed by labels rather than the log content itself, making it fast and efficient. This approach minimizes storage costs while enabling quick query responses. Loki's compatibility with Prometheus’ service discovery and its integration with Grafana make it an ideal choice for teams looking to manage and analyze logs alongside other monitoring data. Whether you're running a small service or a large-scale infrastructure, Loki ensures that your log aggregation remains highly available, scalable, and low-cost."
  features:
    - title: Pull in Any Logs with Promtail
      description: "Promtail is a dedicated log collector for Loki, designed to gather logs from various sources. It integrates seamlessly with Prometheus’ service discovery and provides advanced features for labeling, transforming, and filtering logs before they are ingested into Loki, ensuring that your logs are organized and relevant from the start."
    - title: Store Logs Efficiently with Loki
      description: "Unlike traditional log aggregation systems, Loki does not index the text of logs, focusing instead on indexing logs by labels. This unique approach reduces storage costs and allows for lightning-fast queries, making it easier to manage large volumes of logs without compromising performance."
    - title: Use LogQL to Explore Your Logs
      description: "Loki comes with a powerful query language called LogQL, which allows users to query logs efficiently. Whether you're using Grafana to visualize logs alongside other metrics or LogCLI for command-line access, LogQL offers robust querying capabilities for in-depth analysis and troubleshooting."
    - title: Alert on Log Events
      description: "With Loki’s built-in alerting system, you can set up alerts based on log patterns and behaviors. These alerts can be routed to a Prometheus Alert manager, ensuring that critical log events trigger timely responses from the right team members."
    - title: Seamless Integration with Grafana
      description: "Loki integrates smoothly with Grafana, enabling users to visualize logs in real-time alongside other monitoring data. This integration offers a unified view of your entire system, empowering teams to monitor and troubleshoot applications more effectively."
    - title: Horizontal Scalability for Large Environments
      description: "Loki is designed to scale horizontally, making it ideal for both small applications and large, distributed systems. This scalability ensures that your logging infrastructure can grow with your needs, maintaining performance and availability regardless of log volume."
  screenshots:
    - /images/hosting-and-infrastructure/monitoring/loki/screenshot-1.png
    - /images/hosting-and-infrastructure/monitoring/loki/screenshot-2.png
---
