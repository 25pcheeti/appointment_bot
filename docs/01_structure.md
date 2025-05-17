## Project Structure

This document explains each top-level file and directory in the 
`appointment_bot` project, detailing their role within the overall data 
pipeline.

### 📄 LICENSE

* **Contents:** Open-source license text (MIT).
* **Pipeline role:** Declares usage rights and contribution terms.
* **Reason for separation:** Clearly defines legal conditions separately 
from code.

### 📄 Makefile

* **Contents:** Command shortcuts (e.g., `make data`, `make train`, `make 
test`).
* **Pipeline role:** Automates frequent tasks, ensuring workflow 
consistency.
* **Reason for separation:** Centralizes task management outside 
individual scripts.

### 📄 README.md

* **Contents:** Project overview, quickstart guide, and basic usage 
instructions.
* **Pipeline role:** Entry point documentation for users and contributors.
* **Reason for separation:** Provides clear, high-level information 
without code details.

### 📄 pyproject.toml

* **Contents:** Build system and package metadata (PEP 517/518 compliant).
* **Pipeline role:** Facilitates editable installs (`pip install -e .`) 
and dependency management.
* **Reason for separation:** Keeps build configuration distinct from 
source logic.

### 📄 environment.yml / requirements.txt

* **Contents:** Conda environment (`environment.yml`) and pip package 
dependencies (`requirements.txt`).
* **Pipeline role:** Ensures reproducible development and deployment 
environments.
* **Reason for separation:** Explicitly manages package dependencies and 
versions.

### 📄 setup.py

* **Contents:** Legacy package metadata and installation scripts.
* **Pipeline role:** Enables package installation and distribution via 
pip.
* **Reason for separation:** Maintains compatibility with traditional 
packaging tools.

### 📁 appointment\_bot.egg-info

* **Contents:** Automatically generated metadata from editable installs.
* **Pipeline role:** Stores metadata necessary for package installation.
* **Reason for separation:** Managed by tooling; not manually edited.

### 📁 data/

* **Subdirectories:**

  * `raw/` (original dataset downloads)
  * `interim/` (partially processed datasets)
  * `processed/` (fully cleaned data ready for modeling)
  * `external/` (third-party or reference datasets)
* **Pipeline role:** Tracks datasets through stages from acquisition to 
modeling.
* **Reason for separation:** Clarifies data sources, stages, and prevents 
accidental overwrites.

### 📁 notebooks/

* **Contents:** Jupyter notebooks for exploratory data analysis and 
prototyping.
* **Pipeline role:** Enables data exploration and visualization in a draft 
format.
* **Reason for separation:** Keeps experimental and exploratory work 
separate from production code.

### 📁 appointment\_bot/ (Python package)

* **Contents:** Core library modules and utilities:

  * `config.py` (configuration settings and logger setup)
  * `dataset.py`, `features.py`, `plots.py`
  * Subpackages: `features/`, `modeling/`
* **Pipeline role:** Provides reusable functions and classes.
* **Reason for separation:** Allows for organized imports and streamlined 
unit testing.

### 📁 src/

* **Contents:** Standalone scripts and CLI entry points:

  * `src/data/download_dataset.py`
  * `src/models/train_model.py`
  * `src/models/tune_models.py` (model hyperparameter tuning script)
* **Pipeline role:** Executes end-to-end data pipeline stages.
* **Reason for separation:** Distinctly separates runnable scripts from 
reusable library code.

### 📁 models/

* **Contents:** Stored trained model artifacts (e.g., `logreg.pkl`, 
`rf_tuned.pkl`).
* **Pipeline role:** Holds serialized model files for inference.
* **Reason for separation:** Keeps output artifacts distinct from source 
code.

### 📁 reports/

* **Subdirectories:**

  * `figures/` (plots, ROC curves, performance visualizations)
* **Pipeline role:** Contains visualization outputs for analysis and 
documentation.
* **Reason for separation:** Maintains clarity by isolating static 
outputs.

### 📁 docs/

* **Contents:** Project documentation and related files:

  * `00_project_background.md` (project context and goals)
  * `01_structure.md` (this document describing the structure)
  * Architecture descriptions and reflections.
* **Pipeline role:** Stores detailed documentation for project rationale 
and usage.
* **Reason for separation:** Keeps explanatory texts distinct from source 
code.

### 📁 references/

* **Contents:** Supplementary materials (academic papers, useful links, 
additional reading).
* **Pipeline role:** Provides reference background and supporting 
documents.
* **Reason for separation:** Prevents clutter in the main codebase.

### 📁 tests/

* **Contents:** Unit tests for project modules using `pytest`.
* **Pipeline role:** Validates the correctness and reliability of the 
pipeline components.
* **Reason for separation:** Clearly organizes test code for easy 
discovery and execution.

