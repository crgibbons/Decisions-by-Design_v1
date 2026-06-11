# Interactive Lab Notebooks

This directory contains Jupyter notebooks for hands-on computational labs in **MATH 260: Applied Mathematics in Society**.

## Quick Start

1. **Install dependencies** (first time only):
   ```bash
   pip install jupyter numpy matplotlib scipy pandas scikit-learn
   ```

2. **Start Jupyter**:
   ```bash
   jupyter notebook
   # or: jupyter lab
   ```

3. **Open a notebook** and run cells in order (Shift+Enter)

## Available Notebooks

### Lab 1: Medication Half-Lives and Exponential Decay
**File**: `01-halflives-interactive.ipynb`

- **Topics**: Differential equations, exponential decay, pharmacokinetics, half-life
- **Governance**: Gender-affirming hormone therapy, medication access, healthcare policy
- **Duration**: 60–90 minutes

**What you'll do:**
- Build a differential equation model: dH/dt = -kH
- Calculate elimination rate constants from half-life data
- Predict hormone concentrations after dose changes
- Explore repeated dosing schedules
- Reflect on healthcare equity implications

### Lab 2: Principal Component Analysis and Data Governance
**File**: `02-pca-data-governance.ipynb`

- **Topics**: Covariance matrices, eigendecomposition, PCA, dimensionality reduction
- **Governance**: Data collection bias, feature selection, algorithmic decision-making
- **Duration**: 60–90 minutes

**What you'll do:**
- Compute covariance matrices from neighborhood data
- Calculate eigenvectors and interpret principal components
- Project high-dimensional data into 2D for visualization
- Analyze what information is lost in dimensionality reduction
- Reflect on how data choices shape governance decisions

## Notebook Structure

Each notebook follows this pattern:

1. **Overview** — Learning goals and context
2. **Governance Context** — Why this matters for policy
3. **Exposition** — Theory with worked examples
4. **Code Examples** — Executed implementations with visualizations
5. **Student Exercises** — Problems for you to solve
6. **Follow-Up Exploration** — Open-ended investigations
7. **Governance Reflection** — Big-picture questions
8. **Report Generation** — Code to create a summary

## How to Use These Notebooks

### In Class (Lab Session)
1. Instructor walks through exposition sections
2. You run code cells and observe outputs
3. You work through student exercises (individually or in pairs)
4. Class discusses findings and governance implications

### Outside Class (Independent Study)
1. Work through notebook at your own pace
2. Try modifying code to answer follow-up questions
3. Write reflections on governance questions
4. Use the report-generation cell to create a PDF for submission

## Tips for Success

- **Run cells in order**: Each cell depends on variables defined earlier
- **Modify and experiment**: Change parameters, add visualizations, test hypotheses
- **Check output carefully**: Look at plots and printed results, not just the numbers
- **Ask questions**: If output is unexpected, that's often the most interesting part
- **Reflect deeply**: Governance questions aren't multiple-choice; write thoughtfully

## Troubleshooting

### "ModuleNotFoundError: No module named 'numpy'" (or other package)
```bash
pip install numpy matplotlib scipy pandas scikit-learn
```

### Code runs but produces no output
Make sure you're running the cell (Shift+Enter, not just Enter)

### Variable undefined errors
Restart the kernel (Kernel → Restart) and run all cells from the beginning

### Plots don't display
Add this to the first code cell:
```python
%matplotlib inline
```

## Submitting Your Work

1. **Save your notebook** with your name in the filename (e.g., `01-halflives-jsmith.ipynb`)
2. **Export to PDF** (File → Export As → PDF for cleaner submission) or submit the .ipynb file
3. **Include your reflections** in the designated markdown cells
4. **Use the report cell** to generate a summary document

## Additional Resources

- [Jupyter Notebook Documentation](https://jupyter-notebook.readthedocs.io/)
- [NumPy Quickstart](https://numpy.org/doc/stable/user/quickstart.html)
- [Matplotlib Tutorial](https://matplotlib.org/stable/tutorials/index.html)
- [Course Notes on Differential Equations](../notes/02-de-crash-course.ptx)
- [Course Notes on Data Governance](../notes/01-dimensionality.ptx)

## Questions?

Post to the course forum or attend office hours. Happy coding!
