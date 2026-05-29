# HBnB Evolution - Sequence Diagrams (API Calls)

This document contains sequence diagrams for key API interactions in the HBnB application, showing communication between:

- Presentation Layer (API / Services)
- Facade
- Business Logic Layer
- Persistence Layer

---

# 1. User Registration

## Description
A new user registers by providing personal details. The system validates and stores the user.

```mermaid
sequenceDiagram
actor User
participant API as Presentation Layer (API)
participant Facade
participant BL as Business Logic Layer
participant DB as Persistence Layer

User->>API: POST /users (register)
API->>Facade: create_user(data)
Facade->>BL: validate_user(data)

BL->>BL: check email uniqueness
BL->>DB: save_user(user)

DB-->>BL: confirmation
BL-->>Facade: user_created
Facade-->>API: success response
API-->>User: 201 Created
```

---

# 2. Place Creation

## Description
A logged-in user creates a new place listing.

```mermaid
sequenceDiagram
actor User
participant API as Presentation Layer (API)
participant Facade
participant BL as Business Logic Layer
participant DB as Persistence Layer

User->>API: POST /places
API->>Facade: create_place(data, user_id)
Facade->>BL: validate_place(data)

BL->>BL: validate price, location
BL->>DB: save_place(place)

DB-->>BL: confirmation
BL-->>Facade: place_created
Facade-->>API: success response
API-->>User: 201 Created
```

---

# 3. Review Submission

## Description
A user submits a review for a place they visited.

```mermaid
sequenceDiagram
actor User
participant API as Presentation Layer (API)
participant Facade
participant BL as Business Logic Layer
participant DB as Persistence Layer

User->>API: POST /reviews
API->>Facade: create_review(data)
Facade->>BL: validate_review(data)

BL->>BL: check rating (1–5)
BL->>DB: save_review(review)

DB-->>BL: confirmation
BL-->>Facade: review_created
Facade-->>API: success response
API-->>User: 201 Created
```

---

# 4. Fetch List of Places

## Description
A user requests a list of places (optionally filtered).

```mermaid
sequenceDiagram
actor User
participant API as Presentation Layer (API)
participant Facade
participant BL as Business Logic Layer
participant DB as Persistence Layer

User->>API: GET /places?filters
API->>Facade: get_places(filters)
Facade->>BL: process_filters(filters)

BL->>DB: query_places(filters)
DB-->>BL: list_of_places

BL-->>Facade: formatted_results
Facade-->>API: response data
API-->>User: 200 OK (places list)
```

---

# Explanatory Notes

## 1. User Registration
- User sends registration request
- API forwards to Facade
- Business layer validates and checks uniqueness
- Data is stored in persistence layer
- Response is returned back through all layers

---

## 2. Place Creation
- User creates a property listing
- Business logic validates price and coordinates
- Place is saved in database
- Confirmation is returned

---

## 3. Review Submission
- User submits rating + comment
- Business logic ensures rating validity (1–5)
- Review stored in database

---

## 4. Fetching Places
- User requests list of places
- Filters processed in business layer
- Database returns matching results
- Results formatted and returned

---

# Key Architectural Flow

✔ Presentation Layer → receives API calls  
✔ Facade → central communication point  
✔ Business Logic → validation + rules  
✔ Persistence Layer → database operations  

---

# Suggested File Structure

```text id="seq-folder-001"
holbertonschool-hbnb/
└── part1/
    ├── high_level_package_diagram.md
    ├── business_logic_class_diagram.md
    ├── sequence_diagrams.md
    └── README.md
```

---

If you want, I can also:
- convert this into a **PDF report for submission**
- or draw a **clean draw.io version**
- or help you prepare for **manual QA review questions**
