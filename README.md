## PicoPocket

<img width="224" height="224" alt="image" src="https://github.com/user-attachments/assets/c16330d5-f00b-4802-bcdd-6a9ec3e67996" />

**PicoPocket** is a portable, pocket-sized computing device designed to function as a **digital wallet**.  
It combines a **battery-powered Raspberry Pi**, a **compact touchscreen display**, and **custom software** inside a **3D-printed enclosure** roughly the size of a bulky debit card.

I built this project to explore how everyday items like wallets could be redesigned using **embedded systems and modern electronics**. Instead of relying only on a smartphone, PicoPocket introduces the **wallet itself as a dedicated digital device**, focused on portability, simplicity, and experimentation.

---

## Simplified System Diagram

*(Only the crucial components are shown)*

<img width="350" height="660" alt="image" src="https://github.com/user-attachments/assets/c1f3c030-85bd-4de4-aae1-e0985aaf16d2" />

---

## Power Architecture

- **3.7V Li-Po battery**
- **TP4056 USB-C charger module (with protection)**
- Raspberry Pi powered through **5V output**
- ❌ No boost converter (not needed)
- ❌ No powered breadboard
---
## Bill of Materials

This document lists all required components with pricing in **RON** and **USD**.

---

## 🔧 Components & Pricing

| # | Component | Qty | Unit (RON) | Unit (USD) | Total (RON) | Total (USD) |
|---|----------|-----|------------|------------|-------------|-------------|
| 1 | NFC / RFID Module | 1 | 9.37 | 2.04 | 9.37 | 2.04 |
| 2 | Micro SD Card 32GB | 1 | 28.03 | 6.09 | 28.03 | 6.09 |
| 3 | Screw Kit (M2–M6) | 1 | 22.27 | 4.84 | 22.27 | 4.84 |
| 4 | Silicone Wire 30 AWG | 1 | 8.23 | 1.79 | 8.23 | 1.79 |
| 5 | Jumper Wires (M–M) | 1 | 7.36 | 1.60 | 7.36 | 1.60 |
| 6 | Jumper Wires (M–F) | 1 | 7.10 | 1.54 | 7.10 | 1.54 |
| 7 | TFT Display 2.4" Touch | 1 | 30.78 | 6.69 | 30.78 | 6.69 |
| 8 | Raspberry Pi Zero 2 W (Soldered Header) | 1 | 137.68 | 29.93 | 137.68 | 29.93 |
| 9 | Speaker 8Ω 1W | 1 | 2.45 | 0.53 | 2.45 | 0.53 |
|10 | TP4056 Charger Module | 2 | 0.62 | 0.13 | 1.24 | 0.27 |
|11 | Li-Po Battery 2000mAh | 1 | 29.02 | 6.31 | 29.02 | 6.31 |

---

##  Grand Total

- **Total (RON):** **283.53 RON** = 291 RON (With Shipping)
- **Total (USD):** **61.63 USD**  = 67.16 USD (With Shipping)

---

## Wiring Diagram

<img width="1324" height="668" alt="image" src="https://github.com/user-attachments/assets/53790162-aa62-4ab9-ad65-e36383a786fd" />


---

## 3D Enclosure Preview

<img width="590" height="719" alt="image" src="https://github.com/user-attachments/assets/1d892213-f475-499c-be6b-9d238aeb53c8" />
<img width="862" height="509" alt="image" src="https://github.com/user-attachments/assets/0f44284d-841c-42a6-8634-58802890523d" />
<img width="830" height="455" alt="image" src="https://github.com/user-attachments/assets/9c896f56-58ec-4e07-ade5-755995776fdf" />
<img width="538" height="422" alt="image" src="https://github.com/user-attachments/assets/623c4d70-b60c-4245-8282-292358acbbce" />

---

### Notes

- All components sourced from **AliExpress**
- Breadboard used instead of PCB for **safety and learning**
- BOM is **manually created**
