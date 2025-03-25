# 🧠 Threat Modeling Methodologies

Threat modeling methodologies provide structured frameworks for identifying, analyzing, and mitigating potential threats. Choosing the right method depends on the system's complexity, regulatory needs, and team familiarity.

This document summarizes the most widely used methodologies in cybersecurity threat modeling.

---

## 1️⃣ STRIDE (Microsoft)

**Focus:** Classification of threats  
**Use Case:** Software/system design phase

| Category               | Description                                | Example                                 |
|------------------------|--------------------------------------------|-----------------------------------------|
| **S**poofing           | Impersonating another identity             | Attacker logs in as another user        |
| **T**ampering          | Modifying data or system state             | Change database entries without auth    |
| **R**epudiation        | Denying actions without evidence           | No audit logs to track actions          |
| **I**nformation Disclosure | Exposing sensitive data                 | Leaking PII through logs                |
| **D**enial of Service  | Crashing or exhausting system resources    | DDoS attack brings down service         |
| **E**levation of Privilege | Gaining unauthorized access rights     | Limited user gets admin access          |

---

## 2️⃣ DREAD

**Focus:** Risk scoring and prioritization  
**Use Case:** Evaluating and ranking threats based on impact and exploitability

| Category          | Question it answers                              |
|-------------------|--------------------------------------------------|
| **D**amage        | How severe is the damage if exploited?           |
| **R**eproducibility | Can the threat be reproduced easily?           |
| **E**xploitability | How easy is it to exploit the threat?           |
| **A**ffected Users | How many users would be impacted?              |
| **D**iscoverability | How easy is it to discover the vulnerability? |

> Score each category 1–10 to prioritize threats.  
> Total Score = D + R + E + A + D

📎 Learn more in [`dread.md`](dread.md)

---

## 3️⃣ PASTA (Process for Attack Simulation and Threat Analysis)

**Focus:** Business-aligned, risk-centric modeling  
**Use Case:** Enterprises or large systems requiring simulation-based threat evaluation
