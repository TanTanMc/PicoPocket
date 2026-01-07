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

## How the PicoPocket App Works

PicoPocket runs raspbery pi OS on the **Raspberry Pi Zero 2 W**.  
The application turns the device into a **stand-alone digital wallet interface**, eliminating the need for a smartphone for everyday wallet operations.

---

### Main Functions

### 1. Virtual Wallet

The app allows the user to store and manage multiple digital identities, including:

- Bank cards (via NFC emulation and UID handling)
- Access cards and ID tags
- Cryptocurrency wallet keys
- Custom user credentials

All information is stored **locally on the device**. NOT IN THE CLOUD, so hackers can't steal the wallet's somehow. 
The system is designed so that encryption and advanced security features can be added in later versions.

---

### 2. Card & Payment Interaction

Using the built-in **NFC module**, PicoPocket can:

- Read physical cards
- Store card identifiers digitally
- Present the selected identity when making a payment or accessing a system

This allows the user to carry **many cards in one physical device**.

---

### 3. Crypto & Transfers

The application also supports cryptocurrency operations, including:

- Storing wallet keys
- Initiating payments directly from the device
- Transferring funds without converting through traditional banking systems

This enables:

- Fast payments  
- Direct crypto usage  
- Simple peer-to-peer transfers  

Transfers between users can be performed in two ways:

1. **POS-style transfer** when two PicoPocket devices are near each other, using the NFC (Still working on this)  
2. **PICO Tag transfer**, is like REVtag from revolut, but for this. Or email/phone number
---

### 4. User Interface

The touchscreen provides access to:

- Wallet overview
- Card selection
- Payment and transfer menus
- Device status (battery, storage, connections)

All interaction happens **directly on PicoPocket** without requiring a phone.


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
<img width="1536" height="1024" alt="c9958e8f-3e48-4044-a637-84655ff5b268" src="https://github.com/user-attachments/assets/beb77e36-3507-4fb0-958d-6c4c9a15d735" />


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
