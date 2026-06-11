# EDITORIAL REVIEW: COURSE NOTES PACING AND CONTENT ASSESSMENT

**Date:** May 28, 2026  
**Course:** MATH 260 - Applied Mathematics in Society  
**Review Period:** Week 1 (Intro) through Week 13 (AI/Algorithms)  
**Time Frame:** 16-week course, 3 hours/week total (2 lectures + 1 lab)

---

## EXECUTIVE SUMMARY

The course notes show **significant imbalance** across units:

| Unit | Weeks | Hours | Current Lines | Assessment |
|------|-------|-------|----------------|------------|
| Intro (M3 Framework) | 1 | 3 | 612 | **ADEQUATE** |
| Healthcare (DE Models) | 2.5 | 7.5 | 180 | **SEVERELY UNDER-RESOURCED** |
| Apportionment | 2.5 | 7.5 | 3071+1480 | **OVER-RESOURCED** |
| Districting | 2.5 | 7.5 | 785 | **ADEQUATE** |
| Data/AI/PCA | 2.5 | 7.5 | 468 | **UNDER-RESOURCED** |
| Content Moderation | 2.5 | 7.5 | 138 | **SEVERELY UNDER-RESOURCED** |

**Overall Recommendation:** Consolidate apportionment content, expand healthcare and content moderation sections.

---

## DETAILED UNIT ANALYSIS

### UNIT 1: INTRODUCTION TO MATHEMATICAL MODELING (Week 1, 3 hours)

**Files:**
- `00-modeling-framework.ptx` (118 lines)
- `001-modeling.ptx` (236 lines)
- `002-modeling.ptx` (258 lines)
- **Total: 612 lines**

**Content Assessment:**
- ✅ Clear exposition of SIAM M3 six-step process
- ✅ Real governance context (medication approval example)
- ✅ Appropriate for introductory framing
- ⚠️ Minor: Could include visual flowchart of M3 process
- ⚠️ Minor: Might benefit from 2-3 additional governance examples

**Pacing:** **APPROPRIATE** for 3-hour introduction.

**Recommendation:** Leave core content as is. Consider adding:
1. Quick reference checklist for M3 steps
2. 1-2 additional governance examples (voting, healthcare access, data)
3. Flowchart diagram showing problem → model → decision flow

---

### UNIT 2: HEALTHCARE AND PHARMACOKINETICS (Weeks 2-4, 7.5 hours)

**Files:**
- `02-de-crash-course.ptx` (180 lines)

**Content Assessment:**
- ✅ Clear exposition of differential equations concepts
- ✅ Covers exponential decay, equilibrium, repeated dosing, linear systems
- ✅ Mathematical concepts are rigorous
- ❌ **CRITICALLY SHORT**: Only ~180 lines for 7.5 hours of instruction
- ❌ Missing: Governance/policy context for healthcare decisions
- ❌ Missing: Real-world case studies (hormone therapy, antibiotics, chemotherapy dosing)
- ❌ Missing: Worked examples with real drug pharmacokinetics
- ❌ Missing: Discussion of equity across patient populations (age, weight, kidney/liver function)
- ❌ Missing: Connection to healthcare policy (FDA approval, access interruptions)

**What's Missing:**
1. **Motivating Examples** (3-5 detailed case studies):
   - Hormone therapy dosing and access equity
   - Antibiotic dosing in infections
   - Chemotherapy protocols for different patient groups
   - Impact of insurance coverage on adherence

2. **Extended DE Examples**:
   - Two-compartment models (blood vs. tissue)
   - Drug interactions (two DEs coupled)
   - Age-dependent elimination (children, elderly)

3. **Policy/Governance Section**:
   - How regulators use pharmacokinetics to set dosing guidelines
   - Role of FDA in drug approval and monitoring
   - Access equity: what happens when patients interrupt therapy?
   - International comparison: how different countries approach dosing policy

4. **Worked Problems**:
   - Numerical examples with real drugs and parameters
   - Spreadsheet simulations of dosing schedules
   - Visualization of concentration over weeks/months

**Pacing Issue:** Currently condensed; needs ~1200-1500 lines to fill 7.5 hours properly.

