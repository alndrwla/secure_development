# Vertical Privilege Escalation Example

This folder contains examples of vertical privilege escalation vulnerabilities and their secure alternatives using Python and Flask.

## Endpoints

- **/resource-insecure** (POST):
  - Highly insecure. Allows any user to change the role of any other user.
  - Example payload:
    ```json
    {
      "user": "alice",
      "target": "bob",
      "new_role": "user"
    }
    ```

- **/resource** (POST):
  - Vulnerable. Allows a user to change their own role by sending the `role` field.
  - Example payload:
    ```json
    {
      "user": "alice",
      "role": "admin"
    }
    ```

- **/resource-secure** (POST):
  - Secure. Does not allow role changes via the request.
  - Example payload:
    ```json
    {
      "user": "alice"
    }
    ```

## How to Run

1. Install dependencies:
    ```bash
    pip install flask
    ```
2. Run the app:
    ```bash
    python app.py
    ```
3. Use a tool like Postman or curl to test the endpoints.

## Purpose

These examples are for educational purposes to demonstrate how improper role validation can lead to privilege escalation vulnerabilities.
