import sys
from importlib import metadata


def check_dependencies() -> None:
    REQUIRED = {
        "pandas": "Data manipulation ready",
        "numpy": "Numerical computation ready",
        "requests": "Network access ready",
        "matplotlib": "Visualization ready",
    }
    print("Checking dependencies:")
    missing = []

    for packet, msg in REQUIRED.items():
        try:
            version = metadata.version(packet)
            print(f"[OK] {packet} ({version}) - {msg}")
        except metadata.PackageNotFoundError:
            print(f"[MISSING] {packet} - required for: {msg}")
            missing.append(packet)

    return missing


def generate_matrix_data(np, n_points=1000):
    rng = np.random.default_rng(seed=42)
    return {
        "signal": rng.normal(loc=0.0, scale=1.0, size=n_points),
        "noise": rng.uniform(-1.0, 1.0, size=n_points),
        "glitch": rng.poisson(lam=3.0, size=n_points),
    }


def fetch_external_data(np):
    try:
        import requests

        url = "https://jsonplaceholder.typicode.com/posts"
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        raw = response.json()

        n_points = len(raw)
        title_lengths = [len(post.get("title", "")) for post in raw]

        return {
            "signal": np.array(title_lengths, dtype=float),
            "noise": np.random.uniform(-1.0, 1.0, size=n_points),
            "glitch": np.array([post.get("userId", 0) for post in raw]),
        }
    except Exception:
        return None


def analyze(pd, np, api=False):
    print("\nAnalyzing Matrix data...")
    data_obj = None

    if api:
        api_data = fetch_external_data(np)
        if api_data is not None:
            data_obj = pd.DataFrame(api_data)

    if data_obj is None:
        api_data = generate_matrix_data(np, n_points=1000)
        data_obj = pd.DataFrame(api_data)

    print(f"Processing {len(data_obj)} data points...")
    return data_obj


def create_graph(df, grapg):
    print("Generating visualization...")

    grapg.figure(figsize=(8, 4))
    grapg.plot(df["signal"], label="signal")
    grapg.plot(df["noise"], label="noise", alpha=0.6)
    grapg.title("Matrix Data Analysis")
    grapg.xlabel("Index")
    grapg.ylabel("Value")
    grapg.legend()
    grapg.tight_layout()
    grapg.savefig("matrix_analysis.png")


def main():
    print("LOADING STATUS: Loading programs...")

    missing = check_dependencies()

    if missing:
        print("\nMissing dependencies:", ", ".join(missing))
        print("\nInstall with pip:")
        print("  pip install -r requirements.txt")
        print("\nInstall with Poetry:")
        print("  poetry install")
        sys.exit(1)

    import matplotlib
    import numpy as np
    import pandas as pd

    matplotlib.use("Agg")
    import matplotlib.pyplot as grapg

    api = "--api" in sys.argv

    df = analyze(pd, np, api=api)
    create_graph(df, grapg)

    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    main()