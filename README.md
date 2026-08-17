# Code Cultivation — Python OOP @ 42 Antananarivo

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Python: 3.8+](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Code style: PEP 8](https://img.shields.io/badge/code%20style-PEP%208-green.svg)

A comprehensive, **progressive learning curriculum** for mastering Object-Oriented Programming (OOP) in Python. This repository contains modular exercises spanning **7 learning phases (P0–P7)**, designed to build a solid foundation in software design, encapsulation, inheritance, polymorphism, data processing patterns, and testing.

## 📚 Overview

**Code Cultivation** is structured as a **learning journey**, not a collection of one-off scripts. Each module introduces new OOP concepts and design patterns, culminating in sophisticated projects like data stream processing systems and plugin architectures.

**Key features:**
- ✅ Progressive difficulty: beginner to intermediate OOP
- ✅ Real-world design patterns: factories, adapters, pipelines, abstract base classes
- ✅ Type-safe: comprehensive type hints throughout (PEP 484)
- ✅ Industry standards: PEP 8 compliance, mypy/flake8 validated
- ✅ Self-contained: Python standard library only—no external dependencies

---

## 🗂️ Learning Path

```
P0/         # Fundamentals: I/O, variables, control flow
            # Exercises: hello world, input/output, basic arithmetic
            
P1/         # Functions & scope: function definition, parameters, return values
            # Exercises: custom functions, lambda functions, map/filter/reduce patterns
            
P2/         # Custom exceptions & error handling
            # Exercises: exception hierarchies, error validation, custom error types
            
P3/         # CLI tooling & data analytics
            # Exercises: argument parsing, file I/O, statistics, decorators
            
P4/         # File streams & transformation pipelines
            # Exercises: file manipulation, stream processing, buffering strategies
            
P5/         # Polymorphic data processors & plugin architecture
            # Exercises: abstract base classes, data validation, stream orchestration
            # HIGHLIGHT: `DataStream` class manages multiple processor types with
            #            export plugins (CSV, JSON, custom)
            
P6/         # Package structure & module organization
            # Exercises: `__init__.py` patterns, package imports, namespace management
            
P7/         # (Extensible for advanced topics)
```

---

## 🚀 Quick Start

### Prerequisites
- **Python 3.8 or later** (3.10+ recommended)
- No external packages required

### Clone & Explore

```bash
# Clone the repository
git clone https://github.com/deep-awak/code-cultivation-poo.git
cd code-cultivation-poo

# Run a simple exercise (P0)
python3 P0/ex0/ft_hello_garden.py

# Run an intermediate exercise (P3)
python3 P3/ex0/ft_command_quest.py arg1 arg2 arg3

# Run an advanced exercise (P5)
python3 P5/ex0/data_processor.py

# Run module-level exercises
python3 -m P5.ex0.data_processor
python3 -m P5.ex1.data_stream
```

---

## 📖 Module Highlights

### **P0 & P1: Foundations**
Simple function-based exercises introducing variables, control flow, and custom functions.

| Exercise | Topic |
|----------|-------|
| `ex0/ft_hello_garden.py` | Hello world |
| `ex1/ft_garden_name.py` | Input/output |
| `ex2/ft_plot_area.py` | Math operations |
| `ex6/ft_count_harvest_iterative.py` | Loops |

### **P2: Error Handling**
Custom exception hierarchies and validation patterns.

```python
# Example: P2/ex3/ft_custom_errors.py
class GardenError(Exception): ...
class PlantError(GardenError): ...
class WaterError(GardenError): ...

try:
    if days_since_watered > 2:
        raise PlantError("Wilting!")
except GardenError as e:
    print(f"Caught: {e}")
```

### **P3: CLI & Analytics**
Argument parsing, file operations, and data aggregation.

```python
# Example: P3/ex1/ft_score_analytics.py
# Accepts command-line scores, computes min/max/mean
python3 P3/ex1/ft_score_analytics.py 85 90 78 92
```

### **P4: Stream Processing**
File I/O and transformation pipelines with character/line buffering.

### **P5: Polymorphic Processors (★ Core)**
Abstract base classes, type validation, and plugin architecture.

```python
# Example: P5/ex0/data_processor.py & P5/ex1/data_stream.py
class DataProcessor(ABC):
    @abstractmethod
    def validate(self, data: Any) -> bool: ...
    @abstractmethod
    def ingest(self, data: Any) -> None: ...

class NumericProcessor(DataProcessor): ...
class TextProcessor(DataProcessor): ...
class LogProcessor(DataProcessor): ...

# Stream orchestration
stream = DataStream()
stream.register_processor(NumericProcessor())
stream.register_processor(TextProcessor())
stream.process_stream(batch_data)
stream.output_pipeline(n_items, CSVExportPlugin())
```

### **P6: Package Architecture**
Proper Python package structure with `__init__.py`, namespace management, and nested module imports.

```python
# P6 demonstrates:
# - Direct file imports: import alchemy.elements
# - Package re-exports: from alchemy import strength_potion
# - Nested package access: import alchemy.transmutation.recipes
```

---

## 💡 Code Quality

All code follows strict standards:

### **PEP 8 Compliance**
```bash
# Format with black
black .

# Check with flake8
flake8 .

# Type-check with mypy
mypy .
```

### **Type Hints**
Every function includes full type annotations:

```python
def parse_scores(args: list[str]) -> list[int]:
    """Parse comma-separated or space-separated scores."""
    return [int(score) for score in args]

def display_stats(scores: list[int]) -> None:
    """Print min, max, mean, and variance."""
    if not scores:
        return
    print(f"Min: {min(scores)}, Max: {max(scores)}, Mean: {sum(scores)/len(scores):.2f}")
```

---

## 📝 Exercise Organization

Each exercise is **self-contained** and **executable**:

```
P3/
├── ex0/
│   └── ft_command_quest.py        # Prints sys.argv
├── ex1/
│   └── ft_score_analytics.py      # CLI score processor
├── ex5/
│   └── ft_data_stream.py          # Data stream demo
└── module3.pdf                     # Official assignment
```

Run any exercise:
```bash
python3 P3/ex0/ft_command_quest.py arg1 arg2
python3 P5/ex0/data_processor.py
python3 -m P5.ex1.data_stream
```

---

## 🛠️ Development Setup

### Optional Tools
While **not required**, these tools help validate code locally:

```bash
# Install dev tools (optional)
pip install black flake8 mypy

# Format all code
black .

# Lint all files
flake8 . --max-line-length=88

# Type-check all files
mypy .
```

### Running Tests
(Note: Some exercises include inline tests via `if __name__ == "__main__"`)

```bash
python3 P2/ex3/ft_custom_errors.py     # Runs built-in demo
python3 P5/ex0/data_processor.py       # Runs interactive demo
```

---

## 📄 License

This project is licensed under the **MIT License** — see [LICENSE](./LICENSE) for details.

Copyright © 2026 Mahery RAZAFIMANANTSOA

---

## 🤝 Contributing

This is primarily a **personal learning and teaching workspace**. To contribute:

1. **Fork** the repository
2. **Create a branch** for your exercise or improvement
3. **Keep changes focused**: one exercise per pull request
4. **Include documentation**: 
   - Brief README inside the exercise folder (if non-trivial)
   - Type hints and docstrings
5. **Validate code quality**:
   ```bash
   black <files>
   flake8 <files>
   mypy <files>
   ```
5. **Submit a pull request** with a clear description

---

## 📞 Questions & Support

- **Official Subjects**: See `P0/en.subject.pdf`, `P1/en.subject.pdf`, `P3/module3.pdf`
- **Project Homepage**: [42 Antananarivo](https://42antananarivo.mg/)
- **42 Network**: [42 School](https://42.fr/)

---

## 🌿 Philosophy

> "Code Cultivation" embodies the idea that learning OOP is like gardening: it requires patience, consistent practice, progressive challenges, and solid foundational knowledge before moving to complex structures. Each module builds on the last, just as plants grow through seasons.

Happy coding! 🌱
