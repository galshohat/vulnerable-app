# InboxOps — Intentionally Vulnerable Demo Application

> ⚠️ **WARNING**: This application is **deliberately insecure**. It is designed as a
> training target for the AI Security Agents Workshop. **Do NOT deploy this
> application in any environment connected to real users or data.**

## What Is This?

InboxOps is a fake email-marketing SaaS platform. It was built from scratch with
dozens of realistic security vulnerabilities planted across every layer of the
stack — authentication, database access, file handling, cryptography, API
design, CI/CD, infrastructure-as-code, and dependency management.

Workshop participants use AI agents (built with the Azure AI Agent Service SDK)
to scan this repository, discover the vulnerabilities, and produce a security
audit report — all without being told what to look for or where.

## Repository Structure

```
.
├── app.py                  # Flask application — routes, CORS, error handling
├── auth.py                 # Authentication — login, registration, sessions
├── database.py             # Database layer — queries, connection handling
├── config.py               # Application configuration and secrets
├── payments.py             # Stripe payment integration
├── requirements.txt        # Python dependencies (pinned to vulnerable versions)
├── .env                    # Environment variables (committed — intentional)
│
├── api/
│   ├── endpoints.py        # REST API routes
│   └── middleware.py       # Request/response middleware
│
├── utils/
│   ├── crypto.py           # Encryption and hashing utilities
│   ├── file_handler.py     # File upload and path handling
│   └── xml_parser.py       # XML import/export parsing
│
├── deploy/
│   ├── Dockerfile          # Container image definition
│   ├── docker-compose.yml  # Multi-service orchestration
│   └── terraform/
│       └── main.tf         # AWS infrastructure provisioning
│
└── .github/
    └── workflows/
        └── ci.yml          # CI/CD pipeline definition
```

## Vulnerability Categories

The planted issues span the following categories:

| Category | Examples |
|---|---|
| **Injection** | SQL injection, command injection, SSTI, XSS, XXE |
| **Authentication & Sessions** | Weak hashing, timing attacks, insecure sessions |
| **Secrets Management** | Hardcoded API keys, committed `.env`, leaked credentials |
| **Cryptography** | Weak algorithms (MD5/SHA1), static IVs, short keys |
| **Infrastructure** | Over-permissive IAM, public S3 buckets, no TLS enforcement |
| **Dependencies** | Pinned to versions with known CVEs |
| **CI/CD** | Missing security scans, hardcoded credentials in pipelines |
| **Access Control** | IDOR, missing authorization checks, CORS misconfiguration |

## How It's Used in the Workshop

1. Participants configure an MCP tool pointing at this repository.
2. They build AI agents that read files, search code, and analyze patterns.
3. The agents discover vulnerabilities autonomously — no hints are provided.
4. Agents produce structured findings with severity scores, explanations, and
   remediation steps.

Participants never modify this repo. It exists purely as a read-only scan target.

## Tech Stack (Simulated)

- **Backend**: Python / Flask
- **Database**: PostgreSQL (via raw SQL — no ORM)
- **Payments**: Stripe API
- **Infra**: Docker, Terraform (AWS)
- **CI/CD**: GitHub Actions

## License

This repository is part of the AI Security Agents Workshop training materials.
It is provided for **educational purposes only**.
