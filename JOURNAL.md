# JOURNAL

## Total Time Spent on Project
**20 hours**

---

## 18.11.2025  
**Time spent:** ~4 hours  

### Work done
- Designed the **project poster**
- Researched and selected **all electronic components**
- Created a **BOM (Bill of Materials)**
- Built a **demo website** to explain the purpose of the device  
  - Used **Lovable** because I am still learning how to code
- Defined the **main idea and use case** of the device

I am preparing this project for a **national physics tournament** that will take place in **May**.  
The goal is to demonstrate a **portable, pocket-sized computing device**.  

Initially, the components were very expensive, but I discovered **Hack Club**, which made this project possible.

### Media

- Poster design  
  <img width="1911" height="963" alt="b2a85d53-e8b1-4aa4-a132-6ef8feee8508" src="https://github.com/user-attachments/assets/137e951d-5740-4dd2-b1ed-9a6b703977ee" />


---

## 19.11.2025  
**Time spent:** ~7 hours  

### Work done
- Designed the **CAD enclosure**
- Started **PCB design**
- Tested early layouts and dimensions
- Ensured component fit inside the case

This stage focused on turning the idea into a **physical object**.

### Media
- CAD enclosure  
  <img width="1053" height="536" alt="f46f1171-0bb4-41e8-b774-179ffe7ce7f8" src="https://github.com/user-attachments/assets/72681b0a-e0a1-40ff-9ef0-475a6757ac28" />


---

## 05.12.2025  
**Time spent:** ~5 hours  

### Work done
- Adjusted the enclosure so the **screen fits perfectly**
- Changed the screen mounting method:
  - Instead of glue, I designed a **protective frame**
  - This made the device slightly bigger but much safer
- Began learning **PCB design basics**
- Decided to use a **breadboard** for now (safer and more flexible)

### Media
- First prototype  
 <img width="1898" height="957" alt="image" src="https://github.com/user-attachments/assets/f704034a-6c9e-4eb5-b147-07ddf59f012b" />
<img width="1318" height="861" alt="image" src="https://github.com/user-attachments/assets/c08b4877-cf22-4835-8f35-a82f0ac59e9b" />



---

## 13.12.2025  
**Time spent:** ~4 hours  

### Work done
- Created the **GitHub repository**
- Added:
  - `README.md`
  - `JOURNAL.md`
  - `BOM.csv`
  - `CAD/`
  - `Firmware/`
- Organized project structure for submission and review

### Media
- Repository structure  
  <img width="1915" height="951" alt="image" src="https://github.com/user-attachments/assets/2051d672-5d0a-4371-bef5-114c44506a05" />


---
## 13.12.2025  
**Time spent:** ~4 hours  

### Additional update
- **Remade the BOM to be more budget-friendly**
  - Reduced the total cost by approximately **$20**
  - Replaced higher-cost suppliers with components sourced from **AliExpress**
  - Improved overall project feasibility while staying within strict budget constraints



## Summary
PicoPocket evolved from an idea into a **working prototype**, including:
- Electronics
- CAD enclosure
- Firmware planning
- Documentation
- Presentation materials

This project represents **technical learning** , especially within budget constraints.

---

## 28.12.2025  
**Time spent:** ~5 hours  

### Work done
- Finalized the **electrical wiring plan**
- Cleaned up the **wiring diagram** to match the actual components being used
- Removed unnecessary parts from the design:
  - Boost converter
  - Breadboard with built-in power module
  - Bundled jumper wires
- Added the **RC522 NFC module** to the system design
- Updated the **BOM** with accurate prices and quantities
- Reformatted the **README** to clearly present the budget and component list
- Ensured that all components logically fit inside the enclosure

A large portion of the session was spent verifying that the wiring makes sense electrically and physically.  
I carefully checked how power flows from the Li-Po battery through the TP4056 charging module and into the Raspberry Pi Zero 2W, making sure that no unnecessary voltage conversion stages are used.  
This simplified the design and reduced cost, power loss, and complexity.

I also documented how the SPI bus is shared between the display and the NFC reader, confirming that the chip select lines are handled correctly and that there are no conflicts on the data lines.  
This step was important to avoid communication issues once the firmware development begins.

### Media
- Updated wiring diagram  
 <img width="1324" height="668" alt="image" src="https://github.com/user-attachments/assets/7ee51dfd-c905-4625-a61f-8efa57ec0b96" />

- Revised component layout inside enclosure  
  <img width="862" height="509" alt="image" src="https://github.com/user-attachments/assets/0f44284d-841c-42a6-8634-58802890523d" />

---

