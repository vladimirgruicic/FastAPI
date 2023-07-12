#!/bin/bash

curl -X POST -H "Content-Type: application/json" -d '{
  "username": "jloe",
  "email": "jloe@jdoe.com",
  "user_request": "I want my garden cleaned!"

}' http://localhost:8000/user_requests