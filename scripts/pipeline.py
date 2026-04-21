# scripts/pipeline.py

import subprocess


def run_step(script_name):
    print(f"Running {script_name}...")
    result = subprocess.run(
        ["python", f"scripts/{script_name}"],
        capture_output=True,
        text=True
    )

    print(result.stdout)

    if result.returncode != 0:
        print(result.stderr)
        raise Exception(f"Error running {script_name}")


def main():
    run_step("ingest.py")
    run_step("transform.py")
    run_step("load.py")

    print("Pipeline executed successfully!")


if __name__ == "__main__":
    main()