# GLOSSARY.md — SocioTrack Domain Vocabulary

This glossary establishes the ubiquitous domain language for the **SocioTrack** self-learning engagement agent. All agent prompts, test names, Pydantic schemas, and frontend UI components must strictly adhere to these definitions.

---

### Core Domain Concepts

#### 1. `StateGraph`
The deterministic, directed acyclic or cyclic state machine (powered by LangGraph) that orchestrates memory retrieval, post generation, brand voice evaluation, and reinforcement reflection.

#### 2. `Brand Voice Gate` (Node 3)
A fast, sub-second evaluation node that grades candidate drafts on a scale from **0.0 to 10.0** based on tone, technical rigor, absence of marketing jargon, adherence to zero-link rules, and absence of hashtags.

#### 3. `Composite Score`
The quantitative virality formula measuring authentic community engagement:
$$\text{Composite Score} = \frac{(3 \times \text{Shares}) + (2 \times \text{Replies}) + (1 \times \text{Likes})}{\text{Impressions}} \times 100$$
A score above **5.0** triggers the reinforcement learning node.

#### 4. `Learned Lesson`
A distilled, actionable engineering hypothesis or operational rule extracted from a winning post ($\text{Composite Score} > 5.0$). It is vectorized using text embeddings and stored in ChromaDB's `_learned_lessons` collection.

#### 5. `Audience Sentiment`
A structured vector record capturing practitioner attitude, skepticism level, and current hot-button concerns (e.g., *"cautious and demanding"*, seeking concrete benchmarks over toy swarms).

#### 6. `Seam`
A public interface boundary where tests observe system behavior (e.g., calling `run_agent_cycle` or `ingest_analytics`) without inspecting or coupling to private internal state.

#### 7. `Tracer Bullet`
A vertical slice that connects all application layers (UI component $\rightarrow$ FastAPI endpoint $\rightarrow$ LangGraph node $\rightarrow$ ChromaDB vector store) to verify end-to-end functionality before horizontal expansion.

#### 8. `Zero-Link Constraint`
An algorithmic rule mandating that the primary post body contain zero external URLs to avoid platform distribution penalties (-85% reach suppression). Technical value must be self-contained within the post; links are reserved for follow-up comments.
