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

**7 Stages of PASTA:**
1. Define Business Objectives  
2. Define the Technical Scope  
3. Decompose the Application  
4. Analyze Threats  
5. Analyze Vulnerabilities and Weaknesses  
6. Model Attacks  
7. Conduct Risk Analysis & Remediation Planning

**Focus:** Business-aligned, risk-centric modeling  
**Use Case:** Enterprises or large systems requiring simulation-based threat evaluation

✅ Pros:
- Aligns with compliance & business goals
- Supports simulation and modeling
- Suitable for complex environments

📎 Learn more in [`pasta.md`](pasta.md)

---

## 4️⃣ LINDDUN (Privacy Threat Modeling)

**Focus:** Privacy threat analysis  
**Use Case:** Systems handling personal or sensitive data (e.g., GDPR compliance)

| Category | Example                                 |
|----------|-----------------------------------------|
| **L**inkability | Linking user sessions or actions  |
| **I**dentifiability | Identifying individuals       |
| **N**on-repudiation | Lack of user-deniable actions |
| **D**etectability | Visibility of system activities |
| **D**isclosure of Information | Leaked personal data |
| **U**nauthorized Actions | Misuse of data           |
| **N**on-compliance | Violating legal requirements   |

✅ Great for privacy by design and regulatory mapping

---

## 5️⃣ Attack Trees

**Focus:** Visual modeling of potential attack paths  
**Use Case:** Critical systems, control systems, risk visualization

- Root node = Goal of the attacker (e.g., “Steal user data”)
- Branches = Different steps/methods to reach the goal
- Supports logical operators (AND/OR)
- Helps in risk quantification

> Tip: Combine with STRIDE or DREAD for deeper analysis

---

## 🤔 Choosing the Right Methodology

| Method       | Best For                      | Strengths                          |
|--------------|-------------------------------|------------------------------------|
| STRIDE       | Software design               | Easy to learn, intuitive           |
| DREAD        | Threat scoring                | Simple, effective risk comparison  |
| PASTA        | Enterprise systems            | Business-aligned, simulation-ready |
| LINDDUN      | Privacy-focused apps          | Privacy-centric                    |
| Attack Trees | Visualizing attack surfaces   | Great for presentation & analysis  |

---

## 🔗 Resources & Next Steps

- [Introduction to Threat Modeling](introduction.md)
- [Checklist Template](../templates/threat-modeling-checklist.md)
- [Risk Calculator](../tools/risk_calculator.py)
