# Detailed Class Diagram - Business Logic Layer

## Overview

This diagram represents the core business entities of the HBnB Evolution application and the relationships between them.

---

## Class Diagram

```mermaid
classDiagram

class BaseModel {
    +UUID id
    +datetime created_at
    +datetime updated_at
    +save()
    +update()
    +delete()
}

class User {
    +String first_name
    +String last_name
    +String email
    +String password
    +Boolean is_admin

    +register()
    +update_profile()
    +delete_user()
}

class Place {
    +String title
    +String description
    +Float price
    +Float latitude
    +Float longitude

    +create_place()
    +update_place()
    +delete_place()
    +list_places()
}

class Review {
    +Integer rating
    +String comment

    +create_review()
    +update_review()
    +delete_review()
    +list_reviews()
}

class Amenity {
    +String name
    +String description

    +create_amenity()
    +update_amenity()
    +delete_amenity()
    +list_amenities()
}

BaseModel <|-- User
BaseModel <|-- Place
BaseModel <|-- Review
BaseModel <|-- Amenity

User "1" --> "*" Place : owns
User "1" --> "*" Review : writes
Place "1" --> "*" Review : receives
Place "*" --> "*" Amenity : has
```
