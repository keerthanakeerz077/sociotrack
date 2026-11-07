# AGENTS.md — Persistent Project Memory & Skill Activation Directives

> **Critical Instruction for Antigravity & AI Agents:**  
> This file is the permanent memory and operational law for this repository. You must ALWAYS consult and apply our active engineering and productivity skills to plan, implement, review, and ship features.

---

## 🛠️ Active Skills Mandate: Always Use Our Skills

The repository maintains an active suite of specialized skills in `.agents/skills/`. You are required to actively invoke and execute these workflows on every task:

| Skill | Trigger / Domain | Mandatory Standard |
| :--- | :--- | :--- |
| **`tdd`** | Building features, fixing bugs, writing tests | Follow the **red → green loop** in vertical slices (one seam, one test, minimal implementation). Test only against public **seams**, never private internals. No tautological tests. |
| **`codebase-design`** | Architecture, refactoring, module interfaces | Build **deep modules** (substantial behavior behind small interfaces). Place seams where callers gain leverage and maintainers gain locality. Hide implementation complexity. |
| **`code-review`** | Verifying diffs, PRs, before finishing tasks | Conduct **two-axis reviews**: **Standards** (Fowler code smells, repo conventions) and **Spec** (faithful implementation of requirements). |
| **`diagnosing-bugs`** | Broken features, test failures, regressions | Follow the systematic diagnostic loop: reproduce with minimal script, isolate root cause, formulate falsifiable hypothesis before changing code. |
| **`domain-modeling`** | Domain concepts, data models, state contracts | Maintain ubiquitous domain vocabulary. Consult and update [`GLOSSARY.md`](./GLOSSARY.md). Record architectural decisions. |
| **`implement`** | Feature implementation | Work in tracer-bullet vertical slices. Keep diffs minimal, focused, and tested before moving to the next slice. |
| **`to-spec` / `to-tickets`** | Task breakdown and planning | Synthesize user requirements into unambiguous specs and dependency-ordered vertical slice tickets. |
| **`improve-codebase-architecture`** | System architecture reviews | Identify deepening opportunities and eliminate shallow abstractions or tight coupling. |
| **`writing-for-agents`** | Creating skills, rules, prompts | Follow progressive disclosure, high-leverage context pointers, and deterministic process constraints. |

---

## 🧠 Project Core Memory: SocioTrack Engagement Agent

### 1. Architectural Philosophy
SocioTrack is an autonomous, memory-conditioned social media engagement system built with **FastAPI**, **LangGraph**, **ChromaDB / pgvector**, and **Next.js 14**. It replaces static LLM schedulers with a closed reinforcement learning loop.

### 2. LangGraph StateGraph (4 Deterministic Nodes)
1. **`retrieve_brand_memory`**: Semantic vector search retrieving the top 5 past winning posts and live audience sentiment from ChromaDB.
2. **`draft_post_variations`**: Synthesizes 3 distinct battle-tested formats:
   - **Format A (Data-first)**: Quantitative benchmarks, latency reductions, token cost savings.
   - **Format B (Hot take / Contrarian)**: Challenges industry defaults (e.g., Redis overuse, unconstrained swarms, ORM object caching).
   - **Format C (Tactical breakdown)**: Step-by-step 4-step implementation playbooks.
3. **`evaluate_brand_voice`**: Sub-second brand voice critique scoring drafts **0.0–10.0** against strict brand Dos and Don'ts; selects winning post.
4. **`update_memory_with_performance`**: Reinforcement learning evaluator. Evaluates simulated or real engagement metrics using the viral composite score formula.

### 3. The Core Reinforcement Equation
$$\text{Composite Score} = \frac{(\text{Shares} \times 3) + (\text{Replies} \times 2) + (\text{Likes} \times 1)}{\text{Impressions}} \times 100$$

- **Gating Barrier:** If $\text{Composite Score} > 5.0$, the post qualifies as high-performing / viral.
- **Memory Distillation:** The agent automatically extracts the core takeaway rule and vectorizes it into long-term memory (`_learned_lessons` collection).
- **Integrity Guard:** Posts with score $\le 5.0$ are discarded so bad content never corrupts the knowledge store.

### 4. Content & Voice Constraints (Empirical Rules)
- **Contrarian Hook:** Begin with a defensible counter-argument to common cargo-cult architecture. Never start with greetings, company news, or marketing fluff.
- **Zero Outbound Links:** Primary post bodies MUST NOT contain external URLs (-85% reach penalty). Value must be self-contained; links belong only in follow-up thread comments.
- **Anti-Jargon / Zero Hashtags:** Ban corporate buzzwords ("synergy", "paradigm shift"). Strictly 0 hashtags.
- **Code & Benchmarks:** Always pair claims with 4-8 line side-by-side code diffs or ASCII latency comparisons.
- **Timing:** Schedule primary technical debate posts at **14:00 UTC** (2:00 PM EST).

---

## 📐 Development Guidelines
1. **Pydantic Contracts First:** All inputs, outputs, agent state dictionaries, and API responses must be strictly validated with Pydantic v2 schemas.
2. **Deterministic Fallbacks:** The agent pipeline must always execute gracefully (<6.0 seconds), falling back to high-signal deterministic templates if third-party LLM providers time out.
3. **Seeded Test Data:** Test suites must execute against isolated, in-memory ChromaDB collections and SQLite instances without polluting production state.
