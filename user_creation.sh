#!/bin/bash

curl -X POST -H "Content-Type: application/json" -d '{
  "username": "jloe",
  "email": "jloe@jdoe.com"
}' http://localhost:8000/users