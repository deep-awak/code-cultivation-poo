#!/usr/bin/env python3

import importlib
import importlib.util
import sys
from types import ModuleType
from typing import TYPE_CHECKING, Dict, Optional, Tuple

if TYPE_CHECKING:
    import pandas as pd

REQUIRED_PACKAGES: Tuple[str, ...] = ("pandas", "numpy", "matplotlib")
OPTIONAL_PACKAGES: Tuple[str, ...] = ("requests",)

DESCRIPTIONS: Dict[str, str] = {
    "pandas": "Data manipulation ready",
    "numpy": "Numerical computation ready",
    "requests": "Network access ready",
    "matplotlib": "Visualization ready",
}

DATA_POINTS = 1000
OUTPUT_FILE = "matrix_analysis.png"


def load_module(name: str) -> Optional[ModuleType]:
    if importlib.util.find_spec(name) is None:
        return None
    try:
        return importlib.import_module(name)
    except ImportError:
        return None


def get_version(module: Optional[ModuleType]) -> str:
    if module is None:
        return "unknown"
    return str(getattr(module, "__version__", "unknown"))


def check_dependencies() -> Dict[str, Optional[ModuleType]]:
    print("Checking dependencies:")
    modules: Dict[str, Optional[ModuleType]] = {}
    for name in REQUIRED_PACKAGES:
        module = load_module(name)
        modules[name] = module
        status = "OK" if module else "MISSING"
        version = get_version(module) if module else "not installed"
        desc = DESCRIPTIONS.get(name, "")
        print(f"[{status}] {name} ({version}) - {desc}")

    for name in OPTIONAL_PACKAGES:
        module = load_module(name)
        modules[name] = module
        if module:
            desc = DESCRIPTIONS.get(name, "")
            print(f"[OK] {name} ({get_version(module)}) - {desc}")
    print()
    return modules


def show_missing_instructions(missing: Tuple[str, ...]) -> None:
    print("ERROR: Missing required dependencies:", ", ".join(missing))
    print()
    print("Install with pip:")
    print("    pip install -r requirements.txt")
    print()
    print("Install with Poetry:")
    print("    poetry install")
    print("    poetry run python loading.py")


def generate_matrix_data(
    np_module: ModuleType, pd_module: ModuleType
) -> "pd.DataFrame":
    rng = np_module.random.default_rng(seed=42)
    digital_rain = rng.normal(loc=50, scale=15, size=DATA_POINTS)
    glitch_intensity = rng.exponential(scale=2.0, size=DATA_POINTS)
    agent_proximity = rng.uniform(low=0, high=100, size=DATA_POINTS)

    frame = pd_module.DataFrame(
        {
            "digital_rain": digital_rain,
            "glitch_intensity": glitch_intensity,
            "agent_proximity": agent_proximity,
        }
    )
    return frame


def analyze_data(frame: "pd.DataFrame") -> "pd.DataFrame":
    return frame.describe()


def visualize(frame: "pd.DataFrame", plt: ModuleType) -> None:
    fig, ax = plt.subplots(figsize=(8, 6))
    scatter = ax.scatter(
        frame["agent_proximity"],
        frame["glitch_intensity"],
        c=frame["digital_rain"],
        cmap="viridis",
        s=12,
        alpha=0.7,
    )
    ax.set_title("Matrix Environment: Glitch\
 vs Proximity & Rain", fontsize=12, pad=15)
    ax.set_xlabel("Agent Proximity")
    ax.set_ylabel("Glitch Intensity")
    cbar = fig.colorbar(scatter, ax=ax)
    cbar.set_label("Digital Rain Density")
    fig.tight_layout()
    fig.savefig(OUTPUT_FILE)
    plt.close(fig)


def main() -> None:
    print("LOADING STATUS: Loading programs...\n")

    modules = check_dependencies()
    missing = tuple(
        name for name in REQUIRED_PACKAGES if modules.get(name) is None
    )
    if missing:
        show_missing_instructions(missing)
        sys.exit(1)

    np_module = modules["numpy"]
    pd_module = modules["pandas"]
    plt_module = load_module("matplotlib.pyplot")
    if np_module is None or pd_module is None or plt_module is None:
        print("ERROR: Could not fully load required modules.")
        sys.exit(1)

    print("Analyzing Matrix data...")
    print(f"Processing {DATA_POINTS} data points...")
    frame = generate_matrix_data(np_module, pd_module)

    print("Generating visualization...")
    visualize(frame, plt_module)

    print("\nAnalysis complete!")
    print(f"Results saved to: {OUTPUT_FILE}\n")
    print()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrupted.")
        sys.exit(1)
    except Exception as error:
        print(f"Unexpected error while loading programs: {error}")
        sys.exit(1)
