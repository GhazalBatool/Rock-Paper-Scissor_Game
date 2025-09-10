let scores = { user: 0, ai: 0, ties: 0 };

function play(move) {
  const mode = document.getElementById("mode").value;

  fetch("/play", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ move: move, mode: mode })
  })
  .then(res => res.json())
  .then(data => {
    const { user, ai, result } = data;

    let msg = "";
    if (result === "user") {
      scores.user++;
      msg = `✅ You win! ${user} beats ${ai}`;
    } else if (result === "ai") {
      scores.ai++;
      msg = `❌ You lose! ${ai} beats ${user}`;
    } else {
      scores.ties++;
      msg = `🤝 It's a tie! Both chose ${user}`;
    }

    document.getElementById("gameOutput").innerText = msg;
    document.getElementById("scoreBoard").innerText =
      `Score → You: ${scores.user} | AI: ${scores.ai} | Ties: ${scores.ties}`;
  });
}
