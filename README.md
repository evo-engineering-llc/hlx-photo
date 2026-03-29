# HLX Photo Reconstruction

Deterministic image reconstruction using constraint-based convergence.

---

## What it does

* Reconstructs missing regions in images
* Preserves structural coherence
* Produces consistent results across inputs
* No training, no models, no randomness

---

## Example Results

### Example 1

**Original**
![original](showcase/example1/original.jpg)

**Corrupted**
![corrupted](showcase/example1/corrupted.jpg)

**Reconstructed**
![reconstructed](showcase/example1/reconstructed.jpg)

**Diff (difference from original)**
![diff](showcase/example1/diff.jpg)

---

### Example 2

**Original**
![original](showcase/example2/original.jpg)

**Corrupted**
![corrupted](showcase/example2/corrupted.jpg)

**Reconstructed**
![reconstructed](showcase/example2/reconstructed.jpg)

**Diff**
![diff](showcase/example2/diff.jpg)

---

### Example 3

**Original**
![original](showcase/example3/original.jpg)

**Corrupted**
![corrupted](showcase/example3/corrupted.jpg)

**Reconstructed**
![reconstructed](showcase/example3/reconstructed.jpg)

**Diff**
![diff](showcase/example3/diff.jpg)

---

### Example 4

**Original**
![original](showcase/example4/original.jpg)

**Corrupted**
![corrupted](showcase/example4/corrupted.jpg)

**Reconstructed**
![reconstructed](showcase/example4/reconstructed.jpg)

**Diff**
![diff](showcase/example4/diff.jpg)

---

### Example 5

**Original**
![original](showcase/example5/original.jpg)

**Corrupted**
![corrupted](showcase/example5/corrupted.jpg)

**Reconstructed**
![reconstructed](showcase/example5/reconstructed.jpg)

**Diff**
![diff](showcase/example5/diff.jpg)

---

## Notes

* Diff images are intentionally low magnitude — this indicates high reconstruction accuracy
* System is fully deterministic
* Reconstruction is achieved via iterative constraint enforcement, not generative prediction

---

## Run

```bash
python run.py
```

---

## Summary

This system reconstructs structure by iteratively eliminating inconsistent states until a stable solution remains.
