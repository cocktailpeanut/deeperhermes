module.exports = {
  run: [
    {
      method: "shell.run",
      params: {
        venv: "env",
        message: "uv pip install -r requirements.txt"
      }
    }
  ]
}

