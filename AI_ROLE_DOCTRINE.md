\# AI Role Doctrine



\## Purpose

This document defines the permanent role boundaries of AI within this system.



The goal is to preserve:

\- Determinism

\- Repeatability

\- Auditability

\- User decision ownership



AI is explicitly constrained to prevent erosion of these properties.



---



\## What AI IS allowed to do



AI may:

\- Explain outputs produced by deterministic calculations

\- Rephrase or summarise user-provided data

\- Generate documentation or descriptions

\- Assist with UI wording

\- Assist with data visualisation of already-computed results

\- Assist with scenario narration \*\*without altering inputs or outputs\*\*



AI may never modify core calculations.



---



\## What AI is NOT allowed to do (hard prohibitions)



AI must never:

\- Generate or modify core calculations

\- Change assumptions

\- Infer missing inputs

\- Suggest actions or decisions

\- Optimise outcomes

\- Rank scenarios as “better” or “worse”

\- Replace deterministic logic with probabilistic logic

\- Decide on behalf of the user



If AI output changes the result, the system is broken.



---



\## AI and decision ownership



\- All decisions remain with the user

\- The system presents consequences, not advice

\- AI must not express recommendations

\- AI must not express confidence or authority



Language such as “you should” or “best option” is prohibited.



---



\## AI and auditability



\- AI output must be clearly labeled as explanatory

\- Core outputs must remain reproducible without AI

\- The system must function fully if AI is disabled



AI is an accessory, not a dependency.



---



\## Enforcement principle



If a feature requires AI to function correctly, it is out of scope.



If removing AI changes outcomes, the design has failed.



This doctrine takes precedence over convenience, UX, and feature richness.



