import pandas as pd
import glob

files = sorted(glob.glob("prisoners_dilemma_notes*.csv"))

if not files:
    print("No result files found.")
    exit(1)

print(f"Found {len(files)} result file(s)\n")

for f in files:
    df = pd.read_csv(f)
    model = df['model'].iloc[0] if 'model' in df.columns else "unknown"
    n_prompts = df['prompt'].nunique()
    n_rows = len(df)
    confess_rate = (df['choice'] == "Confess").mean()

    print(f"File: {f}")
    print(f"  Model: {model}")
    print(f"  Rows: {n_rows} | Unique prompts: {n_prompts}")
    print(f"  Confession rate: {confess_rate:.1%}\n")
