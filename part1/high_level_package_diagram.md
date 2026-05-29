# High-Level Package Diagram - HBnB Evolution

## Overview

The HBnB Evolution application follows a three-layer architecture:

1. Presentation Layer
2. Business Logic Layer
3. Persistence Layer

The application uses the Facade Pattern to simplify communication between the presentation layer and the business logic layer.

---

## Package Diagram

```mermaid
classDiagram

class PresentationLayer {
    <<Interface>>
    +APIEndpoints
    +Services
}

class HBnBFacade {
    +create_user()
    +update_user()
    +create_place()
    +create_review()
    +get_places()
}

class BusinessLogicLayer {
    +User
    +Place
    +Review
    +Amenity
}

class PersistenceLayer {
    +UserRepository
    +PlaceRepository
    +ReviewRepository
    +AmenityRepository
    +DatabaseAccess
}

PresentationLayer --> HBnBFacade : Uses
HBnBFacade --> BusinessLogicLayer : Handles Business Logic
BusinessLogicLayer --> PersistenceLayer : Database Operations
```
