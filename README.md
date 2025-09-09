
# 🚶 Central Limit Theorem in Discrete Random Walks

This project demonstrates the **Central Limit Theorem (CLT)** by simulating 1D random walks and analyzing the distribution of walker positions.

---

## 📂 Code Structure
- **main.py** → random walk generator, histogram builder, variance calculator.

---

## 🔑 Important Variables
- `M` → number of walkers  
- `N` → number of steps per walker  
- `p` → probability of stepping right (default: 0.5 for unbiased walk)  

---

## ⚙️ How to Interact
1. Open **main.py**  
2. Modify `M` and `N` to simulate different ensemble sizes.  
3. Run:
   ```bash
   python main.py

---

## 🧠 Physical/Statistical Intuition

* Mean displacement:

  $$
  \langle x \rangle = 0
  $$

* Variance grows linearly with steps:

  $$
  \langle x^2 \rangle \sim N
  $$

* Distribution approaches Gaussian by CLT.

---

## 🧮 Numerical Models

* **Discrete random walk model**
* **Central Limit Theorem (CLT)**
* **Euler–Cromer step integration** for cumulative steps

```
