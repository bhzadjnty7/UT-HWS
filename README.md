# Hardware Security and Trust - University of Tehran

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![Verilog](https://img.shields.io/badge/Verilog-RTL-purple)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Logistic%20Regression-orange)
![Security](https://img.shields.io/badge/Security-Cryptography-red)

## 📑 Table of Contents
- [About The Course](#-about-the-course)
- [Projects Overview](#-projects-overview)
  - [HW4: IP Watermarking](#hw4-ip-watermarking)
  - [CA1 - Part 1: PRESENT Block Cipher](#ca1---part-1-present-block-cipher)
  - [CA1 - Part 2: RFID Mutual Authentication](#ca1---part-2-rfid-mutual-authentication)
  - [CA2: Physical Unclonable Functions (PUFs)](#ca2-physical-unclonable-functions-pufs)
  - [CA3: Hardware Trojan Detection](#ca3-hardware-trojan-detection)
- [Technologies & Tools](#-Technologies-&-Tools)
- [How to Run](#-how-to-run)
- [License](#-license)

## 📌 About the Course
This repository contains the assignments and practical projects for the **Hardware Security and Trust** course, offered at the **University of Tehran (UT)**, Department of Electrical and Computer Engineering, during the **Spring 2025 (1403-1404)** semester under the supervision of **Dr. Siamak Mohammadi**.

The course covers a wide range of topics in hardware security, from physical-level security primitives to system-level vulnerabilities. The projects implemented here demonstrate practical approaches to both securing hardware systems and exploiting their vulnerabilities using analytical and machine learning techniques.

---

## 🚀 Projects Overview

This repository is divided into four main assignments, each targeting a specific domain within hardware security:

### 1. Lightweight Cryptography & RFID Authentication (`HW1` & `HW2_Part2`)
This project focuses on secure communication in resource-constrained environments (like IoT and RFID tags).
* **PRESENT Block Cipher:** Implementation of the ultra-lightweight PRESENT cipher (80-bit key, 64-bit block) from scratch in Python. Includes building the Substitution (S-box) and Permutation layers.
* **Error Propagation Analysis:** Evaluating the resilience of ECB, CBC, and CTR encryption modes against channel noise.
* **Lightweight RFID Mutual Authentication:** A Client-Server socket programming implementation of an RFID authentication protocol using `SHA-256/512` and Pre-Shared Keys (PSK). It includes defensive mechanisms against Replay and Man-in-the-Middle (MITM) attacks.

### 2. Physical Unclonable Functions (PUFs) & ML Attacks (`HW2_PUF`)
Analysis of hardware security primitives that leverage manufacturing variations.
* **PUF Simulation:** Modeled standard **Arbiter PUFs** and **XOR Arbiter PUFs** using the `pypuf` library.
* **Metric Evaluation:** Calculated intra-chip Hamming distance (Reliability), inter-chip Hamming distance (Uniqueness), and Bit Aliasing.
* **Noise Simulation:** Analyzed the effect of environmental noise (5% bit-flip probability) on Challenge-Response Pairs (CRPs).
* **Machine Learning Modeling Attacks:** Implemented a **Logistic Regression** model using `scikit-learn` to successfully predict PUF responses based on CRP tables, demonstrating vulnerabilities in standard Arbiter PUFs.
* **Randomness Testing:** Evaluated the generated keys against the **NIST SP 800-22** statistical test suite to ensure True Random Number Generator (TRNG) qualities.

### 3. Hardware Trojan Detection in ALU (`HW3_Trojan`)
A deep dive into identifying malicious modifications in integrated circuits using both structural and functional analysis.
* **White-box Analysis:** Inspected the Verilog RTL code of an infected Arithmetic Logic Unit (ALU) to manually identify 5 inserted Hardware Trojans.
* **Black-box Analysis:** Developed automated Python testbenches to generate randomized stimuli to trigger hidden payloads.
* **Simulation & Code Coverage:** Used ModelSim to compare the Golden Model versus the infected model, utilizing Code Coverage metrics to pinpoint unexercised anomalous branches.

### 4. Hardware Watermarking (`HW4_Watermarking`)
Applying Intellectual Property (IP) protection techniques to digital circuit designs.
* **Don't Care Condition Watermarking:** Embedded specific author signatures (bitstreams) into the logic functions of a circuit using Karnaugh maps and unused minterms.
* **Encoder & Graph Coloring Watermarking:** Applied watermarking techniques to a 4-to-2 encoder and a graph coloring problem constraint set, ensuring normal operation remains completely unaffected.

---

## 🛠️ Technologies & Tools
* **Programming Languages:** Python 3.x, Verilog
* **Machine Learning & Data:** `scikit-learn`, `numpy`, `matplotlib`
* **Hardware Security Libs:** `pypuf`
* **Simulation Tools:** ModelSim (for Trojan detection)
* **Networking:** Python `socket` library (for RFID protocol)
* **Environment:** Jupyter Notebooks (`.ipynb`) and standard Python scripts.

---

## 📂 Repository Structure

```text
├── HW1_Cryptography_RFID/
│   ├── PRESENT_Cipher.ipynb      # PRESENT implementation and Error Propagation
│   ├── client.py                 # RFID Tag simulator
│   └── server.py                 # RFID Reader simulator
├── HW2_PUF_ML_Attacks/
│   ├── arbiter_puf.py            # PUF instantiation
│   ├── generate_crps.py          # CRP generation script
│   ├── ml_attack.py              # Logistic Regression attack model
│   ├── simulate_noise.py         # Environmental noise simulator
│   └── reports/                  # NIST Randomness test results
├── HW3_Hardware_Trojans/
│   ├── Golden_ALU.v              # Uninfected RTL design
│   ├── Infected_ALU.v            # RTL design with 5 Trojans
│   └── testbenches/              # Python scripts for stimuli generation
├── HW4_Watermarking/
│   └── HW4_Solutions.pdf         # Analytical solutions for K-Maps and Logic Gates
└── README.md
```
---
## ⚙️ How to Run
* Clone the Repository
```bash
git clone https://github.com/[Your-Username]/Hardware-Security-and-Trust-UT.git
cd Hardware-Security-and-Trust-UT
```

* Install Dependencies
For the Python-based projects (PUFs, Cryptography, ML Attacks), install the required libraries:
```bash
pip install numpy matplotlib scikit-learn pypuf
```

* Example: Running the ML Attack on PUF
Navigate to the PUF directory and run the attack simulation:
```bash
cd HW2_PUF_ML_Attacks
python generate_crps.py    # Generates challenges.csv and responses.csv
python ml_attack.py        # Trains the model and prints the prediction accuracy
```

* Example: Simulating the RFID Protocol
Open two separate terminal windows.

In Terminal 1 (Start Reader/Server):
```bash
cd HW1_Cryptography_RFID
python server.py
```
In Terminal 2 (Start Tag/Client):
```bash
python client.py
```
---
## 👥 Author
* Behzad Jannati - M.Sc. Student at University of Tehran
* Student ID: 810103098
* GitHub: @bhzadjnty7

---
## 📜 License
This project is open-source and available under the MIT License. Note that these assignments are strictly for educational purposes as part of the University of Tehran curriculum. Please adhere to the university’s academic integrity policies if you are a current student.

---
## ⭐️ Support

If you find this repository useful, consider giving it a ⭐️
