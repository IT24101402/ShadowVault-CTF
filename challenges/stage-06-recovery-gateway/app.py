from flask import Flask, request

app = Flask(__name__)

EXPECTED_TOKEN = "NV-SV-6204"
EXPECTED_CODE = "IV6"
FINAL_FLAG = "SHADOW{shadowvault_recovered}"


@app.route("/", methods=["GET"])
def index():
    return """
    <h1>ShadowVault Access Gateway</h1>
    <p>Recovery mode requires both authorization factors.</p>

    <form method="POST" action="/unlock">
        <label>Recovery Token:</label><br>
        <input type="text" name="token" placeholder="Enter recovery token"><br><br>

        <label>Verification Code:</label><br>
        <input type="text" name="code" placeholder="Enter verification code"><br><br>

        <button type="submit">Unlock</button>
    </form>
    """


@app.route("/unlock", methods=["POST"])
def unlock():
    token = request.form.get("token", "")
    code = request.form.get("code", "")

    if token == EXPECTED_TOKEN and code == EXPECTED_CODE:
        return f"<h1>Vault unlocked</h1><p>{FINAL_FLAG}</p>"

    return (
        "<h1>Access denied</h1>"
        "<p>Recovery authorization failed.</p>",
        403,
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
