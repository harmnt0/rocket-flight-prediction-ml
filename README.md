# Rocket Flight Prediction Model (Physics + Machine Learning)

## Overview

In this project, I built a physics-based rocket simulator and used it to generate a dataset for training a machine learning model that predicts maximum altitude.

The simulator models rocket motion using thrust, gravity, and aerodynamic drag. By running hundreds of simulations with different input values, I created a dataset that was then used to train a Random Forest regression model.

This project connects engineering simulation with data-driven prediction and reflects how real-world systems are modeled before physical testing.
---

## Project Structure

- `rocket_simulator.py` → physics-based rocket simulation  
- `generate_data.py` → generates dataset using the simulator  
- `rocket_data.csv` → dataset of simulated rocket flights  
- `train_model.py` → trains and evaluates the machine learning model  

---

## Key Features

- Physics-based rocket simulation (thrust, gravity, drag)  
- Custom dataset generation (no external data used)  
- Random Forest regression model  
- Feature importance analysis  
- Interactive prediction input  

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
2. Generate a dataset by varying:
   - mass  
   - thrust  
   - burn time  
3. Train a Random Forest model on the generated data  
4. Predict maximum altitude from input values  

---

## Results

The model achieved a mean absolute error of about 7.6 meters, showing that it can predict rocket height with good accuracy.

Feature importance analysis showed that mass had the biggest impact on performance, followed by thrust and burn time. This lines up with the physics, since higher mass reduces acceleration and limits altitude.

---

## Example Output

Run:

```bash
python train_model.py
```

You will see:
- model error (MAE)  
- feature importance values  
- a graph comparing actual vs predicted values  
- an option to input your own values for prediction  

---

## How to Run

Install dependencies:
```bash
pip install numpy pandas scikit-learn matplotlib
```

Generate dataset:
```bash
python generate_data.py
```

Train the model:
```bash
python train_model.py
```

---

## Project Report

A full write-up of this project is included in the repository.
[Download Report](rocket-flight-prediction-ml_report.pdf)

---

## Future Improvements

- Improve aerodynamic drag modeling  
- Include real-world flight data  
- Predict full flight trajectory instead of only max height  
- Integrate CAD-based parameters into the simulation  

---

## Why This Project Matters

This project combines physics simulation, data generation, and machine learning into one system.

Instead of using an existing dataset, the model is trained on data generated from physics. This reflects how engineering problems are often approached, where simulations are used to estimate performance before building anything physically.
