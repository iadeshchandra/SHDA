# 🚀 SHDA Management App

A **production-ready nonprofit management system** built with Python (Kivy) for Android.

Designed for clubs, organizations, and community groups to manage:

- 👥 Members
- 💰 Donations
- 📊 Expenses (Social & Festival separated)
- 📄 Reports (PDF)
- ☁️ Firebase Sync
- 📱 Automated APK Build (GitHub Actions)

---

## ✨ Key Features

### 🔐 Authentication
- Secure admin login
- Default credentials:
  - Username: `admin`
  - Password: `admin123`

---

### 👥 Member Management
- Add and manage members
- Store name and phone number
- Sync to Firebase

---

### 💰 Donation Tracking
- Assign donations to members
- Track amount and date
- Clean structure for reporting

---

### 📊 Expense Management
- Two separate categories:
  - Social Work
  - Festival Expenses
- Item-based structure (JSON)
- Full tracking with timestamps

---

### 📄 Reports System
- Generate PDF reports
- Stored in device storage
- Expandable for advanced analytics

---

### ☁️ Firebase Integration
- Real-time data sync
- Easy backend scaling
- Works alongside offline SQLite

---

### ⚡ Offline-First Architecture
- Uses SQLite locally
- Works without internet
- Sync-ready for future upgrades

---

### 🤖 GitHub Auto APK Build
- No local setup required
- Fully automated using GitHub Actions
- APK generated on every push

---

## 📂 Project Structure