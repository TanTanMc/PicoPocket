## PicoPocket
<img width="224" height="224" alt="image" src="https://github.com/user-attachments/assets/c16330d5-f00b-4802-bcdd-6a9ec3e67996" />


**PicoPocket** is a portable, pocket-sized computing device designed to function as a **digital wallet**.  
The project combines a **battery-powered Raspberry Pi**, a **compact display**, and **custom software** inside a **3D-printed enclosure** roughly the size of a bulky debit card.

I made this project to explore how everyday items like wallets could be redesigned using **embedded systems and modern electronics**. Instead of relying only on a phone as a digital wallet, PicoPocket introduces the **wallet itself as a dedicated digital device**, focused on portability, simplicity, and experimentation.


The diagram (simplified) (I added only the crucial parts) for the pickpocket

<img width="350" height="660" alt="image" src="https://github.com/user-attachments/assets/c1f3c030-85bd-4de4-aae1-e0985aaf16d2" />




## Bill of Materials (BOM)

| Item | Description | Qty | Unit Price (RON) | Unit Price (USD) | Notes |
|-----|------------|-----|------------------|------------------|------|
| Breadboard | MB-102 breadboard with jumper wires | 1 | 19.61 | 4.30 | Prototyping only (no PCB used) |
| Single Board Computer | Raspberry Pi Zero 2W (pre-soldered GPIO) | 1 | 123.71 | 27.10 | Main system computer |
| Battery | 3.7V 2000mAh Li-Po battery (804050) | 1 | 25.80 | 5.65 | Portable power source |
| Display | 2.4″ SPI TFT LCD with touch (ILI9341) | 1 | 25.64 | 5.61 | User interface display |
| Battery Charger | TP4056 USB-C Li-ion charger with protection | 2 | 1.40 | 0.31 | Redundancy for safety |
| Speaker | 8Ω 1W mini speaker | 1 | 2.80 | 0.61 | Audio output |
| Jumper Wires | Flexible jumper wire set | 1 | 7.90 | 1.73 | Power and signal wiring |
| Silicone Wire | 28 AWG silicone insulated wire (3 m) | 1 | 7.62 | 1.67 | Internal wiring |
| Fasteners | M2 screw assortment kit | 1 | 26.23 | 5.74 | Enclosure mounting |
| Storage | microSD card 32GB (Class 10, A1) | 1 | 24.16 | 5.28 | OS and storage |

**Estimated total cost:** **≈ 267.37 RON / 58.77 USD** but could yall give me 60-70$ because i need to pay for transport for some parts.. please

### Notes
- All components were sourced from **AliExpress** to reduce cost.
- The project uses a **breadboard instead of a PCB** for safety and cuz im not that smart.
- Power is managed directly through the **TP4056 charger module**.
- This BOM was created **manually** and is not auto-generated.


This is the Diagram/Wiring for the project:
<img width="1220" height="512" alt="image" src="https://github.com/user-attachments/assets/a6f4c5a1-f8c2-41ac-8b9c-22d38895846e" />



These are the angles of the 3D model.

<img width="590" height="719" alt="image" src="https://github.com/user-attachments/assets/1d892213-f475-499c-be6b-9d238aeb53c8" />
<img width="862" height="509" alt="image" src="https://github.com/user-attachments/assets/0f44284d-841c-42a6-8634-58802890523d" />
<img width="830" height="455" alt="image" src="https://github.com/user-attachments/assets/9c896f56-58ec-4e07-ade5-755995776fdf" />
<img width="538" height="422" alt="image" src="https://github.com/user-attachments/assets/623c4d70-b60c-4245-8282-292358acbbce" />


