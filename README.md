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

## Bill of Materials (BOM)

> Budget requested: **$65–70 USD**  
> This accounts for **shipping, taxes, and AliExpress transport costs**

| Item | Description | Qty | Notes |
|-----|------------|-----|------|
| Breadboard | Standard mini breadboard (no power module) | 1 | Prototyping only |
| Single Board Computer | Raspberry Pi Zero 2W (pre-soldered GPIO) | 1 | Main system |
| Battery | 3.7V 2000mAh Li-Po (804050) | 1 | Portable power |
| Display | 2.4″ SPI TFT LCD + Touch (ILI9341) | 1 | Main UI |
| Battery Charger | TP4056 USB-C (with protection) | 2 | Redundancy |
| Speaker | 8Ω 1W mini speaker | 1 | Audio |
| Jumper Wires | Separate jumper wire set | 1 | Signal + power |
| Silicone Wire | 28 AWG silicone wire (3m) | 1 | Internal wiring |
| Fasteners | M2 screw assortment | 1 | Enclosure |
| Storage | microSD 32GB (Class 10, A1) | 1 | OS + data |
| NFC Module | SPI-based NFC reader (RC522) | 1 | Contactless cards |

**Estimated total (with shipping): ≈ $65–70 USD**

---

## Wiring Diagram

<img width="1220" height="512" alt="image" src="https://github.com/user-attachments/assets/a6f4c5a1-f8c2-41ac-8b9c-22d38895846e" />

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
