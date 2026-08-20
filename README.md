# Heat Exchanger Design Project

A simple chemical engineering project for analyzing and sizing a heat exchanger using Python, Streamlit, and Matplotlib.

This app helps students and engineers estimate:
- heat duty
- outlet temperatures
- LMTD (log mean temperature difference)
- required heat transfer area
- temperature profile visualization

## Project Objective

The project models a basic shell-and-tube or double-pipe heat exchanger used in process industries. It is designed as a practical learning tool for core chemical engineering concepts related to heat transfer.

## Features

- Interactive Streamlit interface
- Input parameters for hot and cold fluids
- Calculation of energy balance and heat duty
- LMTD calculation for counter-current flow
- Estimated heat exchanger area
- Matplotlib temperature profile plot
- Easy-to-run setup for local use

## Why this project matters

In core chemical engineering, heat exchangers are used for:
- heating and cooling process streams
- energy recovery
- reactor feed preheating
- separation process temperature control
- process safety and efficiency

## Project Workflow

1. Enter fluid properties and flow conditions.
2. Input inlet and outlet temperatures.
3. Select flow arrangement.
4. View calculated heat duty and area.
5. Review the temperature distribution plot.

## Technologies Used

- Python 3
- Streamlit
- Matplotlib
- NumPy

## File Structure

```text
heat_exchanger_project/
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

1. Open a terminal in the project folder.
2. Create a virtual environment (optional but recommended):

```bash
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the App

```bash
streamlit run app.py
```

Then open the local URL shown in the terminal, usually:

```text
http://localhost:8501
```

## Core Formula Used

### Heat duty

```text
Q = m * Cp * (Tin - Tout)
```

### LMTD for counter-current flow

```text
LMTD = ((ΔT1 - ΔT2) / ln(ΔT1 / ΔT2))
```

where:
- ΔT1 = Th,in - Tc,out
- ΔT2 = Th,out - Tc,in

### Heat transfer area

```text
A = Q / (U * LMTD)
```

where:
- A = heat transfer area (m²)
- U = overall heat transfer coefficient (W/m²·K)
- Q = heat duty (W)

## Example

A typical design case may include:
- hot fluid inlet temperature: 120°C
- hot fluid outlet temperature: 80°C
- cold fluid inlet temperature: 30°C
- cold fluid outlet temperature: 70°C
- overall heat transfer coefficient: 800 W/m²·K

The app calculates the required exchanger area from these values.

## Notes

This project is intended for educational and preliminary design analysis. For actual industrial heat exchanger design, designers should also consider:
- fouling factors
- pressure drop
- material compatibility
- exchanger type selection
- safety and process standards

## License

This project is provided for educational use.
