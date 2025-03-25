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
