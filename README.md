# Enterprise EKS Platform

Enterprise-grade Kubernetes platform built on AWS EKS using Terraform, Helm, GitHub Actions, Argo CD, and modern GitOps practices.

## 📖 Overview

This project demonstrates the implementation of a production-inspired cloud-native platform that automates infrastructure provisioning, application deployment, CI/CD workflows, observability, and service mesh integration.

The platform provisions an Amazon EKS cluster using Terraform, deploys microservices using Helm charts, and implements a GitOps workflow with Argo CD. Container images are built, scanned, and pushed to Amazon ECR through GitHub Actions before being automatically deployed to the Kubernetes cluster.

---

## 🏗️ Architecture

```text
Developer
    │
    ▼
GitHub Actions
    │
    ▼
Amazon ECR
    │
    ▼
GitOps Repository
    │
    ▼
Argo CD
    │
    ▼
Amazon EKS
    │
    ▼
Enterprise Applications
```

---

## ⚙️ Technology Stack

### Cloud & Infrastructure

* AWS EKS
* Terraform
* Amazon ECR

### Containerization & Orchestration

* Docker
* Kubernetes
* Helm

### CI/CD & GitOps

* GitHub Actions
* Argo CD

### Observability

* Prometheus
* Grafana
* Jaeger
* OpenTelemetry

### Service Mesh

* Istio

---

## 📂 Repository Structure

```text
enterprise-eks-platform/
├── terraform/
│   ├── main.tf
│   ├── variables.tf
│   └── outputs.tf
│
├── helm/
│   ├── frontend/
│   ├── users-service/
│   ├── orders-service/
│   ├── inventory-service/
│   └── payments-service/
│
├── apps/
│   ├── frontend/
│   ├── users-service/
│   ├── orders-service/
│   ├── inventory-service/
│   └── payments-service/
│
└── .github/
    └── workflows/
        └── ci-cd.yml
```

---

## 🚀 Key Features

### Infrastructure as Code (IaC)

* Provisioned Amazon EKS cluster using Terraform
* Configured worker nodes and networking components
* Automated Kubernetes cluster creation and management
* Reproducible infrastructure deployments

### Kubernetes Deployments

* Helm-based deployment strategy
* Independent deployment configuration for each service
* Environment-specific values support
* Kubernetes-native application management

### GitOps Workflow

* Argo CD continuously monitors desired state
* Automated synchronization between Git and Kubernetes
* Declarative deployment model
* Version-controlled infrastructure and application manifests

### CI/CD Automation

GitHub Actions pipeline performs:

1. Source code checkout
2. Dependency installation
3. Application testing
4. Docker image build
5. Trivy vulnerability scanning
6. Amazon ECR image push
7. GitOps repository update
8. Automated Argo CD deployment

---

## 🧩 Microservices

The platform currently deploys the following services:

| Service           | Purpose                       |
| ----------------- | ----------------------------- |
| Frontend          | User-facing web application   |
| Users Service     | User management operations    |
| Orders Service    | Order processing workflows    |
| Inventory Service | Inventory management          |
| Payments Service  | Payment processing operations |

---

## 📊 Observability Stack

### Prometheus

* Metrics collection
* Kubernetes monitoring
* Application performance metrics

### Grafana

* Dashboard visualization
* Real-time monitoring
* Operational insights

### Jaeger

* Distributed tracing
* Request flow analysis
* Performance bottleneck identification

### OpenTelemetry

* Telemetry collection
* Metrics and trace export
* Vendor-neutral observability integration

---

## 🔐 Security Practices

* Container vulnerability scanning using Trivy
* Secure AWS credential management via GitHub Secrets
* Immutable image tagging strategy
* GitOps-based deployment approvals
* Infrastructure managed through code review processes

---

## 🌐 Service Mesh

Istio is integrated to provide:

* Service-to-service communication management
* Traffic routing and control
* Canary deployment capabilities
* Mutual TLS (mTLS)
* Observability enhancements

---

## 🔄 Deployment Workflow

```text
Code Commit
      │
      ▼
GitHub Actions
      │
      ▼
Build Docker Image
      │
      ▼
Trivy Security Scan
      │
      ▼
Push Image to Amazon ECR
      │
      ▼
Update GitOps Repository
      │
      ▼
Argo CD Sync
      │
      ▼
Deploy to Amazon EKS
```

---

## 📁 Related Repository

GitOps manifests are maintained separately in:

```text
enterprise-eks-gitops
```

This repository contains:

* Argo CD applications
* Environment configurations
* Kubernetes manifests
* Deployment definitions

---

## 🎯 Learning Outcomes

This project provided hands-on experience with:

* Infrastructure automation using Terraform
* Amazon EKS cluster management
* Kubernetes application deployment
* Helm chart development
* CI/CD implementation using GitHub Actions
* GitOps workflows with Argo CD
* Container security scanning
* Kubernetes observability practices
* Service mesh architecture with Istio
* Enterprise platform engineering concepts

---

## 📌 Future Enhancements

* Multi-environment deployment strategy (Dev, QA, Prod)
* Advanced canary deployments using Istio
* Automated rollback mechanisms
* Policy enforcement using OPA Gatekeeper
* Secrets management using AWS Secrets Manager
* Cluster autoscaling enhancements
* Centralized logging with Loki

---

## 📜 Disclaimer

This project was developed as a hands-on Platform Engineering and Cloud-Native learning initiative to demonstrate modern Kubernetes, GitOps, CI/CD, observability, and service mesh implementation patterns in an enterprise-style environment.
