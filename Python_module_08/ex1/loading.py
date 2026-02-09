import sys
import importlib.metadata
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def check_dependencies() -> bool:
    """
    Checks if required packages are installed and prints their versions.
    Returns True if all satisfied, False otherwise.
    """
    required = ["pandas", "numpy", "matplotlib", "requests"]
    all_available = True

    print("Checking dependencies:")
    for package in required:
        try:
            version = importlib.metadata.version(package)
            # خط زیر برای رعایت محدودیت ۷۹ کاراکتر شکسته شده است
            msg = f"[OK] {package} ({version}) - Ready for Zion"
            print(msg)
        except importlib.metadata.PackageNotFoundError:
            print(
                f"[MISSING] {package} - Run 'pip install -r requirements.txt'"
            )
            all_available = False
    return all_available


def analyze_matrix_data() -> None:
    """
    Simulates Matrix data analysis and generates a visualization.
    """
    try:
        print("\nAnalyzing Matrix data...")
        # Simulate 1000 data points of Sentinel positions
        data = {
            'Sentinels': np.random.normal(50, 15, 1000),
            'Agents': np.random.uniform(0, 100, 1000)
        }
        df = pd.DataFrame(data)

        print(f"Processing {len(df)} data points...")

        # Create a visualization
        plt.figure(figsize=(10, 6))
        plt.hist(df['Sentinels'], bins=30, color='green', alpha=0.7)
        plt.title('Sentinel Density Distribution - Zion Perimeter')
        plt.xlabel('Proximity to Zion')
        plt.ylabel('Count')

        output_file = "matrix_analysis.png"
        plt.savefig(output_file)
        print("Analysis complete!")
        print(f"Results saved to: {output_file}")

    except Exception as e:
        print(f"ERROR: Data corruption during analysis: {e}")


def main() -> None:
    """
    Entry point for the loading program.
    """
    print("LOADING STATUS: Loading programs...")

    if check_dependencies():
        analyze_matrix_data()
    else:
        print("\nFATAL: System incomplete. Load missing programs first.")
        sys.exit(1)


if __name__ == "__main__":
    main()
