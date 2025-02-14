module.exports = {
  daemon: true,
  run: [
    {
      method: "shell.run",
      params: {
        venv: "env",                // Edit this to customize the venv folder path
        message: [
          'lms server stop',
          'lms server start --cors',
          '{{which("lms")}} unload --all',
          '{{which("lms")}} get deephermes-3-llama-3-8b-preview -y',
          '{{which("lms")}} load deephermes-3-llama-3-8b-preview -y'
        ]
      }
    },
    {
      method: "shell.run",
      params: {
        venv: "env",                // Edit this to customize the venv folder path
        env: { },                   // Edit this to customize environment variables (see documentation)
        message: 'python app.py',
        on: [{
          "event": "/http:\/\/\\S+/",
          "done": true
        }]
      }
    },
    {
      method: "local.set",
      params: {
        url: "{{input.event[0]}}"
      }
    },
  ]
}

