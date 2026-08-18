# AI Textile Waste Intelligence Platform

An enterprise-grade, full-stack intelligence platform built to monitor, manage, and optimize textile waste recovery workflows, satisfying **Milestone 1** (Week 1 & 2) and **Modules 1 & 2** specifications.

---

## Technical Stack

* **Frontend**: React, Vite, TailwindCSS, React Router, Axios, Recharts (Chart.js wrapper), React Hot Toast
* **Backend**: FastAPI, SQLAlchemy (ORM), JWT Authentication (HS256), bcrypt (password hashing), Pydantic
* **Database**: PostgreSQL (production), SQLite (local persistent fallback for development convenience)
* **Deployment**: Docker, Docker Compose

---

## Getting Started

### 1. Local Development Setup (Without Docker)

This mode runs the backend using Python and the frontend using Node, storing data in a local SQLite file (`textile_waste_fallback.db`).

#### Backend Setup:
1. Navigate to the backend directory:
   ```bash
   cd backend
   ```
2. Activate the virtual environment:
   * **Windows**: `.\venv\Scripts\activate`
   * **macOS/Linux**: `source venv/bin/activate`
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Start the FastAPI server:
   ```bash
   uvicorn main:app --reload --port 8000
   ```
   *The database tables will be created automatically and seeded on startup.*

#### Frontend Setup:
1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```
2. Install npm packages:
   ```bash
   npm install
   ```
3. Start the Vite dev server:
   ```bash
   npm run dev
   ```
4. Open your browser to the URL shown (normally `http://localhost:5173`).

---

### 2. Production Docker Setup

To build and run all services (PostgreSQL, FastAPI backend, React frontend hosted via Nginx reverse proxy) in Docker:

1. Navigate to the `docker` directory:
   ```bash
   cd docker
   ```
2. Build and start the services:
   ```bash
   docker-compose up --build
   ```
3. Access the services:
   * **Frontend Application**: `http://localhost`
   * **FastAPI Backend Swagger Docs**: `http://localhost/docs` (or `http://localhost:8000/docs`)
   * **PostgreSQL Database**: Port `5432`

---

## Default Seeding Credentials

The platform seeds a default Administrator account and template inventory records on database initialization.

### Default Admin Login:
* **Email**: `madhulikagoddumarri@gmail.com`
* **Password**: `123456789`
* **Role**: `Administrator`

### Default Manufacturer Login:
* **Email**: `mfg@twip.org`
* **Password**: `Password123`
* **Role**: `Textile Manufacturer`
