---
draft: false
title: Prometheus
content:
  id: prometheus
  name: Prometheus
  logo: /images/hosting-and-infrastructure/monitoring/prometheus/logo.png
  website: https://prometheus.io/
  iframe_website: /website-iframe/hosting-and-infrastructure/monitoring/prometheus
  dashboardImage: /images/hosting-and-infrastructure/monitoring/prometheus/screenshot-1.png
  short_description: Power your metrics and alerting with the leading open-source monitoring solution
  description: Prometheus, a Cloud Native Computing Foundation project, is a systems and service monitoring system. It collects metrics from configured targets at given intervals, evaluates rule expressions, displays the results, and can trigger alerts when specified conditions are observed.
  features:
    - title: Data model
      description: "Prometheus fundamentally stores all data as time series: streams of timestamped values belonging to the same metric and the same set of labeled dimensions. Besides stored time series, Prometheus may generate temporary derived time series as the result of queries."
    - title: Querying prometheus
      description: Prometheus provides a functional query language called PromQL (Prometheus Query Language) that lets the user select and aggregate time series data in real time. The result of an expression can either be shown as a graph, viewed as tabular data in Prometheus's expression browser, or consumed by external systems via the HTTP API.
    - title: Grafana support for prometheus
      description: "Grafana supports querying Prometheus. The Grafana data source for Prometheus is included since Grafana 2.5.0 (2015-10-28).

The following shows an example Grafana dashboard which queries Prometheus for data:"
    - title: Configuration
      description: Prometheus is configured via command-line flags and a configuration file. While the command-line flags configure immutable system parameters (such as storage locations, amount of data to keep on disk and in memory, etc.), the configuration file defines everything related to scraping jobs and their instances, as well as which rule files to load.
  screenshots:
    - /images/hosting-and-infrastructure/monitoring/prometheus/screenshot-1.png
    - /images/hosting-and-infrastructure/monitoring/prometheus/screenshot-2.png
---