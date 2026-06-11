# Plan: Governance-Centered Applied Mathematics Course Sequence

## STRATEGIC DECISIONS (from user input)
- **Tight governance framing**: Every unit explicitly tied to government/institutional decision-making
- **Narrative arc**: "Who you elect matters" → show impact through policy decisions, representation systems, and algorithmic governance
- **Pharmacokinetics as Unit 1**: Simplest math foundation + real policy relevance (healthcare governance)
- **Sports analytics**: Repurposed as homework assignments for dimensionality reduction practice
- **Markov chains**: Advanced optional extension for redistricting (not core requirement)
- **New topic**: Social Media Content Moderation & AI Fairness as Unit 5
- **Foundation**: SIAM M3 modeling framework (already exists, needs development)

## PROPOSED UNIT STRUCTURE

### Unit 0: Mathematical Modeling Foundations (NEW - polished version)
**Topic**: The Six-Step Modeling Process for Policy Decisions
**Governance Context**: How do we translate messy real-world policy problems into solvable math?
**Math**: Problem formulation, variables, constraints, validation cycles
**Materials Needed**: Polish SIAM M3 section (currently 20% stub) with policy examples
**Example Policy**: Decision to approve/regulate a medication
**Duration**: 1 week (foundations only)

---

### Unit 1: Healthcare Policy & Pharmacokinetics
**Topic**: Who You Elect Matters: Medication Approval & Dosing Governance
**Governance Context**: 
- Medication approval policies (FDA decisions, gender-affirming therapy access)
- Dosing protocols & withdrawal safety (institutional decisions)
- Healthcare equity across populations
**Math**: 
- Differential equations (dH/dt = -kH)
- Exponential decay & half-life
- Logarithms for solving time-based problems
- Recurrence relations for discrete dosing schedules
- Equilibrium analysis for repeated dosing
**Prerequisites**: Algebra, functions, exponentials (pre-calculus review in Unit 0)
**Existing Materials**: 95-100% complete (all 4 halflives activities, homework-01)
**New Materials Needed**: Explicit governance framing introduction; patient equity case studies
**Assignments**: 
- Homework 01 (keep as-is: Effexor XR modeling)
- Add governance reflection: How do dosing decisions affect different populations?

---

### Unit 2: Electoral Representation & Apportionment
**Topic**: How Congress Divides Power: Fair Allocation of Seats
**Governance Context**:
- Constitutional apportionment (every 10 years post-Census)
- State representation fairness
- Paradoxes: Alabama Paradox, Population Paradox, Condorcet Paradox
- International comparisons (parliament sizes, proportional vs. winner-take-all)
**Math**:
- Proportional reasoning & ratios
- Divisor methods (Jefferson, Hamilton, Huntington-Hill, Adams)
- Rounding rules & fairness metrics
- Introduction to optimization: "What is fair?" formalized
**Prerequisites**: Unit 0 (modeling), basic algebra
**Existing Materials**: 
- Basic: 60% complete (00-apportionment.ptx)
- Extended: 85% complete (00-alt-apport.ptx)
- Homework 0: 100% complete (alternative methods)
- Older materials: Barycentrics, error-based methods, TikZ visualizations, 1790 Census data
**New Materials Needed**: 
- Integrate barycentrics visualization from older materials
- Formalize fairness criteria mathematically
- Add international parliament examples
**Assignments**:
- Homework 0 (keep as-is: coffee allocation methods)
- Add: Compare apportionment methods on real Congressional data
- Optional advanced: Explore error minimization formalization

---

### Unit 3: District Design & Voting Rights
**Topic**: Drawing Boundaries: Gerrymandering Detection & Fair Redistricting
**Governance Context**:
- Constitutional voting rights protection
- Legal standards: compactness, contiguity, equal population
- Detecting partisan intent (efficiency gap, declination)
- Racial gerrymandering vs. redistricting for minority representation (LULAC v. Perry)
- Who benefits from unfair districts?
**Math**:
- Graph theory (vertices, edges, connectivity, components)
- Compactness measures (Polsby-Popper, isoperimetric ratio, Reock)
- Geometric fairness concepts
- Introduction to optimization constraints
**Prerequisites**: Unit 0, Unit 1 or 2 (proportional thinking)
**Existing Materials**:
- Core: 85% complete (02-districting.ptx)
- Older materials: LULAC v. Perry oral arguments, compactness research, Virginia redistricting code
- R ensemble code: Complete (not yet student-facing)
**New Materials Needed**:
- Formalize compactness metrics pedagogically
- Add legal/governance framing (voting rights act, constitutional cases)
- Create guided activity: Student designs districts, gets feedback on fairness metrics
**Assignments**:
- Activity: Design 3-district plan for given state, measure compactness
- Homework: Analyze real district data for gerrymandering signals
- Optional advanced: Markov chain ensemble methods (in advanced materials)

