"""
Bluestock Mutual Fund Analytics
Master Pipeline Runner

Runs the main data pipeline scripts in sequence.
"""

import subprocess
import sys
from pathlib import Path


# Project root directory
PROJECT_ROOT = Path(__file__).resolve().parent.parent
SCRIPTS_DIR = PROJECT_ROOT / "scripts"


def run_script(script_name):
    """Run a Python script and stop if it fails."""
    script_path = SCRIPTS_DIR / script_name

    print(f"\n{'=' * 60}")
    print(f"Running: {script_name}")
    print(f"{'=' * 60}")

    result = subprocess.run(
        [sys.executable, str(script_path)],
        cwd=PROJECT_ROOT
    )

    if result.returncode != 0:
        raise RuntimeError(
            f"{script_name} failed with exit code {result.returncode}"
        )

    print(f"✓ Completed: {script_name}")


def main():
    """Run the complete Bluestock data pipeline."""

    pipeline_steps = [
        "data_ingestion.py",
        "clean_data.py",
        "create_db.py",
        "validate_amfi.py",
    ]

    print("\nBluestock Mutual Fund Analytics Pipeline")
    print("Starting pipeline...")

    try:
        for script in pipeline_steps:
            run_script(script)

        print("\n" + "=" * 60)
        print("✓ PIPELINE COMPLETED SUCCESSFULLY")
        print("=" * 60)

    except Exception as error:
        print("\n" + "=" * 60)
        print("✗ PIPELINE FAILED")
        print("=" * 60)
        print(f"Error: {error}")
        sys.exit(1)


if __name__ == "__main__":
    main()