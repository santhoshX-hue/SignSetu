# SignSetu Shared API Contract (Draft)

## 1. Overview & System Principles
SignSetu is an **offline-first healthcare communication assistant** for deaf and non-speaking patients.

### Core Ethical & Clinical Safety Rules:
1. **No Autonomous Diagnosis or Triage**: The local AI model (`llama3.2:3b` via Ollama) must **ONLY** simplify doctor-provided medical explanations into plain, accessible language. It must never diagnose, triage, or invent clinical advice.
2. **Mandatory Doctor Approval Gate**: No AI-generated or simplified communication reaches the patient or the Text-to-ISL module without explicit review and approval by the attending doctor.
3. **Offline-First Guarantee**: All microservices and modules must function entirely on local network/localhost interfaces without external cloud dependencies.
4. **Decoupled Architecture**: Individual modules interface exclusively through standard JSON contracts.

---

## 2. Shared Data Models (`schemas.py`)

### 2.1 Medical Simplification Request (Doctor -> Ollama)
```json
{
  "doctor_notes": "Patient presents with acute pharyngitis. Prescribed amoxicillin 500mg TID for 7 days. Ensure adequate hydration.",
  "simplification_level": "simple_plain_language"
}
```

### 2.2 Simplification Response for Review (Ollama -> Doctor Dashboard)
```json
{
  "original_text": "Patient presents with acute pharyngitis. Prescribed amoxicillin 500mg TID for 7 days. Ensure adequate hydration.",
  "simplified_draft": "You have a throat infection. Take one antibiotic pill three times a day for 7 days. Drink plenty of water.",
  "status": "pending_doctor_approval"
}
```

### 2.3 Doctor Approval & Dispatch (Doctor Dashboard -> Backend)
```json
{
  "approved_text": "You have a throat infection. Take one antibiotic pill three times a day for 7 days. Drink plenty of water.",
  "doctor_id": "dr_001",
  "patient_session_id": "session_101",
  "approved": true
}
```

### 2.4 Motion-to-Text Contract [Teammate Module]
```json
{
  "session_id": "session_101",
  "detected_tokens": ["HEADACHE", "PAIN", "TWO_DAYS"],
  "confidence": 0.88,
  "constructed_phrase": "I have had a headache for two days."
}
```

### 2.5 Text-to-ISL Contract [Teammate Module]
> Note: Standardizes gesture gloss tokens/cues. Does not claim exhaustive grammatical ISL representation.
```json
{
  "input_text": "Take medicine after food",
  "isl_gloss_sequence": ["FOOD", "FINISH", "MEDICINE", "TAKE"],
  "animation_cues": ["anim_food", "anim_finish", "anim_medicine", "anim_take"]
}
```

---

## 3. Endpoints Overview

| Method | Endpoint | Module Owner | Description |
|---|---|---|---|
| `GET` | `/api/health` | Shared | Service health & local Ollama availability |
| `POST` | `/api/doctor/simplify` | Doctor / Backend | Requests local Llama 3.2 simplification of doctor's note |
| `POST` | `/api/doctor/approve-and-send` | Doctor / Backend | Approves simplified message and queues for patient |
| `GET` | `/api/patient/messages/{session_id}` | Patient Module | Retrieves doctor-approved messages for the patient |
| `POST` | `/api/motion/recognize` | Motion-to-Text | Streams/posts gesture cues to recognized text |
| `POST` | `/api/isl/generate-gloss` | Text-to-ISL | Converts approved simplified text to ISL gloss sequence |

---

## 4. Shared Integration Guardrails
- **`backend/app/main.py`**: Shared router aggregator. Do not alter router mounts without team sync.
- **`backend/app/models/schemas.py`**: Shared Pydantic data schemas.
- **`frontend/src/App.jsx`**: Shared top-level view router (`/doctor` and `/patient`).
