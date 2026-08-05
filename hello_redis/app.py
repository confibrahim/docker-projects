from flask import Flask
import redis

app = Flask(__name__)

# Connect to Redis
r = redis.Redis(
    host="my-redis",
    port=6379,
    db=0,
    decode_responses=True
)

def record_view(content_id: str) -> int:
    key = f"views:{content_id}"
    return r.incr(key)

def get_view_count(content_id: str) -> int:
    return int(r.get(f"views:{content_id}") or 0)

@app.route("/")
def hello_world():
    count = record_view("home")
    return f"CoderCo Containers Session! Views: {count}"

@app.route("/count")
def count():
    count = get_view_count("home")
    return f"Current view count: {count}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)