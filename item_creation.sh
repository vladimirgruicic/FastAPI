#!/bin/bash

curl -X POST -H "Content-Type: application/json" -d '{
  "name": "Example Item",
  "price": 9.99,
  "quantity": 10
}' http://localhost:8000/items