---

### Unit 4: Linear Algebra & Data Governance
**Topic**: What Does Your Data Say? Reducing Dimensions, Finding Patterns
**Governance Context**:
- How do platforms & governments use data about citizens?
- Dimensionality reduction in social science research
- Ethics of data collection & analysis
- Who counts? How data silences or amplifies communities
**Math**:
- Covariance matrices & correlation
- Eigenvalues & eigenvectors
- Principal Component Analysis (PCA) by hand & computational
- t-SNE (intuition + application)
- Optional: SVD, word embeddings
**Prerequisites**: Unit 0, linear algebra (eigenvectors/eigenvalues)
**Existing Materials**:
- Theory: 85% complete (01-dimensionality.ptx)
- AI ethics: 85% complete (training data labor exploitation context)
- Activities: PCA/t-SNE toy examples (100% complete)
- Notebooks: Hockey, UFC analytics (50% scaffolding)
- Fact-check activity: "Platforms and AI" (60% complete)
**New Materials Needed**:
- Governance framing: "Data about decisions"
- Activity: Analyze demographic data, identify what can/cannot be discovered
- Ethical case study: Predictive policing (where data fails communities)
**Assignments**:
- Guided PCA activity (keep existing toy examples)
- Homework: Sports analytics (repurposed) - use hockey/UFC data to practice PCA/t-SNE, OR demographic data analysis
- Fact-checking assignment: AI literacy (existing)

---

### Unit 5: Algorithmic Governance & Content Moderation
**Topic** (NEW): Platform Decisions at Scale: Who Controls Speech?
**Governance Context**:
- Social media content moderation (Meta, YouTube, TikTok)
- Meta Oversight Board case studies
- Automated vs. human decisions
- Bias in detection algorithms
- Global governance variations (EU DSA, China regulations)
**Math**:
- Classification algorithms (logistic regression framework)
- Fairness metrics: precision/recall trade-offs
- False positive/negative harm analysis
- Optimization subject to fairness constraints
- Information theoretic fairness concepts
**Prerequisites**: Unit 0, Unit 4 (linear algebra & data analysis)
**Existing Materials**:
- Partial: AI ethics from Unit 4
- Pulitzer Center materials on platform governance
- Papers on algorithmic fairness (research level)
**New Materials Needed**: 
- Develop this as complete unit (currently nonexistent)
- Create simplified classification algorithm scenario
- Build activity: Design content moderation rule, analyze disparate impact
- Case studies: Meta Oversight Board decisions
**Potential Math Approaches**:
- Simplified confusion matrix analysis → fairness metrics
- Constrained optimization: Max accuracy subject to demographic parity
- Or: Information-theoretic approach (Mutual Information with protected attributes)
**Assignments**:
- Activity: Given a classification problem, explore accuracy/fairness trade-off
- Case study analysis: Meta Oversight Board decision
- Homework: Analyze a real platform policy for potential disparate impact

---

### Unit 6: Advanced Topics & Integration (OPTIONAL/CAPSTONE)

**Option A: Convex Geometry & Optimization**
- Math: Simplices, linear functionals, constrained optimization
- Application: Fairness as constrained optimization problem across all units
- Materials: Barycentrics from older materials + formalization
- Prerequisite: Units 1-5

**Option B: Markov Chains & Redistricting Ensembles**
- Math: Stochastic processes, MCMC, ensemble methods
- Application: Generate fair redistricting plans via chain sampling
- Materials: Existing R code + academic papers from older materials
- Prerequisite: Units 0-3

**Option C: Comparative Governance Systems**
- Cross-national comparison: How do different countries handle apportionment, representation, data governance, speech regulation?
- Mathematics: How do different systems instantiate fairness?
- Prerequisite: Units 1-5 (depending on focus)

---

## MATHEMATICAL PROGRESSION (PREREQUISITES BUILD)

```
Unit 0: Modeling Framework
        ↓
Unit 1: Calculus (DE, exponential, logarithm)
        ↓
Unit 2: Proportional reasoning, optimization basics
        ↓
Unit 3: Graph theory
        ↓
Unit 4: Linear algebra (covariance, eigenvalues, PCA)
        ↓
Unit 5: Statistics & classification (uses LA + calculus)
        ↓
Unit 6 (Optional): Advanced integration
```

