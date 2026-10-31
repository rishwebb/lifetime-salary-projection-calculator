#  Earnings OS — Lifetime Revenue Portfolio & Timeline

> A premium, macOS-styled financial ledger and personal milestone tracker built with Vanilla HTML5, CSS3, and JavaScript. Zero dependencies, pure Apple SVG vectors, and frosted glassmorphism.

[![Live Demo](https://img.shields.io/badge/Demo-Live%20Dashboard-dcf836?style=for-the-badge&logo=apple&logoColor=black)](https://rishwebb.github.io/Salary-Lifetime/)
[![License](https://img.shields.io/badge/License-MIT-gray?style=for-the-badge)](LICENSE)

---

## 💎 Design System & Highlights
- **macOS Studio Aesthetics**: Frosted glassmorphism (`backdrop-filter: blur(20px)`), deep obsidian black background (`#060709`), and high-contrast electric lime-yellow-green accents (`#dcf836`).
- **Authentic Apple Details**: macOS window chrome with functional traffic lights (close, minimize, zoom) and sticky top menubar with real-time Cupertino clock.
- **Strictly Zero Emojis**: Every interface icon, indicator, and category symbol is a hand-crafted Apple-style vector SVG.
- **100% Mobile Responsive**: Tested across mobile viewports (iPhone/Android) with zero horizontal overflow, fluid touch scrolling, and adaptive layouts.

---

## 📊 Consolidated Portfolio Figures (June 2025 – October 2026)

| Category | Source File | Records | Total (₹) | % of Earned |
| :--- | :--- | :---: | :---: | :---: |
| **🏢 Freelance Agency Salary** | [`freelance_agency_salary.csv`](./freelance_agency_salary.csv) | 5 months | **₹47,000.00** | 74.6% |
| **🎓 Freelance College Work** | [`freelance_college_work.csv`](./freelance_college_work.csv) | 12 payouts | **₹10,919.00** | 17.3% |
| **📦 Digital Product Sales** | [`digital_product_sale_revenue.csv`](./digital_product_sale_revenue.csv) | 25 records *(33 sales)* | **₹4,413.29** | 7.0% |
| **💳 Razorpay Online Gateway** | [`razorpay_earnings.csv`](./razorpay_earnings.csv) | 51 txns | **₹569.56** | 0.9% |
| **✍️ Review Work Bounty** | Voice Record *(Jun 2025)* | 1 credit | **₹90.00** | 0.1% |
| **Gross Total Money Made** | | **94 entries** | **₹62,991.85** | **100.0%** |

> [!NOTE]
> **Focused Revenue Tracking**: All portfolio metrics strictly track organic money made through professional retainers, client freelancing, and digital asset sales. Non-earning elements (such as gambling activities) are omitted, keeping the focus entirely on real-world value creation and upward financial momentum.

---

## 🚀 Key Modules
1. **Interactive Trajectory Chart**: Switch between *Combined View*, *Monthly Revenue*, and *Cumulative Growth* views with dynamic SVG curves and bars.
2. **Monthly Milestones Scrubber**: Horizontal selector tracking progression from June 2025 to October 2026. Clicking any month automatically filters the granular ledger.
3. **Visual Journey Lookbook**: Milestone cards with Retina photo frames ready for photo uploads (supports drag-and-drop or file upload with instant localStorage persistence). Features the October 2026 milestone celebrating the new all-time high ₹15k salary and the Poco X8 Pro Max upgrade.
4. **Granular Ledger (94 Transactions)**: Real-time search, category dropdown filter, sorting (date/amount), and pagination.
5. **One-Click Export**: Download the complete audited master dataset in structured JSON format.

---

## 🛠️ Local Development

Clone the repository and run any static file server:

```bash
# Clone repository
git clone https://github.com/rishwebb/Salary-Lifetime.git
cd Salary-Lifetime

# Serve with Python
python -m http.server 3000

# Or serve with Node / NPX
npx serve .
```

Open `http://localhost:3000` in your browser.
