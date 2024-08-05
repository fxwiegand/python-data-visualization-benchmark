import pandas as pd
import numpy as np
import yaml

with open("config.yaml", 'r') as file:
    config = yaml.safe_load(file)

dataset_size = config.get('dataset_size', 100)

patient_ids = [f"ID_{i:09d}" for i in range(dataset_size)]
hospital_ids = [f"HOS_{i:09d}" for i in range(dataset_size)]

categories = ["Healthy", "Diabetic", "Hypertensive", "Cardiac"]
diagnosis = np.random.choice(categories, dataset_size)

age = np.random.uniform(20.0, 80.0, size=dataset_size)
blood_pressure = np.random.uniform(90.0, 180.0, size=dataset_size)
heart_rate = np.random.randint(60, 100, size=dataset_size)
cholesterol = np.random.randint(150, 300, size=dataset_size)

df = pd.DataFrame({
    'Patient_ID': patient_ids,
    'Hospital_ID': hospital_ids,
    'Diagnosis': diagnosis,
    'Age': age,
    'Blood_Pressure': blood_pressure,
    'Heart_Rate': heart_rate,
    'Cholesterol': cholesterol
})

df.to_csv("data/input.csv", index=False)