**All units grounded in**: Calculus (pre-req) + Linear Algebra (pre-req), no higher mathematics needed

---

## CRITICAL FILES TO CREATE/MODIFY

### New Files Needed
- `source/notes/00-modeling-framework.ptx` — Polish SIAM M3 section (currently 20% stub)
- `source/notes/05-content-moderation.ptx` — NEW unit on algorithmic governance
- `source/homework/homework-02.ptx` — Apportionment application assignment
- `source/homework/homework-03.ptx` — Districting analysis assignment
- `source/homework/homework-04.ptx` — Sports analytics (repurposed) OR demographic data analysis
- `source/homework/homework-05.ptx` — Content moderation fairness trade-off assignment

### Files to Modify/Integrate
- `source/notes/00-apportionment.ptx` — Add governance framing introduction
- `source/notes/02-districting.ptx` — Strengthen legal/voting rights context (from older LULAC materials)
- `source/notes/01-dimensionality.ptx` — Reframe as "data governance" not just "LLMs"
- `source/activities/` — Create new guided activity for district fairness analysis
- `main.ptx` — Reorder chapters to follow Unit 0→1→2→3→4→5 progression

### Materials to Integrate from Older Folder
- Barycentrics visualization & theory (Unit 2)
- LULAC v. Perry legal analysis & context (Unit 3)
- Compactness measure research papers (Unit 3)
- R redistricting ensemble code documentation (Unit 3 advanced)
- Pulitzer Center platform governance materials (Unit 5)

---

## IMPLEMENTATION PHASES

**Phase 1: Foundation Polishing**
- Develop Unit 0 (modeling framework) from stub
- Add governance framing to Units 1-3 existing materials
- Update main.ptx chapter ordering

**Phase 2: Governance Integration**
- Rewrite Unit 4 (dimensionality) intro with data governance framing
- Create Unit 5 (content moderation) from scratch
- Migrate relevant older materials into student-facing content

**Phase 3: Assessment & Activities**
- Create missing homework assignments (02, 03, 04, 05)
- Create guided activity for district fairness analysis
- Repurpose sports analytics as homework exercise

**Phase 4: Advanced Integration (Optional)**
- Document Markov chain ensemble methods as advanced extension
- Create convex geometry capstone materials
- Build comparative governance unit

---

## GOVERNANCE NARRATIVE THREAD

**Across all units, answer: "Who decides?"**

- **Unit 1 (Healthcare)**: Doctors and regulators decide dosing. Governance: FDA, institutional ethics boards, patient access equity
- **Unit 2 (Apportionment)**: Electoral college decides power distribution. Governance: Congress, state legislatures, constitutional constraints
- **Unit 3 (Redistricting)**: State legislators decide district boundaries. Governance: Courts enforce voting rights, protect minorities
- **Unit 4 (Data Analysis)**: Researchers/platforms decide what's measurable. Governance: Data ethics, representation in datasets, silenced voices
- **Unit 5 (Content Moderation)**: Platforms (via algorithms + humans) decide what gets published. Governance: Meta Oversight Board, regulatory frameworks, competing rights

**Capstone reflection**: How does math formalize fairness in governance? Where does math fail?

---

## VERIFICATION CHECKPOINTS

1. **Unit 0**: Mathematical Modeling section no longer a stub; includes policy examples
2. **Unit 1**: Homework 1 solution includes governance reflection; all 4 halflives activities tied to policy context
3. **Unit 2**: Alternative apportionment methods integrated; barycentrics visualization added
4. **Unit 3**: LULAC v. Perry case study included; student can explain compactness measures
5. **Unit 4**: PCA activity completed with data governance framing; ethics component present
6. **Unit 5**: Content moderation unit complete with fairness metric activity and case study
7. **Main.ptx**: All chapters ordered correctly; prerequisite dependencies clear to students
8. **Assessment**: All homework assignments (02-05) created and tested; at least 2 cover governance applications explicitly

---

## SCOPE & EXCLUSIONS

**INCLUDED**:
- All 5 core governance units
- Integration of 85%+ complete materials
- Selective integration of older research materials (barycentrics, LULAC, compactness measures)
- Sports analytics repurposed as homework

**EXCLUDED** (for future expansion):
- Markov chain ensemble methods (advanced optional only)
- Convex geometry capstone (optional)
- Climate/environmental policy modeling
- Supply chain modeling
- Game theory in voting
- Bayesian inference

---

## OPEN QUESTIONS FOR USER

None - user has provided clear direction. Recommend proceeding with Phase 1 immediately.

