Rocket Flight Prediction Model (Physics + Machine Learning)

## Overview

In this project, I built a physics-based rocket simulator and used it to generate a dataset for training a machine learning model that predicts maximum altitude.

The simulator models rocket motion using thrust, gravity, and aerodynamic drag. By running hundreds of simulations with different input parameters, I created a dataset that was then used to train a Random Forest regression model.

This project connects engineering simulation with data-driven prediction.

---

## Project Structure

- `rocket_simulator.py` → Physics-based rocket simulation  
- `generate_data.py` → Generates dataset using simulation  
- `rocket_data.csv` → Dataset of simulated flights  
- `train_model.py` → Trains machine learning model and evaluates performance  

---

## Key Features

- Physics-based rocket simulation (thrust, gravity, drag)  
- Custom dataset generation (no external data used)  
- Random Forest regression model  
- Feature importance analysis  
- Interactive prediction system  

---

## Technologies Used

- Python  
- NumPy  
- Pandas  
- Scikit-learn  
- Matplotlib  

---

## Model Approach

1. Simulate rocket flights using physics equations  
2. Generate dataset by varying:
   - mass  
   - thrust  
   - burn time  
3. Train a Random Forest model on generated data  
4. Predict maximum altitude from input parameters  

---

## Results

The model achieved a mean absolute error of approximately **7.6 meters**, indicating strong predictive accuracy.

Feature importance analysis showed that **mass had the greatest impact** on rocket performance, followed by thrust and burn time. This aligns with physical expectations, since higher mass reduces acceleration and limits altitude.

---

## Example Output

Run:

```bash
python train_model.py