**Recommendation:** 
- **EXPAND significantly** to at least 1000-1200 lines
- Add 3-4 detailed governance case studies
- Include 5-8 worked examples with real pharmacokinetics data
- Create connection between DEs and clinical decision-making
- Address equity questions: how dosing differs across patient groups

**Priority:** HIGH - This unit is foundation for understanding repeated systems and policy trade-offs

---

### UNIT 3: APPORTIONMENT (Weeks 5-7, 7.5 hours)

**Files:**
- `00-apportionment.ptx` (3071 lines) - **EXTENSIVE**
- `00-alt-apport.ptx` (1480 lines) - **EXTENSIVE**
- **Total: 4551 lines**

**Content Assessment:**
- ✅ Comprehensive coverage of divisor methods, fairness criteria
- ✅ Clear definitions and examples
- ✅ Good governance framing (Montana paradox, representation)
- ❌ **SEVERELY OVER-RESOURCED**: 4551 lines for 7.5 hours
- ⚠️ Unclear structure: duplicate content across two files (apportionment + alt-apport)
- ⚠️ Some sections are redundant or could be condensed

**Issues:**
1. **Structure**: Why two files? Is `00-alt-apport.ptx` an earlier draft or alternative approach? If alternative approaches, should be clearly marked as "optional deeper dive"
2. **Length**: 4551 lines is 6x the appropriate length (should be ~750 lines for 7.5 hours)
3. **Organization**: Some content appears repetitive

**Recommendation:**
- **CONSOLIDATE**: Merge the two files, eliminating redundancy
- **TARGET LENGTH**: Reduce to 800-1000 lines
- **Keep**: Fairness criteria, divisor methods, governance framing
- **Consolidate**: Examples of paradoxes (Hamilton, Jefferson, Alabama)
- **Move to appendix or resources**: Historical notes, exhaustive comparisons of all methods
- **ACTION**: Review both files for duplication and consolidate to single, streamlined version

**Priority:** MEDIUM - Unit is well-covered but needs consolidation to make room for other units

---

### UNIT 4: DISTRICTING (Weeks 8-10, 7.5 hours)

**Files:**
- `02-districting.ptx` (785 lines)

**Content Assessment:**
- ✅ Clear exposition of gerrymandering
- ✅ Includes graph theory foundations
- ✅ Real case study reference (LULAC v. Perry)
- ✅ Math concepts are rigorous
- ⚠️ Moderate length (785 lines)
- ⚠️ Could include more on efficiency gap calculation
- ⚠️ Could expand on voting rights and equal protection law

**Pacing:** **APPROPRIATE** for 7.5 hours, though could be expanded slightly.

**Potential Expansions (Optional):**
1. More detailed worked examples of compactness measures (Polsby-Popper, Reock score)
2. Efficiency gap calculations on real data
3. Connection to Supreme Court decisions (Shaw v. Reno, Rucho v. COMMON CAUSE)
4. Practical redistricting challenge: balancing multiple fairness criteria

**Recommendation:**
- Keep current content as core
- Consider expanding to 1000-1100 lines with:
  - 2-3 additional worked examples on compactness
  - Practical case study (e.g., Texas 2020 redistricting, North Carolina efficiency gap litigation)
  - Algorithm sketch for automated redistricting

**Priority:** LOW - Unit is well-balanced; improvements are optional

---

### UNIT 5: DATA GOVERNANCE AND DIMENSIONALITY REDUCTION (Weeks 11-13, 7.5 hours)

**Files:**
- `01-dimensionality.ptx` (468 lines) - Data governance introduction
- `05-content-moderation.ptx` (138 lines) - Content moderation (classification/fairness)
- **Total: 606 lines**

**Content Assessment:**

#### Dimensionality Reduction (`01-dimensionality.ptx`, 468 lines):
- ✅ Governance framing: data supply chain, LLM training
- ✅ Ethical emphasis on AI labor and working conditions
- ✅ Real references (Pulitzer Center investigation)
- ⚠️ Lacks mathematical depth on PCA
- ⚠️ Missing: covariance matrices, eigenvalues, projections
- ⚠️ Missing: t-SNE, UMAP, other modern dimensionality reduction
- ⚠️ Missing: worked numerical examples

