from flask import Flask, request

app = Flask(__name__)

EXPECTED_TOKEN = "NV-SV-6204"
FINAL_FLAG = "SHADOW{shadowvault_recovered}"

@app.route("/", methods=["GET"])
def index():
    return """
    <h1>ShadowVault Access Gateway</h1>
    <form method="POST" action="/unlock">
        <input type="text" name="token" placeholder="Enter recovery token">
        <button type="submit">Unlock</button>
    </form>
    """

@app.route("/unlock", methods=["POST"])
def unlock():
    token = request.form.get("token", "")

    if token == EXPECTED_TOKEN:
        return f"<h1>Vault unlocked</h1><p>{FINAL_FLAG}</p>"

    return "<h1>Access denied</h1><p>Invalid recovery token.</p>", 403

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
