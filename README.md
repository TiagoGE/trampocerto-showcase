# TrampoCerto


**A full-stack mobile marketplace connecting construction workers with companies that need to hire fast.**

![React Native](https://img.shields.io/badge/React_Native-Expo-000020?logo=expo&logoColor=white)
![Next.js](https://img.shields.io/badge/Next.js-15-000000?logo=next.js&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?logo=typescript&logoColor=white)
![Supabase](https://img.shields.io/badge/Supabase-3FCF8E?logo=supabase&logoColor=white)
![Status](https://img.shields.io/badge/status-in_production-success)

</div>

> **Note:** This is a public showcase of a private, production project. The source code is closed, but this page documents the architecture, features and engineering decisions behind it.

---

## What it is

TrampoCerto is a two-sided marketplace for the construction industry. **Workers** (bricklayers, helpers, electricians) create a profile, get verified and apply to jobs. **Companies** post jobs, hire, track daily attendance and pay automatically. The product spans a **mobile app** (iOS + Android), a **web dashboard** for companies and an **admin panel** for operations — all on a single shared backend.

**Currently in production, in the process of being published to the Google Play Store and App Store.**

---

## Screenshots

### Company Dashboard (Web)
<div align="center">
  <img src="https://github.com/user-attachments/assets/e31b1b36-8808-4371-923d-53b63d50888c" alt="Company web dashboard" width="90%" />
</div>

### Mobile App
<div align="center">
  <img src="https://github.com/user-attachments/assets/642363c1-8e2c-4f39-9093-9f0f93c9300f" alt="Mobile app — worker profile" width="30%" />
  <img src="https://github.com/user-attachments/assets/16f48506-a578-4dad-981a-27168c77e2d9" alt="Mobile app — job feed" width="30%" />
  <img src="https://github.com/user-attachments/assets/043fe307-f260-4b00-8234-05274c42e4aa" alt="Mobile app — job detail" width="30%" />
</div>


### Admin Panel
<div align="center">
  <img src="https://github.com/user-attachments/assets/97eda95e-f841-4fdf-b6bd-a47e29dde73f" alt="Admin panel — overview" width="90%" />
</div>

---

## Tech Stack

| Layer | Technology |
|---|---|
| **Mobile** | React Native, Expo, Expo Router, NativeWind |
| **Web** | Next.js 15 (App Router), Tailwind CSS, shadcn/ui |
| **Language** | TypeScript (end-to-end) |
| **Backend** | Supabase — PostgreSQL, Auth, Storage, Realtime |
| **Serverless** | Supabase Edge Functions (Deno) |
| **Payments** | Asaas (marketplace split) — tokenized cards + PIX |
| **Infra** | Vercel, Cloudflare (WAF + DNS), EAS Build |

---

## Key Features

### For workers
- Profile with trades, availability, location radius and document verification
- Job feed filtered by distance and skills, with real-time application status
- Daily work log (attendance + activities) and contract extensions
- Payment history and PIX payout accounts
- Ratings and reputation

### For companies
- Post and manage jobs (daily-rate or fixed-price contracts)
- Review applicants, accept/reject, rate workers
- Daily attendance control with confirm/dispute flow
- Tokenized card on file; automatic billing
- Reputation and payment history

### Platform
- **Real-time** updates between both sides (Supabase Realtime)
- **Push notifications** (Expo Push) triggered directly from the database
- Transactional **emails** for critical events
- **Admin panel**: user/document verification, disputes, support tickets, audit log

---

## Architecture Highlights

- **End-to-end TypeScript** across 85+ screens (mobile app + web dashboard + admin).
- **Security-first data layer:** Row Level Security on every table, business logic enforced inside the database via `SECURITY DEFINER` functions — clients never trust their own IDs, every critical action is authorized server-side.
- **Marketplace payment model:** the platform never holds funds. Cards are **tokenized server-side (PCI-conscious)**, companies are charged automatically, and workers receive **PIX** transfers directly — handled by Edge Functions and scheduled cron jobs (weekly capture, fixed-price midpoint/completion charges).
- **Automated lifecycle:** job confirmation, auto-close, contract extensions, completion disputes and worker-removal flows are all driven by scheduled jobs.
- **Hardened auth:** PKCE flow, email-based MFA for companies, HMAC-signed admin sessions, privilege-escalation guards and a Cloudflare WAF in front.

---

## Engineering Decisions

A few choices I'm proud of:

- **Logic in the database, not the client.** Critical operations (accept job, payments, account deletion) run as atomic Postgres functions. This makes the rules impossible to bypass from a tampered client and keeps the two frontends thin.
- **RLS as the default, not an afterthought.** Every new table ships with Row Level Security enabled, so data isolation between companies and workers is enforced at the lowest layer.
- **Server-side card tokenization.** No raw card data ever touches the app — the mobile client opens a payment link, the token comes back via webhook.
- **One backend, three clients.** The mobile app, the company dashboard and the admin panel all consume the same Supabase backend, avoiding duplicated business rules.

---

## About

Built end-to-end by **Tiago Guerra Endsfeldz** — data modeling, backend, mobile app, web dashboard, payments and deployment.

- 🔗 LinkedIn: [LinkedIn - Tiago](https://www.linkedin.com/in/tiago-guerra-endsfeldz/)
- 🌐 Live: [TrampoCertoapp](https://www.trampocertoapp.com/)
- 📧 tiago.guerrae@gmail.com