#### Content Moderation (`05-content-moderation.ptx`, 138 lines):
- ✅ Confusion matrix definition
- ✅ Fairness metrics (precision, recall, demographic parity, equal opportunity)
- ✅ Real case reference (Meta Oversight Board, EU DSA)
- ❌ **CRITICALLY SHORT**: Only 138 lines for 2.5 weeks
- ❌ Missing: detailed worked examples
- ❌ Missing: numerical exercises on precision/recall trade-offs
- ❌ Missing: discussion of thresholding and ROC curves
- ❌ Missing: application to real moderation scenarios

**Issues:**
1. **Imbalance**: Dimensionality reduction has labor/ethics focus but lacks math. Content moderation has math but lacks depth.
2. **Coverage**: Combined 606 lines for 7.5 hours is tight; should be 1000-1200 lines
3. **Missing**: Connection between dimensionality reduction (what we can/cannot see) and fairness in classification

**Recommendation:**
- **EXPAND dimensionality section** with:
  - PCA mathematics (covariance, eigenvectors)
  - Worked numerical examples
  - Connection to t-SNE and UMAP for visualization
  - How feature selection affects downstream fairness

- **EXPAND content moderation section** with:
  - 4-5 detailed worked examples (confusion matrices, precision/recall calculations)
  - Threshold tuning and ROC curves
  - Real-world scenario: should a platform optimize for precision or recall?
  - Group fairness: how to measure and achieve demographic parity

- **ADD bridge section**:
  - How do data collection choices affect classification fairness?
  - Case study: hiring algorithms and gender bias
  - Case study: predictive policing and racial bias

**Target Length**: Expand to 1100-1300 lines (from current 606)

**Priority:** HIGH - Unit needs significant expansion to cover both PCA and fairness in classification with depth

---

## SUMMARY OF ACTIONS

### IMMEDIATE PRIORITIES (Do First):

1. **EXPAND Healthcare Unit** (Priority: HIGH)
   - Current: 180 lines
   - Target: 1200-1500 lines
   - Action: Add governance context, case studies, worked examples, equity considerations
   - Rationale: Foundation for repeated systems, policy trade-offs

2. **EXPAND Data/AI Unit** (Priority: HIGH)
   - Current: 606 lines (468 + 138)
   - Target: 1100-1300 lines
   - Action: Deepen PCA math, expand moderation section, add bridge/fairness section
   - Rationale: Unit covers two topics that must be better integrated

3. **CONSOLIDATE Apportionment Unit** (Priority: MEDIUM)
   - Current: 4551 lines (3071 + 1480)
   - Target: 800-1000 lines
   - Action: Merge two files, eliminate redundancy, move optional content to appendix
   - Rationale: Free up space, clarify structure, reduce student cognitive load

4. **MINOR ENHANCEMENTS** (Priority: LOW)
   - Intro Unit: Add flowchart, 1-2 additional examples (should grow from 612 → 700 lines)
   - Districting Unit: Add 1-2 case studies, expand compactness examples (grow from 785 → 1000 lines)

### TIMELINE:
- Healthcare expansion: 3-4 days
- Data/AI expansion: 3-4 days
- Apportionment consolidation: 1-2 days
- Minor enhancements: 1 day

### CONTENT SOURCING:
- Healthcare: Use journal articles on gender-affirming care, antibiotic dosing, cancer treatment
- Data/AI: Use content moderation case studies, fairness literature, Pulitzer Center materials
- Apportionment: Review existing literature for edge cases, historical notes

---

## EDITORIAL NOTES FOR INDIVIDUAL FILES

### `02-de-crash-course.ptx`
**Status:** NEEDS MAJOR EXPANSION  
**Comments to add in file:**
```xml
<!-- EDITORIAL NOTE: This section covers the mathematical foundations of DEs.
     NEEDED: Significant expansion with governance context, case studies, and worked examples.
     Current length (180 lines) is appropriate for a 2-hour math refresher but insufficient 
     for a 7.5-hour unit. 
     
     MISSING SECTIONS:
     1. Healthcare policy context and case studies (hormone therapy, antibiotics, chemotherapy)
     2. Real drug pharmacokinetics with numerical examples
     3. Equity considerations: how dosing differs across populations
     4. FDA approval and regulatory decision-making
     5. Impact of access interruptions on patient outcomes
     
     TARGET: Expand to 1200-1500 lines with 3-4 governance case studies and 8-10 worked examples.
-->
```

