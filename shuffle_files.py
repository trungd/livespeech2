import random
import sys
import os
import yaml

if __name__ == "__main__":
    subset = sys.argv[1]
    for fn in os.listdir(f"docs/assets/{subset}/enrollment_samples"):
        print(fn)
    d = []
    for i, fn in enumerate(random.choices([fn for fn in os.listdir(f"docs/assets/{subset}/enrollment_samples") if fn.endswith(".wav")], k=30)):
        models = [
            name for name in os.listdir(f"docs/assets/{subset}")
            if name not in ["enrollment_samples"] and not name.startswith(".")]
        random.shuffle(models)
        d.append({
            "id": str(i + 1),
            "enroll": f"./assets/{subset}/enrollment_samples/{fn}",
            "samples": [
                f"./assets/{subset}/{model}/{fn.replace('.enroll', '')}"
                for model in models
            ]})
    with open(f"docs/_data/samples_{subset}_shuffled_nmos.yml", "w") as fo:
        yaml.dump(d, fo)
