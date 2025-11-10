````markdown
# GORSE Recommendation Playground

This project demonstrates how to use **Gorse**, an open-source recommender system, to track user feedback and generate recommendations.

---

## Prerequisites

- [Docker](https://www.docker.com/) installed
- `curl` command-line tool
- Optional: Python virtual environment (for other scripts)

---

## Run Gorse Playground

Run Gorse using Docker:

```bash
docker run -p 8088:8088 zhenghaoz/gorse-in-one --playground
````

* Dashboard: [http://127.0.0.1:8088/overview](http://127.0.0.1:8088/overview)
* RESTful API docs: [http://127.0.0.1:8088/apidocs](http://127.0.0.1:8088/apidocs)

This will download the demo dataset and start the server.

---

## API Usage

### 1. Add Feedback

Use the `/api/v1/feedback` endpoint to track user actions:

```bash
curl -X POST http://localhost:8088/api/v1/feedback \
-H "Content-Type: application/json" \
-d '[{"user_id":"user1","item_id":"101","feedback_type":"like","timestamp":1700000000}]'
```

* `user_id` → the ID of the user
* `item_id` → the ID of the item
* `feedback_type` → e.g., `like`, `star`, `read`
* `timestamp` → Unix timestamp (seconds since epoch)

---

### 2. Get Recommendations

Use the `/api/v1/recommend/user/{user_id}` endpoint to get recommendations:

```bash
curl http://localhost:8088/api/v1/recommend/user/user1?n=5
```

* `n` → number of recommended items to return

---

### 3. List Users (Optional)

To check existing users:

```bash
curl http://localhost:8088/api/v1/user
```

---

### Notes

* It may take a few seconds after posting feedback for the model to update and provide recommendations.
* All API endpoints are documented in the Gorse Playground RESTful API docs: [http://127.0.0.1:8088/apidocs](http://127.0.0.1:8088/apidocs)

---

### References

* [Gorse Official Website](https://gorse.io/)
* [Gorse GitHub Repository](https://github.com/zhenghaoz/gorse)

---

### License

MIT License

```

---

