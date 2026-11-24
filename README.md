# 🏛️ Fix My City

> **Civic Grievance Redressal & Municipal Operations Platform**  
> *Engineered specifically for Shri Ramdeobaba University (RBU) Campus & Katol Road, Nagpur (`21.1764° N, 79.0617° E`).*

[![Live Demo](https://img.shields.io/badge/Live%20Demo-GitHub%20Pages-black?style=flat&logo=github)](https://aryan2739.github.io/fix-my-city/)
[![Figma Prototype](https://img.shields.io/badge/Figma-Prototype%20Canvas-black?style=flat&logo=figma)](https://www.figma.com/design/RB6XpSiJ4nMNFf2oTlz0Mi)
[![Stack](https://img.shields.io/badge/Tech%20Stack-100%25%20HTML5%20%2B%20CSS3-blue?style=flat)]()
[![Zero JS](https://img.shields.io/badge/JavaScript-0%25%20(Pure%20CSS)-success?style=flat)]()

---

## 🌟 Live Links

- **🌐 Live Hosted Website**: [https://aryan2739.github.io/fix-my-city/](https://aryan2739.github.io/fix-my-city/)
- **🎨 Figma Design Canvas**: [Figma Prototype File (`RB6XpSiJ4nMNFf2oTlz0Mi`)](https://www.figma.com/design/RB6XpSiJ4nMNFf2oTlz0Mi)
- **📁 GitHub Repository**: [https://github.com/Aryan2739/fix-my-city](https://github.com/Aryan2739/fix-my-city)

---

## 📌 Project Overview

**Fix My City** is a modern civic technology portal designed to bridge university students, faculty, and residents with municipal authorities (Nagpur Municipal Corporation). It provides transparent reporting, tracking, and field crew verification for physical civic infrastructure issues.

### ⚡ Architectural Philosophy: 100% Pure HTML5 + CSS3
This project is built with **zero runtime JavaScript**. All interactive capabilities are powered by modern CSS3 structural techniques:
- **Popups & Modals**: Built using the CSS `:target` pseudo-class.
- **Category Filter Tabs**: Powered by the CSS radio button sibling combinator hack (`:checked ~`).
- **Interactive Upvoting**: Built with HTML checkbox states (`:checked + .upvote-box`).
- **Campus Geospatial Map**: Embedded via responsive OpenStreetMap HTML5 `<iframe>` centered on Katol Road & RBU Nagpur.
- **Mobile Navigation**: Toggled purely via CSS checkbox state.

---

## 📸 The 4 Real-World Nagpur Civic Complaints

All issues feature 100% authentic local photographs stored in `assets/`:

| Ticket # | Category | Incident Title | Nagpur Location | Status |
| :--- | :--- | :--- | :--- | :--- |
| **#FMC-101** | 🚧 Roads & Potholes | **Deep Hazardous Pothole near Main Entrance Gate** | Main Gate, Ramdeobaba University, Katol Road | `REPORTED` |
| **#FMC-102** | 💡 Street Lighting | **Series of 4 Dark Streetlights on Campus Hostel Pathway** | Hostel & Temple Pathway, Ramdeo Tekdi, RBU | `IN PROGRESS` |
| **#FMC-103** | 🗑️ Waste Management | **Overflowing Garbage Bins outside Campus Gate 2** | Opposite Gate 2, Gittikhadan, Katol Road | `RESOLVED` |
| **#FMC-104** | 💧 Water & Drainage | **Drinking Water Supply Pipeline Leak near Sports Complex** | Sports Complex Road, Ramdeobaba University | `IN PROGRESS` |

---

## 🔄 4-Stage Municipal Lifecycle Pipeline

Each reported issue progresses through a transparent 4-stage municipal resolution pipeline:
1. **Registered**: Citizen grievance logged with timestamp.
2. **Under Verification**: Validated by zonal municipal desk.
3. **Crew Dispatched**: Field maintenance team assigned.
4. **Resolved & Closed**: Verified fixed with side-by-side Before vs After photographic proof.

---

## 🚀 How to Run Locally

Because this project requires no build tools, compilers, or server backends:
1. Clone the repository:
   ```bash
   git clone https://github.com/Aryan2739/fix-my-city.git
   ```
2. Double-click `index.html` to open it in any web browser.

---

## 👨‍💻 Author & Academic Information

- **Author**: Aryan Gupta (CSE 1st Year)
- **Institution**: Shri Ramdeobaba University (RBU), Nagpur
- **Design System**: 8-Point Minimalist Monochrome Box Architecture
