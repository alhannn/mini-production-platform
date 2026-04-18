# Mini Production Platform

A mini production-style SaaS monitoring platform built to learn software reliability engineering, platform engineering, and observability practices.

## Project goal

This project simulates a small real-world platform that monitors service health, tracks incidents, and demonstrates how to build and operate a distributed application using modern infrastructure tooling.

## Planned architecture

- Frontend dashboard
- Backend API
- Background worker
- Postgres
- Redis
- Docker Compose for local development
- Kubernetes for orchestration
- GitHub Actions for CI/CD
- Prometheus + Grafana for observability
- OpenTelemetry for tracing and telemetry
- Alerting, load testing, runbooks, and postmortems

## Repository structure

```text
services/
  frontend/
  api/
  worker/

infrastructure/
  docker/
  kubernetes/
  monitoring/

docs/
  architecture/
  runbooks/
  postmortems/

scripts/
.github/
  workflows/