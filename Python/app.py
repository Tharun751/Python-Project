from flask import Flask, render_template, request, redirect, url_for
import numpy as np  # Import numpy

app = Flask(__name__)

class Patient:
    def __init__(self, name, age, test_result=None):
        self.name = name
        self.age = age
        self.test_result = test_result

    def to_dict(self):
        return {"Name": self.name, "Age": self.age, "Test Result": self.test_result}

class CovidTestManagementSystem:
    def __init__(self):
        self.patients = []

    def add_patient(self, patient):
        self.patients.append(patient)

    def get_patient_by_name(self, name):
        for patient in self.patients:
            if patient.name == name:
                return patient
        return None

    def update_test_result(self, name, test_result):
        patient = self.get_patient_by_name(name)
        if patient:
            patient.test_result = test_result
            print(f"Test result updated for {patient.name}")
        else:
            print(f"Patient with name {name} not found.")

    def get_all_patients(self):
        return [patient.to_dict() for patient in self.patients]

    def generate_test_result(self):
        # Simulate COVID-19 test result using numpy
        return np.random.choice(['Positive', 'Negative'], p=[0.3, 0.7])

patients_data = []
covid_system = CovidTestManagementSystem()

@app.route('/')
def index():
    return render_template('index.html', patients=patients_data)

@app.route('/testing_page')
def testing_page():
    return render_template('testing_page.html')

@app.route('/admin')
def admin():
    all_patients = covid_system.get_all_patients()
    return render_template('admin.html', all_patients=all_patients)

@app.route('/add_patient', methods=['POST'])
def add_patient():
    name = request.form.get('name')
    age = int(request.form.get('age'))

    # Generate COVID-19 test result
    test_result = covid_system.generate_test_result()

    patient = Patient(name, age, test_result)
    covid_system.add_patient(patient)

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