### `00-apportionment.ptx` and `00-alt-apport.ptx`
**Status:** NEEDS CONSOLIDATION  
**Comments to add:**
```xml
<!-- EDITORIAL NOTE: This section is substantially over-resourced at 4551 combined lines for 7.5 hours.
     ACTION REQUIRED: Merge with 00-alt-apport.ptx, eliminating redundancy.
     Target final length: 800-1000 lines (currently ~600% of appropriate size).
     
     CONSOLIDATION STRATEGY:
     - Keep core divisor methods and fairness criteria
     - Combine worked examples, eliminating duplicates
     - Move exhaustive method comparisons to appendix
     - Keep governance framing (Montana, representation questions)
     
     Recommended merging: See companion file 00-apportionment-consolidated-draft.ptx
-->
```

### `01-dimensionality.ptx`
**Status:** NEEDS EXPANSION AND MATH DEPTH  
**Comments to add:**
```xml
<!-- EDITORIAL NOTE: Strong governance and ethics framing, but lacking mathematical depth.
     Current section emphasizes AI labor and data supply chain (good!), but needs:
     - PCA mathematics: covariance, eigenvalues, projections
     - Numerical worked examples
     - Connection to t-SNE, UMAP
     - Bridge to fairness in classification (how feature selection affects downstream bias)
     
     MISSING CONTENT:
     1. Principal Component Analysis mathematics and interpretation
     2. Worked examples: calculating PCA on real data
     3. Visualization: biplots, variance explained plots
     4. Modern methods: t-SNE, UMAP for non-linear reduction
     5. Governance case study: how data collection choices affect algorithmic fairness
     
     Current length: 468 lines; Target: 600-750 lines for this section
     (Combined with content moderation: 1100-1300 lines total for 7.5-hour unit)
-->
```

### `05-content-moderation.ptx`
**Status:** CRITICALLY UNDER-RESOURCED  
**Comments to add:**
```xml
<!-- EDITORIAL NOTE: Section covers important fairness concepts but lacks depth and worked examples.
     At 138 lines for ~2.5 weeks, this is severely under-resourced.
     
     MISSING CONTENT:
     1. Detailed worked examples on precision/recall trade-offs (5-8 examples with numbers)
     2. ROC curves and threshold tuning
     3. Group fairness calculations (demographic parity, equal opportunity)
     4. Real-world scenario analysis: how should platforms balance false positives vs false negatives?
     5. Case studies: hiring algorithms, predictive policing, content moderation
     6. Discussion of impossible tradeoffs (e.g., demographic parity + equal opportunity)
     
     TARGET: Expand to 400-500 lines for this section
     (Combined with dimensionality reduction: 1100-1300 lines total for 7.5-hour unit)
-->
```

---

## NOTES ON INTEGRATION

The new interactive Jupyter notebooks (Lab 1: Half-Lives, Lab 2: PCA) provide **excellent computational support** for the healthcare and data/AI units:

- **Lab 1 (Half-Lives)** implements exponential decay and repeated dosing
- **Lab 2 (PCA)** implements dimensionality reduction with covariance and eigendecomposition

**Recommendation:** When expanding course notes, refer students to notebooks for computational examples and visualization. Notes should focus on governance context, mathematical intuition, and policy implications; labs should provide the computational implementation.

---

## FINAL ASSESSMENT

| Unit | Current Status | Action | Priority |
|------|---|---|---|
| Intro | ✅ Adequate | Minor enhancements | LOW |
| Healthcare | ❌ Severely under-resourced | Major expansion | HIGH |
| Apportionment | ⚠️ Over-resourced | Consolidate | MEDIUM |
| Districting | ✅ Adequate | Optional expansion | LOW |
| Data/AI | ❌ Under-resourced | Major expansion | HIGH |

**Overall Course Health:** Imbalanced; needs reallocation of content from apportionment to healthcare and data/AI units.

---

*Prepared by: Course Development Team*  
*Review Date: May 28, 2026*  
*Next Review: After content expansion complete*