## Additional content for apportionment and coordinates follows

# Barycentric Coordinates
## harnessing affine space to model methods for solving allocation problems

### Background: affine space
A <term>vector space</term> should be familiar from linear algebra: it is a nonempty set satisfying the 10 vector space properties. In <m>\RR^n</m>, a line, plane, or higher-dimensional analogue passing through the origin is a vector space.

Many lines, planes, and higher dimensional analogs miss the origin, though; we call these <term>affine spaces</term> and we can think of them as vector spaces that have been translated away from the origin.

Most of our intuition-building examples will occur on a line, <m> \ell = \{(x,y) \, | \, x + y = d\}</m>, or a plane, <m>P: \{ (x,y,z) \, | \, x + y + z = d\}</m>. More generally, we'll be interested in points in <m>\RR^n</m> of the form <me> x_1 + x_2 + \cdots + x_n = d</me> for some <m>d \gt 0</m>.

(definition: affine combination)

(picture: line)

(picture: plane)

<!--

Proposition. If <m>P_1 \neq P_n</m> in <m>\RR^n</m>, <m>n \geq 2</m>, there is a unique line passing through <m>P_1</m> and <m>P_2</m>. For this reason, we say <m>P_1</m> and <m>P_2</m> determine a line.

Proof. Suppose <m>P_1 = (a_1, \ldots, a_n)</m> and <m>P_2 = (b_1, \ldots, b_n)</m>. Let <m>O</m> denote the origin. From Calculus, we know that a line is given by <m>r = r_0 + t d</m> where <m>r</m> is the position vector of an arbitrary point on the line, <m>r_0</m> is the position vector of a specific point on the line, <m>d</m> is the direction vector of the line, and <m>t</m> is a real-valued parameter.

(geogebra applet?)

From the given information, we can take <m>OP_1</m>,  <m>r_0 = OP_1</m>

Proposition. For all <m>n \geq 3</m>, if <m>P_1, P_2, P_3</m> are non-collinear points in <m>\RR^n</m>, they determine a <m>2</m>-dimensional plane.

Proposition. More generally, for all <m>n \geq 3</m>, if the points <m>P_1, \ldots,P_d</m> do not all lie within an affine space of dimension smaller than <m>d</m>, they determine a <m>(d-1)</m>-dimensional affine space.

Proof problem. Let <m>P_1, P_2, P_3</m> be non-collinear points. Show that for every point <m>Q</m> on the plane determined by <m>A, B, C</m>, there are unique numbers <m>x_1, x_2, x_3</m> satisfying <m>x_1 + x_2 + x_3 = 1</m> and <m>Q = x_1P_1 + x_2P_2 + x_3P_3</m>.

Generalize to <m>d \leq n</m> points that do not all lie within an affine space of dimension smaller than <m>d</m>.

Remark. The values <m>x_1, \ldots, x_d</m> are an <term>invariant</term> of the points <m>P_1,\ldots,P_d</m> and <m>Q</m>.

Proof problem. For three non-collinear points <m>P_1,P_2,P_3</m> and a point <m>Q</m> on the plane they determine, we can interpret the numbers <m>x, y, z</m> as in the previous problem as areas.

(picture)

Verify that <m>x = \frac{\area(QP_2P_3)}{\area(P_1P_2P_3)}</m>, <m>y = \frac{\area(QP_1P_3)}{\area(P_1P_2P_3)}</m>, and <m> z = \frac{\area(QP_1P_2)}{\area(P_1P_2P_3)}</m>.
-->

Simplices. The subset of points in <m>\RR^n</> with coordinates that are nonnegative and sum to one form an <m>n</m>-simplex, called the <term>convex hull</term> of (points).

(picture)

(theorem: simplex is a convex hull of points or an intersection of positive half-spaces)



Each <m>n</m>-simplex is bounded by <term>codimension one faces</term>, or <m>(n-1)</m>-simplices lying in different <m>(n-1)</m>-dimensional affine spaces. Similarly, we can define codimension <m>k</m> faces to be <m>(n-k)</m>-dimensional simplices.

(picture: line segment with the codimension one faces)

(picture: triangle with labeled codimension one faces)

(picture: tetrahedron with labeled codimension one and codimension two faces)

The problems we want to solve naturally involve points in (scaled) simplices, so we need to agree on ways to describe coordinates and other features within a simplex.

We will use <term>convex coordinates</m>, denoted <m>(a \, : \, b \, : c)</m>, to describe the point on the simplex with traditional coordinates(traditional coordinates).

(intuitive definition of barycenter)

--
